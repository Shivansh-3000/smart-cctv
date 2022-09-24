import cv2
import numpy as np

def motiononvideo():

    cap = cv2.VideoCapture("highway1.mp4")

    while True:
        #_, frame = cap.read()
        _, frame1 = cap.read()
        _, frame2 = cap.read()
        height, width, _ = frame1.shape
        #finding region to calculate 4....
        region1 = frame1[340: 720, 400: 1000]
        region2 = frame2[340: 720, 400: 1000]
        diff = cv2.absdiff(region2, region1)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (6, 6))
        _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #masking to find contours to detect edge 2....
        for cnt in contours:
            #Removing unnecessary small objects 3....
            area = cv2.contourArea(cnt)
            if(area>100):
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.putText(region1, "Motion", (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.rectangle(region1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Frame", frame1)
        key = cv2.waitKey(40)
        if key == 97:
            cap.release()
            cap.destroyAllWindows()
            break