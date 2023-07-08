import datetime
from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort
import numpy as np

CONFIDENCE_THRESHOLD = 0.8
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# initialize the video capture object
video_cap = cv2.VideoCapture(0)

# load the pre-trained YOLOv8n model
model = YOLO("yolov8l.pt")
tracker = DeepSort(max_age=50)

while True:
    start = datetime.datetime.now()
    ret, frame = video_cap.read()

    if not ret:
        break

    detections = model(frame)[0]

    results = []
    person=[]
    boxes=detections.boxes
    for i in range(len(boxes)):
        data=boxes[i]
        xmin, ymin, xmax, ymax =data.xyxy[0][0].cpu(), data.xyxy[0][1].cpu(), data.xyxy[0][2].cpu(), data.xyxy[0][3].cpu()
        results.append([[xmin, ymin, xmax - xmin, ymax - ymin], data.conf[0].cpu(), data.cls])


    tracks = tracker.update_tracks(results, frame=frame)
    # loop over the tracks
    for track in tracks:
        # if the track is not confirmed, ignore it
        if not track.is_confirmed():
            continue

        # get the track id and the bounding box
        track_id = track.track_id
        ltrb = track.to_ltrb()

        xmin, ymin, xmax, ymax = int(ltrb[0]), int(
            ltrb[1]), int(ltrb[2]), int(ltrb[3])
        # draw the bounding box and the track id
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
        cv2.rectangle(frame, (xmin, ymin - 20), (xmin + 20, ymin), GREEN, -1)
        cv2.putText(frame, str(track_id), (xmin + 5, ymin - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 2)

    # end time to compute the fps
    end = datetime.datetime.now()
    # show the time it took to process 1 frame
    print(f"Time to process 1 frame: {(end - start).total_seconds() * 1000:.0f} milliseconds")
    # calculate the frame per second and draw it on the frame
    fps = f"FPS: {1 / (end - start).total_seconds():.2f}"
    cv2.putText(frame, fps, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

video_cap.release()
cv2.destroyAllWindows()