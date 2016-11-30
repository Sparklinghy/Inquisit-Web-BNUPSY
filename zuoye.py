import cv2
import numpy

for p in range(1,11):
    work_dir = "C:/Python/zuoye/"
    img = cv2.imread(work_dir+"pic"+str(p)+".jpg")
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    value = [0] * 3
    gray_img1 = numpy.zeros([height, width], numpy.uint8)
    gray_img2 = numpy.zeros([height, width], numpy.uint8)

    i = p*5
    for row in range(height):
        for column in range(width):
            for chan in range(channels):
                value[chan] = img[row, column, chan]
                R = value[2]
                G = value[1]
                B = value[0]
                # new_value = 0.2989 * R + 0.5870 * G + 0.1140 * B
                new_value = 0.2989 * R + 0.5870 * G + 0.1140 * B
                gray_img1[row, column] = new_value
                gray_img2[row, column] = new_value - i 

    new_name1 = "pic"+str(p)+"1.jpg"
    new_name2 = "pic" + str(p) + "2.jpg"
    cv2.imwrite(work_dir + new_name1, gray_img1)
    cv2.imwrite(work_dir + new_name2, gray_img2)
