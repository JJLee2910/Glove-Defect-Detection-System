import cv2
import numpy as np

# Fixed size for all the displayed screen
fixed_size = (550, 550)

image_path = 'C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\tear.jpg'
frame = cv2.imread(image_path)

# Resize the image
frame = cv2.resize(frame, fixed_size, fx=0, fy=0, interpolation=cv2.INTER_CUBIC)

# Convert the image to HSV format
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Mask for detecting glove
lower = np.array([0, 31, 140])
upper = np.array([103, 255, 255])
mask = cv2.inRange(hsv_frame, lower, upper)
# cv2.imshow("og mask", mask)
print(mask)


# Find Contours
# findContours alters the image to show only the glove (blue color)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

# Detect the defect within the glove
internal_cnt = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] >= 0]
# print(internal_cnt)
if len(contours) > 0:
    blue_area = max(contours, key=cv2.contourArea)
    (xg, yg, wg, hg) = cv2.boundingRect(blue_area)

    # # Draw rectangle for glove
    # cv2.rectangle(frame, (xg, yg), (xg + wg, yg + hg), (255, 0, 0), 1)

    # # Label the glove
    # frame = cv2.putText(frame, 'Glove', (xg, yg - 5), cv2.FONT_HERSHEY_SIMPLEX,
    #                     0.5, (255, 0, 0), 1, cv2.LINE_AA)
    
    # Find defect
    if len(internal_cnt) > 0:
        for i in internal_cnt:

            # Check defect size
            area = cv2.contourArea(i)
            print(area)
            if area > 60:
                (xd, yd, wd, hd) = cv2.boundingRect(i)

                # Draw rectangle for defect
                cv2.rectangle(frame, (xd, yd), (xd + wd, yd + hd), (0, 0, 255), 1)

                # Label the defect
                if area > 418:
                    # Defect Type: Tearing
                    frame = cv2.putText(frame, 'Tearing', (xd, yd - 5), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.5, (0, 0, 255), 1, cv2.LINE_AA)

            cv2.imshow('Mask', mask)
            cv2.imshow('Output', frame)
            # cv2.imshow('Contours', frame)

cv2.waitKey(0)
# Close all the current windows
cv2.destroyAllWindows()