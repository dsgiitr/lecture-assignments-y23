# vim: expandtab:ts=4:sw=4
import numpy as np
import scipy.linalg


"""
Table for the 0.95 quantile of the chi-square distribution with N degrees of
freedom (contains values for N=1, ..., 9). Taken from MATLAB/Octave's chi2inv
function and used as Mahalanobis gating threshold.
"""
### Don't change
chi2inv95 = {
    1: 3.8415,
    2: 5.9915,
    3: 7.8147,
    4: 9.4877,
    5: 11.070,
    6: 12.592,
    7: 14.067,
    8: 15.507,
    9: 16.919,
}


class KalmanFilter(object):
    """
    A simple Kalman filter for tracking bounding boxes in image space.

    The 8-dimensional state space

        x, y, a, h, vx, vy, va, vh

    contains the bounding box center position (x, y), aspect ratio a, height h,
    and their respective velocities.

    Object motion follows a constant velocity model. The bounding box location
    (x, y, a, h) is taken as direct observation of the state space (linear
    observation model).

    """

    def __init__(self):
        dt=1.0

        #State Transition Matrix
        self.F=np.array([[1.0,0.0,0.0,0.0,dt,0.0,0.0,0.0],
                        [0.0,1.0,0.0,0.0,0.0,dt,0.0,0.0],
                        [0.0,0.0,0.1,0.0,0.0,0.0,dt,0.0],
                        [0.0,0.0,0.0,1.0,0.0,0.0,0.0,dt],
                        [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
                        [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
                        [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
                        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]])

        #Measurement Matrix
        self.H=np.array([[1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                        [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
                        [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
                        [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0]])
        
        
        # Create Kalman filter model matrices.
 ##ADD code
        # Motion and observation uncertainty are chosen relative to the current
        # state estimate. These weights control the amount of uncertainty in
        # the model. This is a bit hacky.
##ADD code
        self.position_weight=0.2
        self.velocity_weight=0.2

    def initiate(self, measurement):
        """Create track from unassociated measurement.

        Parameters
        ----------
        measurement : ndarray
            Bounding box coordinates (x, y, a, h) with center position (x, y),
            aspect ratio a, and height h.

        Returns
        -------
        (ndarray, ndarray)
            Returns the mean vector (8 dimensional) and covariance matrix (8x8
            dimensional) of the new track. Unobserved velocities are initialized
            to 0 mean.

        """
        #State covariance matrix
        covariance=np.diag([1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0])
        mean=measurement
        mean=np.append(mean,np.zeros(4,dtype=float))
        cov_factor=10
        for i in range(4):
            covariance[i][i]=mean[i]*cov_factor*self.position_weight
        for i in range(4,8):
            covariance[i][i]=mean[i]*cov_factor*self.velocity_weight
##ADD code
        return mean, covariance

    def predict(self, mean, covariance):
        """Run Kalman filter prediction step.

        Parameters
        ----------
        mean : ndarray
            The 8 dimensional mean vector of the object state at the previous
            time step.
        covariance : ndarray
            The 8x8 dimensional covariance matrix of the object state at the
            previous time step.

        Returns
        -------
        (ndarray, ndarray)
            Returns the mean vector and covariance matrix of the predicted
            state. Unobserved velocities are initialized to 0 mean.

        """
##ADD code
        Q=np.zeros(8)
        for i in range(4):
            Q[i]=mean[i]*self.position_weight
        for i in range(4,8,1):
            Q[i]=mean[i]*self.velocity_weight
        Q=np.diag(Q)
        mean=np.dot(mean,self.F)
        covariance=np.dot(np.dot(self.F,covariance),self.F.T)+Q
        return mean, covariance

    def project(self, mean, covariance):
        """Project state distribution to measurement space.

        Parameters
        ----------
        mean : ndarray
            The state's mean vector (8 dimensional array).
        covariance : ndarray
            The state's covariance matrix (8x8 dimensional).

        Returns
        -------
        (ndarray, ndarray)
            Returns the projected mean and covariance matrix of the given state
            estimate.

        """
##ADD code
        R=np.zeros(4)
        for i in range(4):
            R[i]=mean[i]*self.position_weight
        R=np.diag(R)
        mean=np.dot(mean,self.H)
        covariance=np.dot(np.dot(self.H,covariance),self.H.T)+R
        return mean, covariance

    def update(self, mean, covariance, measurement):
        """Run Kalman filter correction step.

        Parameters
        ----------
        mean : ndarray
            The predicted state's mean vector (8 dimensional).
        covariance : ndarray
            The state's covariance matrix (8x8 dimensional).
        measurement : ndarray
            The 4 dimensional measurement vector (x, y, a, h), where (x, y)
            is the center position, a the aspect ratio, and h the height of the
            bounding box.

        Returns
        -------
        (ndarray, ndarray)
            Returns the measurement-corrected state distribution.

        """
##ADD code
        R=np.zeros(4)
        for i in range(4):
            R[i]=mean[i]*self.position_weight
        R=np.diag(R)
        K=np.dot(np.dot(covariance,self.H.T),np.linalg.inv(np.dot(np.dot(self.H,covariance),self.H.T)+R))
        new_mean=mean+np.dot(K,measurement-np.dot(self.H,mean))
        factor=np.identity(8)-np.dot(K,self.H)
        new_covariance=np.dot(np.dot(factor,covariance),factor.T)+np.dot(np.dot(K,R),K.T)
        return new_mean, new_covariance

    def gating_distance(self, mean, covariance, measurements, only_position=False):
        """Compute gating distance between state distribution and measurements.

        A suitable distance threshold can be obtained from `chi2inv95`. If
        `only_position` is False, the chi-square distribution has 4 degrees of
        freedom, otherwise 2.

        Parameters
        ----------
        mean : ndarray
            Mean vector over the state distribution (8 dimensional).
        covariance : ndarray
            Covariance of the state distribution (8x8 dimensional).
        measurements : ndarray
            An Nx4 dimensional matrix of N measurements, each in
            format (x, y, a, h) where (x, y) is the bounding box center
            position, a the aspect ratio, and h the height.
        only_position : Optional[bool]
            If True, distance computation is done with respect to the bounding
            box center position only.

        Returns
        -------
        ndarray
            Returns an array of length N, where the i-th element contains the
            squared Mahalanobis distance between (mean, covariance) and
            `measurements[i]`.

        """
        ### Don't change anything
        mean, covariance = self.project(mean, covariance)
        if only_position:
            mean, covariance = mean[:2], covariance[:2, :2]
            measurements = measurements[:, :2]

        cholesky_factor = np.linalg.cholesky(covariance)
        d = measurements - mean
        z = scipy.linalg.solve_triangular(
            cholesky_factor, d.T, lower=True, check_finite=False, overwrite_b=True
        )
        squared_maha = np.sum(z * z, axis=0)
        return squared_maha
