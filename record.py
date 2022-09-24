import cv2
from datetime import datetime


def record():
    cap = cv2.VideoCapture(0)
    time = datetime.now()
    date = time.date()
    hours = time.hour
    minute = time.minute
    sec = time.second
    videoname = 'recording'+str(date)+str(hours)+str(minute)+str(sec)+'.avi'

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(videoname, fourcc, 20.0, (640, 480))
    #output = cv2.VideoWriter(rec_name, fourcc, fps, (int(width), int(height)))
    while True:
        timer = datetime.now()
        date1 = timer.date()
        hours1 = timer.hour
        minute1 = timer.minute
        sec1 = timer.second
        text = str(date) + ' - ' + str(hours) + ' - ' + str(minute) + ' - ' + str(sec)
        _, frame = cap.read()

        cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

        out.write(frame)

        cv2.imshow("esc. to stop", frame)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break