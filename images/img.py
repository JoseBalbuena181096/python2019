#!/usr/bin/env python 
import cv2
import numpy as np 
import matplotlib.pyplot as plt

for i in range(10,30):
    plt.figure(figsize=(20,15))
    image=cv2.imread("/home/jose/images/dst"+str(i)+"/window.jpg",0)
    image2=cv2.imread("/home/jose/images/dst"+str(i)+"/lines.jpg")
    image4=cv2.imread("/home/jose/images/dst"+str(i)+"/lines_text.jpg")
    image3=cv2.imread("/home/jose/images/dst"+str(i)+"/lines_reference.jpg")
    plt.subplot(2,2,1)
    plt.title('Sliding window search.',size = 25)
    plt.xlabel('Image columns.',size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image)

    plt.subplot(2,2,2)
    plt.title(' Polynomial regression.',size = 25)
    plt.xlabel('Image columns.',size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image2)

    plt.subplot(2,2,3)
    plt.title('Center line.',size = 25)
    plt.xlabel('Image columns.',size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image3)

    plt.subplot(2,2,4)
    plt.title(' Angle of center line.',size = 25)
    plt.xlabel('Image columns.',size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image4)
    #plt.savefig('winR'+str(i)+'.png')
    plt.savefig('/home/jose/images/dst'+str(i)+'/winR'+str(i)+'.png')