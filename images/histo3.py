#!/usr/bin/env python 
import cv2
import numpy as np 
import matplotlib.pyplot as plt

for i in range(10,30):
    plt.figure(figsize=(20,6))
    image=cv2.imread("/home/jose/images/dst"+str(i)+"/histo_frame.jpg")
    image2=cv2.imread("/home/jose/images/dst"+str(i)+"/window.jpg")
    plt.subplot(2,2,1)
    plt.title('Mapping in perspective inverse',size=25)
    plt.xlabel('Image columns.',size = 20)
    plt.ylabel('Image rows.',size = 20)
    plt.yticks(size = 20)
    plt.xticks(size = 20)
    fig =plt.imshow(image2)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    histogram = np.sum(image[:,:],axis=0) 
    histogram = (1/256)*histogram
    histogram = histogram.astype(int)
    plt.subplot(2,2,2)
    plt.title('Histogram.')
    plt.plot(histogram)
    plt.xlabel('Column number in the image.')
    plt.ylabel('Normalized sum of color intensity (H).')
    #plt.savefig("/home/jose/Desktop/opencv/dst"+str(i)+'/hist'+str(i)+'.png')
    #plt.savefig('hist'+str(i)+'.png')
    plt.savefig("/home/jose/images/dst"+str(i)+'/hist_R'+str(i)+'.png')