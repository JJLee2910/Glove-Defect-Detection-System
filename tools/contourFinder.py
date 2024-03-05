import cv2 as cv
import numpy as np


def find_skin_contours(img):
    img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    skin_lower = np.array([88, 113, 135])
    skin_higher = np.array([255, 255, 355])
    skin_extracted = cv.inRange(img_lab, skin_lower, skin_higher)

    # floodfill from point (0, 0)
    h, w = skin_extracted.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv.floodFill(skin_extracted, mask, (0, 0), 255)
    # invert floodfilled image
    skin_extracted = cv.bitwise_not(skin_extracted)
    # skin_extracted = cv.resize(skin_extracted, None, fx=0.2, fy=.2)

    # cv.imshow("skin_extracted", skin_extracted)

    a_erode = cv.erode(skin_extracted, None, iterations=2)
    # cv.imshow("a_erode", a_erode)

    a_dilate = cv.dilate(a_erode, None, iterations=2)
    # cv.imshow("a_dilate", a_dilate)

    a_fill = cv.morphologyEx(a_dilate, cv.MORPH_CLOSE,
                             np.ones((7, 7), dtype=np.uint8))
    # cv.imshow("a_fill", a_fill)

    a_canny = cv.Canny(a_fill, 0, 255)
    # cv.imshow("a_hole_canny", a_canny)

    # find contours
    a_contours, _ = cv.findContours(
        a_canny,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE
    )

    # cv.drawContours(img, a_contours, -1, (0, 255, 0), 3)
    # img = cv.resize(skin_extracted, None, fx=0.2, fy=.2)
    # cv.imshow("img", img)

    return a_contours


def find_latex_contour(img):
    latex_lower = np.array([73, 89, 54])
    latex_higher = np.array([179, 255, 107])
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    latex_extracted = cv.inRange(img_hsv, latex_lower, latex_higher)
    latex_extracted = cv.bitwise_not(latex_extracted, latex_extracted)
    latex_extracted = cv.erode(latex_extracted, None, iterations=1)
    latex_extracted = cv.dilate(latex_extracted, None, iterations=1)
    # cv.imshow("latex_extracted", latex_extracted)

    latex_contours, hierarchy = cv.findContours(
        latex_extracted,
        cv.RETR_TREE,
        cv.CHAIN_APPROX_SIMPLE
    )
    # cv.imshow("latex_extracted", latex_extracted)
    largest_contour = None
    largest_contour_area = -1
    for i, cnt in enumerate(latex_contours):
        # only get parentless contours
        if hierarchy[0][i][3] != -1:
            continue

        current_contour_area = cv.contourArea(cnt)

        # cv.drawContours(img, [cnt], -1, (0, 255, 0), 2)
        # cv.putText(
        #     img,
        #     tuple(cnt[0][0] + (10, 10)),
        #     cv.FONT_HERSHEY_SIMPLEX,
        #     0.5,
        #     (0, 0, 255),
        #     1,
        #     cv.LINE_AA
        # )

        if largest_contour is None:
            largest_contour = cnt
            largest_contour_area = current_contour_area
        elif current_contour_area > largest_contour_area:
            largest_contour = cnt
            largest_contour_area = current_contour_area

    # cv.drawContours(img, [largest_contour], -1, (0, 255, 0), 2)
    # cv.imshow("latex_hole_extracted", img)
    return largest_contour
