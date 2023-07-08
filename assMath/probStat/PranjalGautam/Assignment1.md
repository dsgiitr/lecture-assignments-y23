# Assignment 1

### -Pranjal Gautam

## Q1

We know,

$$
X\rightarrow P(X)=\frac {e^{-\lambda}\lambda^x} {x!}
\newline
Y\rightarrow P(Y)=\frac {e^{-\mu}\mu^y} {y!}
$$

We use the bivariate transformations

$$
U=X, V=X+Y
\newline
P_{uv}(u,v)e^{-(\lambda+\mu)}\frac {\lambda^u\mu^{v-u}} {u!(v-u)!}
\newline
P_{u|v}(u,v)=\frac {\frac {\lambda^u\mu^{v-u}} {u!(v-u)!}}{\sum\frac {\lambda^u\mu^{v-u}} {u!(v-u)!}}
$$

we can multiply and divide by v!

$$
=\frac {\mu^{v-u}\lambda^u} {u!(v-u)!}\cdotp v!\cdotp \frac 1 {(1+\frac {\lambda} {\mu})^v \mu^v}
\newline
=\begin{pmatrix}
   v  \\
   u 
\end{pmatrix}(\frac {\lambda} {\mu})^u\cdotp \frac 1 {(1+\frac {\lambda}{\mu})^v}
\newline
=\begin{pmatrix}
   v  \\
   u 
\end{pmatrix} ({\frac {\lambda}{\lambda+\mu}})^u({\frac {\mu}{\lambda+\mu}})^{v-u}
\newline
v=n,u=x,\frac {\lambda}{\lambda+\mu}=\pi
\newline
=\begin{pmatrix}
   n  \\
   x 
\end{pmatrix} \pi^x(1-\pi)^{n-x}
$$

## Q2

For random samples X1,X2,X3…Xk,

$$
P(X_n=\frac 1 n)=1 - \frac 1 {n^2}
\newline
P(x_n=n)=\frac 1 {n^2}
$$

For convergence in probability,

$$
lim_{n\rightarrow \infin}P(|X_n-E(X_n)|>\epsilon)=0
$$

We calculate P(X=0) and E(X) for n tending to infinity

$$
lim_{n\rightarrow \infin}E(X)=\frac 2 n -\frac 1 {n^2}=0
\newline
lim_{n\rightarrow \infin}P(X_n=\frac 1 {n^2})=1-\frac 1 {n^2}
\newline
P(X_n=0)=1
\newline
lim_{n\rightarrow \infin}P(|X_n-E(X_n)|<\epsilon)=1
$$

## Q3

We know.

$$
P(X=0)=1,
\newline
E(X) exists
$$

$$
P(X>x)=1-F_X(x)
\newline
\int_0^{\infin}P(X>x)dx
$$

Assume Fx(x)=1 for some x>A

$$
=\int_0^A(1-F_X(x))dx
\newline
=A-\int_0^AF_X(x)dx
\newline
=A-[xF_X(x)]^A_0+\int^A_0xf_x(x)dx
\newline
=A-A+E(X)=E(X)
$$

## Q4

We know the Kellback-Lieber divergence is given by

$$
D_{KL}=\int p(x)\space log(\frac {p(x)} {q(x)})dx
$$

Where,

$$
p(x)=N(x|\mu,E)
\newline
q(x)=N(x|m,L)
\newline
p(x)=\frac 1 {\sqrt{2\pi}E}e^{- \frac 1 2 (\frac {x-\mu} {E})^2}
\newline
q(x)=\frac 1 {\sqrt{2\pi}L}e^{- \frac 1 2 (\frac {x-m} {L})^2}
$$

We can now evaluate the expression for Kellback-Lieber divergence.

$$
D_{KL}=\int \frac 1 {\sqrt{2\pi}L}e^{- \frac 1 2 (\frac {x-m} {L})^2} \space log(\frac {\frac 1 {\sqrt{2\pi}E}e^{- \frac 1 2 (\frac {x-\mu} {E})^2}}

{\frac 1 {\sqrt{2\pi}L}e^{- \frac 1 2 (\frac {x-m} {L})^2}})\space dx
\newline
=\int \frac 1 {\sqrt{2\pi}L}e^{- \frac 1 2 (\frac {x-m} {L})^2} \space (log(E)-log(L)-\frac 12((\frac {x-\mu} {E})^2-(\frac {x-m} {L})^2)dx
\newline
=(log(E)-log(L)- \frac 1 2(\frac {\mu^2} {E^2}-\frac {m^2}{L^2}))+(\frac {\mu} {E^2}-\frac m {L^2})m+(\frac 1 {E^2}-\frac 1 {L^2})(L^2+m^2)
\newline
=(log(E)-log(L)-\frac {\mu^2} {2E^2} -\frac {3m^2} {2L^2}+\frac {\mu m+m^2+L^2} {E^2}-1)
$$

## Q5

We have,

$$
f_{xy}(x,y)=\frac 1 {2\pi(1-p^2)^{\frac 1 2}}e^{-\frac 1 2(x^2-2pxy+y^2)}
\newline
f_x(x)=\int_{-\infin}^{\infin}\frac 1 {2\pi(1-p^2)^{\frac 1 2}}e^{-\frac 1 2(x^2-2pxy+y^2)}dy
\newline
=\frac{e^{-\frac 1 2 x^2}} {2\pi\sqrt{(1-p^2)}} \int_{-\infin}^{\infin}e^{-\frac 1 2 \frac {y^2} {2(1-p^2)}}dy
\newline
=\frac {e^{\frac {-x^2} 2}} {\sqrt{2\pi}}
$$

And due to the symmetry

$$
f_y(y)=\frac {e^{\frac {-y^2} 2}} {\sqrt{2\pi}}
$$

Now,

$$
corr(x,y)=\frac{E(XY)-E(X)E(Y)} {\sigma_x\sigma_y}
$$

Its obvious this is just equal to E(XY), so,

$$
E(XY)=\int_{-\infin}^{\infin}\int_{-\infin}^{\infin}xy\frac 1 {2\pi(1-p^2)^{-\frac 1 2}}e^{-\frac 1 2(x^2-2pxy+y^2)}dxdy
\newline
=\frac {1}{\sqrt{2\pi}}\int_{-\infin}^{\infin}y {e^{\frac {-y^2} 2}} \int_{-\infin}^{\infin}xe^{-\frac 1 2 \frac {(x-py)^2} {(1-p^2)}}dxdy
\newline
=\frac 1 {2\pi}p \int_{-\infin}^{\infin}y^2e^{-\frac 1 2y^2}dy
\newline
=\frac {\sqrt{2\pi}p} {\sqrt{2\pi}}=p
$$

$$
Corr(x^2,y^2)=\frac {E(X^2Y^2)-E(X^2)E(Y^2)} {\sigma_{x^2}\sigma_{y^2}}
\newline
E(X^2)=E(Y^2)=\sigma_{x}^2+\mu_x^2=1
\newline
\sigma_{x^2}=\sqrt{2}=\sigma_{y^2}
\newline
E(X^2Y^2)=\int_{-\infin}^{\infin}\int_{-\infin}^{\infin}x^2y^2\frac 1 {2\pi(1-p^2)^{-\frac 1 2}}e^{-\frac 1 2(x^2-2pxy+y^2)}dxdy
=1+2p^2
\newline
Corr(x^2,y^2)=\frac {1+2p^2-1} {(\sqrt{2})^2}
=p^2
$$

## Q6

$$
X \thicksim Gamma(\alpha,\beta)
\newline
X=\frac 1 {\Gamma{a}\beta^{\alpha}}x^{\alpha-1}e^{-\frac x{\beta}}
\newline
\alpha=n,\beta=x
$$

Now we know,

$$
Y\thicksim Gamma(n,\beta)
\newline
Where\space Y=nX,
\newline X\thicksim Exponential(\beta)
$$

So,

$$
X_1+X_2....+X_n=Y
\newline
E(Y)=nE(X_i)=n\beta
\newline
\sigma_y=n(\frac{\sigma_x}{\sqrt{n}})=\sqrt{n}\beta
$$

Now, due to CLT

$$
\frac {Y-E(Y)}{\sigma_y}\thicksim N(0,1)
\newline
Y-n\beta\thicksim N(0,n\beta^2)
\newline
Y \thicksim N(n\beta,n\beta^2)
$$

So,

$$
Gamma(n,3)\thicksim N(3n,9n)
$$

For large n.