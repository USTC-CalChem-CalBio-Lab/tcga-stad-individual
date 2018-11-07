#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:20:22 2018

@author: frank-lsy
"""
import PIL.Image as im

im.MAX_IMAGE_PIXELS = 1000000000 

def joint_image(input_image1, input_image2, label_img, output_image):
    
    joint_image = im.new('RGBA',(16384,20000))
    image1 = im.open(input_image1)
    img1 = image1.crop((0,1400,16384,11500))
    image2 = im.open(input_image2)
    img2 = image2.crop((0,1300,16384,11500))
    image3 = im.open(label_img)
    img3 = image3.resize((2000,2800),im.ANTIALIAS)
    joint_image.paste(img1,(0,0))
    joint_image.paste(img2,(0,9800))
    joint_image.paste(img3,(12700,140))
    joint_image.show()
    joint_image.save(output_image)

#joint_image("bar-cin-avg.png","cin-hla-frequency.png", "cin-label.png", "CIN.png")

#joint_image("bar-ebv-avg.png","ebv-hla-frequency.png", "ebv-label.png", "EBV.png")

#joint_image("bar-msi-avg.png","msi-hla-frequency.png", "msi-label.png", "MSI.png")

#joint_image("bar-gs-avg.png","gs-hla-frequency.png", "gs-label.png", "GS.png")

joint_image("bar-male-avg.png","male-hla-frequency.png", "male-label.png", "MALE.png")

joint_image("bar-female-avg.png","female-hla-frequency.png", "female-label.png", "FEMALE.png")