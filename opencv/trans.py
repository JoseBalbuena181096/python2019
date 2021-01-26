#!/usr/bin/env python 
import cv2
import numpy as np 
import matplotlib.pyplot as plt

for i in range(10,30):
    plt.figure(figsize=(20,15))
    image=cv2.imread("/home/jose/Desktop/opencv/src/sample"+str(i-10)+".jpg")
    image2=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/img_points.jpg")
    image3=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/bright.jpg")
    image4=cv2.imread("/home/jose/Desktop/opencv/dst"+str(i)+"/gray.jpg")
    plt.subplot(2,2,1)
    plt.title('Original image', size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.', size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image)

    plt.subplot(2,2,2)
    plt.title(' Selected area to change its perspective.', size = 23)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.', size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image2)

    plt.subplot(2,2,3)
    plt.title('Mapping in perspective inverse ', size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.', size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image3)

    plt.subplot(2,2,4)
    plt.title('Grayscale',size = 25)
    plt.xlabel('Image columns.', size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image4)
    #plt.savefig('winR'+str(i)+'.png')
    plt.savefig('/home/jose/Desktop/opencv/dst'+str(i)+'/srcC'+str(i)+'.png')