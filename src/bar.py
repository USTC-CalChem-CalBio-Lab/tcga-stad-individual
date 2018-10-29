#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:53:24 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd
import csv
import re

cin = pd.read_csv("../bar-tmp/cin.csv")
ebv = pd.read_csv("../bar-tmp/ebv.csv")
gs = pd.read_csv("../bar-tmp/gs.csv")
msi = pd.read_csv("../bar-tmp/msi.csv")
#print(bar["HLA"]) 
name_list = cin["HLA"]
cin_list = cin["Avg_Amount"]
ebv_list = ebv["Avg_Amount"]
gs_list = gs["Avg_Amount"]
msi_list = msi["Avg_Amount"]


cin_csv = open("../bar/cin.csv",'r')
reader = csv.DictReader(cin_csv)
cin_class_list = [row['HLA'] for row in reader]

gs_csv = open("../bar/gs.csv",'r')
reader = csv.DictReader(gs_csv)
gs_class_list = [row['HLA'] for row in reader]

ebv_csv = open("../bar/ebv.csv",'r')
reader = csv.DictReader(ebv_csv)
ebv_class_list = [row['HLA'] for row in reader]

msi_csv = open("../bar/msi.csv",'r')
reader = csv.DictReader(msi_csv)
msi_class_list = [row['HLA'] for row in reader]

for i in range(len(cin_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",cin_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],cin_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",cin_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],cin_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",cin_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],cin_list[i],label = "CIN",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-cin-avg.png",dpi = 2560)
plt.show()

for i in range(len(ebv_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",ebv_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],ebv_list[i],label = "EBV",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",ebv_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],ebv_list[i],label = "EBV",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",ebv_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],ebv_list[i],label = "EBV",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-ebv-avg.png",dpi = 2560)
plt.show()

for i in range(len(gs_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",gs_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],gs_list[i],label = "GS",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",gs_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],gs_list[i],label = "GS",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",gs_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],gs_list[i],label = "GS",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-gs-avg.png",dpi = 2560)
plt.show()

for i in range(len(msi_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",msi_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],msi_list[i],label = "MSI",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",msi_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],msi_list[i],label = "MSI",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",msi_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],msi_list[i],label = "MSI",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-msi-avg.png",dpi = 2560)
plt.show()
