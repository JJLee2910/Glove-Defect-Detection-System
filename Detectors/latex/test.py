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
lower = np.array([73, 89, 54])
upper = np.array([179, 255, 107])
mask = cv2.inRange(hsv_frame, lower, upper)

# Find Contours
# findContours alters the image to show only the glove (blue color)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Detect the defect within the glove
internal_cnt = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] >= 0]

# Find defect
if len(internal_cnt) > 0:
    for i in internal_cnt:

        # Check defect size
        area = cv2.contourArea(i)
        print(area)
        if area <= 10:
            (xd, yd, wd, hd) = cv2.boundingRect(i)

            # Draw rectangle for defect
            cv2.rectangle(frame, (xd, yd), (xd + wd, yd + hd), (0, 0, 255), 1)

            # Crop the image for identifying dirt
            crop_image = frame[yd:yd + hd, xd:xd + wd]

            # Label the defect
            if area:
                # Defect Type: Tearing
                frame = cv2.putText(frame, 'Tearing', (xd, yd - 5), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 0, 255), 1, cv2.LINE_AA)

        # Display the glove mask video
        cv2.imshow('Mask', mask)
        # Display the output video
        cv2.imshow('Output', frame)

cv2.waitKey(0)
# Close all the current windows
cv2.destroyAllWindows()
