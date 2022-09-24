import cv2
def motion():
    cap = cv2.VideoCapture(0)

    while True:
        val1, f1 = cap.read()
        val2, f2 = cap.read()

        diff = cv2.absdiff(f2, f1)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff = cv2.blur(diff, (5, 5))

        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        c, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(c) > 0:
            for contour in c:
                if cv2.contourArea(contour) < 1000:
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(f1, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(f1, "MOTION", (8, 90), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

        else:
            cv2.putText(f1, "NO-MOTION", (8, 90), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)

        cv2.imshow("press a to exit", f1)

        if cv2.waitKey(1) == 97:
            cap.release()
            cv2.destroyAllWindows()
            break