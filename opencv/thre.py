#!/usr/bin/env python 
import cv2
import numpy as np 
import matplotlib.pyplot as plt

for i in range(10,30):
    plt.figure(figsize=(20,15))
    image2=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/dilate.jpg")
    image3=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/threshold.jpg")
    image4=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/filter_width.jpg")
    image=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/gray.jpg")
    plt.subplot(2,2,1)
    plt.title('Grayscale', size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.', size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image)

    plt.subplot(2,2,2)
    plt.title('Median filter', size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.', size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image2)

    plt.subplot(2,2,3)
    plt.title('Thresholding', size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.', size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image3)

    plt.subplot(2,2,4)
    plt.title('White width filter',size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image4)
    #plt.savefig('winR'+str(i)+'.png')
    plt.savefig('/home/jose/Desktop/opencv/dst'+str(i)+'/filters'+str(i)+'.png')