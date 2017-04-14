# -*- coding: utf-8 -*-
__author__ = 'Seran'

import cv2

vidcap = cv2.VideoCapture('../movie/test2.mp4')

count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()

    if(int(vidcap.get(1)) % 20 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("../images/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1


vidcap.release()
