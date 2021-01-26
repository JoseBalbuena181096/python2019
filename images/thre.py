#!/usr/bin/env python 
import cv2
import numpy as np 
import matplotlib.pyplot as plt

for i in range(10,30):
    plt.figure(figsize=(20,15))
    image2=cv2.imread("/home/jose/images/dst"+str(i)+"/dilate.jpg")
    image3=cv2.imread("/home/jose/images/dst"+str(i)+"/threshold.jpg")
    image4=cv2.imread("/home/jose/images/dst"+str(i)+"/filter_width.jpg")
    image=cv2.imread("/home/jose/images/dst"+str(i)+"/gray.jpg")
    plt.subplot(2,2,1)
    plt.title('Grayscale')
    plt.xlabel('Image columns.')
    plt.ylabel('Image rows.')
    fig =plt.imshow(image)

    plt.subplot(2,2,2)
    plt.title('Median filter')
    plt.xlabel('Image columns.')
    plt.ylabel('Image rows.')
    fig =plt.imshow(image2)

    plt.subplot(2,2,3)
    plt.title('Thresholding')
    plt.xlabel('Image columns.')
    plt.ylabel('Image rows.')

    fig =plt.imshow(image3)

    plt.subplot(2,2,4)
    plt.title('White width filter')
    plt.xlabel('Image columns.')
    plt.ylabel('Image rows.')
    fig =plt.imshow(image4)
    #plt.savefig('winR'+str(i)+'.png')
    plt.savefig('/home/jose/images/dst'+str(i)+'/filters'+str(i)+'.png')