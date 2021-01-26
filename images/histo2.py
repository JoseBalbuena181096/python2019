#!/usr/bin/env python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt

for i in range(10,30):
    plt.figure(figsize=(20,6))
    image=cv2.imread("/home/jose/images/dst"+str(i)+"/histo_frame.jpg")
    plt.subplot(2,2,1)
    plt.title('Interest Region of Image.')
    plt.xlabel('Image columns.')
    plt.ylabel('Image rows.')
    fig =plt.imshow(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    histogram = np.sum(image[:,:],axis=0) 
    histogram = (1/256)*histogram
    histogram = histogram.astype(int)
    plt.subplot(2,2,2)
    plt.title('Histogram.')
    plt.plot(histogram)
    midpoint = np.int(histogram.shape[0]/2)
    leftx_base = np.argmax(histogram[:midpoint])
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint
    plt.plot([leftx_base,leftx_base], [0,histogram[leftx_base]],label = "Maximum intensity left.")
    plt.plot([rightx_base ,rightx_base], [0,histogram[rightx_base ]],label = "Maximum intensity rigth.")
    plt.xlabel('Column number in the image.')
    plt.ylabel('Normalized sum of color intensity (H).')
    #plt.savefig("/home/jose/Desktop/opencv/dst"+str(i)+'/hist'+str(i)+'.png')
    plt.legend()
    #plt.savefig('hist'+str(i)+'.png')
    plt.savefig("/home/jose/images/dst"+str(i)+'/hist_A'+str(i)+'.png')