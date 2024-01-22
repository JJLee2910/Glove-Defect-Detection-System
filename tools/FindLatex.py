import cv2 as cv
import numpy as np

def skinContour(img):
    img_label = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    skin_lower = np.array([45, 105, 85])
    skin_higher = np.array([180, 160, 110])
    skin_extracted = cv.inRange(img_label, skin_lower, skin_higher)

    h,w = skin_extracted.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(skin_extracted, mask, (0,0), 255)
    skin_extracted = cv.bitwise_not(skin_extracted)

    erode = cv.a_erode(skin_extracted, None, iterations=2)

    dilateImg = cv.dilate(erode, None, iterations=2)

    fillImg = cv.morphologyEx(dilateImg, cv.MORPH_CLOSE, np.ones((7,7)), dtype=np.uint8)

    cannyImg = cv.Canny(fillImg, 0, 255)

    # find the contours
    contours = cv.findContours(cannyImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    return contours

def findLatexContour(img):
    latex_lower = np.array([0,0,0])
    latex_higher = np.array([135,206,235]) # adjust accordingly
    hsv_img = cv.cvtColor(img, cv.COLOR_BRR2HSV)
    extractedLatex = cv.inRange(hsv_img, latex_lower, latex_higher)
    extractedLatex = cv.bitwise_not(extractedLatex, extractedLatex)
    extractedLatex = cv.erode(extractedLatex, None, iterations=1)
    extractedLatex = cv.dilate(extractedLatex, None, iterations=1)

    latexContour, hierarchy = cv.findContours(extractedLatex, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    largestContour = None
    largestContourArea = -1
    for i, cnt in enumerate(largestContour):
        if hierarchy[0][i][3] != -1:
            continue

        currentContourArea = cv.contourArea(cnt)


        if largestContour is None:
            largestContour = cnt
        elif currentContourArea > largestContourArea:
            largestContour = cnt
            largestContourArea = currentContourArea

    return largestContour

def findDirtColor(img):
    # normal stain colour
    stain_one_lower = np.array([115, 125, 90])
    stain_one_higher = np.array([145, 155, 105])
    img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    strel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))

    stain_one_extracted = cv.inRange(img_lab,stain_one_lower,stain_one_higher)
    stain_one_extracted = cv.erode(stain_one_extracted,strel,iterations=1)
    stain_one_extracted = cv.dilate(stain_one_extracted,strel,iterations=3)
    stain_one_extracted = cv.Canny(stain_one_extracted, 0, 255)
    stain_one_extracted = cv.morphologyEx(stain_one_extracted,cv.MORPH_CLOSE,strel)


    # black marker stain
    stain_two_lower = np.array([35, 125, 105])
    stain_two_higher = np.array([85, 135, 125])

    stain_two_extracted = cv.inRange(img_lab,stain_two_lower,stain_two_higher)
    stain_two_extracted = cv.morphologyEx(stain_two_extracted,cv.MORPH_CLOSE,strel)
    stain_two_extracted = cv.erode(stain_two_extracted,strel, iterations=1)
    stain_two_extracted = cv.dilate(stain_two_extracted, strel,iterations=3)
    stain_two_extracted = cv.Canny(stain_two_extracted, 0, 255)
    stain_combined_extracted = cv.bitwise_or(stain_one_extracted,stain_two_extracted)

    stain_contours, hierarchy = cv.findContours( stain_combined_extracted,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    return stain_contours
