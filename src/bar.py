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
'''
cin_male= pd.read_csv("../lines/cin-male.csv")
ebv_male = pd.read_csv("../lines/ebv-male.csv")
gs_male = pd.read_csv("../lines/gs-male.csv")
msi_male = pd.read_csv("../lines/msi-male.csv")
cin_female = pd.read_csv("../lines/cin-female.csv")
ebv_female = pd.read_csv("../lines/ebv-female.csv")
gs_female = pd.read_csv("../lines/gs-female.csv")
msi_female = pd.read_csv("../lines/msi-female.csv")
'''
male = pd.read_csv("../lines/male.csv")
female = pd.read_csv("../lines/female.csv")
#print(bar["HLA"]) 
name_list = female["HLA"]
'''
cin_male_list = cin_male["Avg_Amount"]
ebv_male_list = ebv_male["Avg_Amount"]
gs_male_list = gs_male["Avg_Amount"]
msi_male_list = msi_male["Avg_Amount"]
cin_female_list = cin_female["Avg_Amount"]
ebv_female_list = ebv_female["Avg_Amount"]
gs_female_list = gs_female["Avg_Amount"]
msi_female_list = msi_female["Avg_Amount"]
'''
male_list = male["Avg_Amount"]
female_list = female["Avg_Amount"]

#print (cin_female_list)
'''
cin_male_csv = open("../lines/cin-male.csv",'r')
reader = csv.DictReader(cin_male_csv)
cin_male_class_list = [row['HLA'] for row in reader]

gs_male_csv = open("../lines/gs-male.csv",'r')
reader = csv.DictReader(gs_male_csv)
gs_male_class_list = [row['HLA'] for row in reader]

ebv_male_csv = open("../lines/ebv-male.csv",'r')
reader = csv.DictReader(ebv_male_csv)
ebv_male_class_list = [row['HLA'] for row in reader]

msi_male_csv = open("../lines/msi-male.csv",'r')
reader = csv.DictReader(msi_male_csv)
msi_male_class_list = [row['HLA'] for row in reader]


cin_female_csv = open("../lines/cin-female.csv",'r')
reader = csv.DictReader(cin_female_csv)
cin_female_class_list = [row['HLA'] for row in reader]

gs_female_csv = open("../lines/gs-female.csv",'r')
reader = csv.DictReader(gs_female_csv)
gs_female_class_list = [row['HLA'] for row in reader]

ebv_female_csv = open("../lines/ebv-female.csv",'r')
reader = csv.DictReader(ebv_female_csv)
ebv_female_class_list = [row['HLA'] for row in reader]

msi_female_csv = open("../lines/msi-female.csv",'r')
reader = csv.DictReader(msi_female_csv)
msi_female_class_list = [row['HLA'] for row in reader]
'''

male_csv = open("../lines/male.csv",'r')
reader = csv.DictReader(male_csv)
male_class_list = [row['HLA'] for row in reader]

female_csv = open("../lines/female.csv",'r')
reader = csv.DictReader(female_csv)
female_class_list = [row['HLA'] for row in reader]


for i in range(len(male_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",male_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],male_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",male_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],male_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",male_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],male_list[i],label = "CIN",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-male.png",dpi = 2560)
plt.show()

for i in range(len(female_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",female_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],female_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",female_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],female_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",female_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],female_list[i],label = "CIN",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-female.png",dpi = 2560)
plt.show()


'''
for i in range(len(cin_male_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",cin_male_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],cin_male_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",cin_male_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],cin_male_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",cin_male_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],cin_male_list[i],label = "CIN",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-cin-male.png",dpi = 2560)
plt.show()

for i in range(len(ebv_male_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",ebv_male_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],ebv_male_list[i],label = "EBV",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",ebv_male_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],ebv_male_list[i],label = "EBV",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",ebv_male_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],ebv_male_list[i],label = "EBV",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-ebv-male.png",dpi = 2560)
plt.show()

for i in range(len(gs_male_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",gs_male_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],gs_male_list[i],label = "GS",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",gs_male_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],gs_male_list[i],label = "GS",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",gs_male_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],gs_male_list[i],label = "GS",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-gs-male.png",dpi = 2560)
plt.show()

for i in range(len(msi_male_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",msi_male_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],msi_male_list[i],label = "MSI",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",msi_male_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],msi_male_list[i],label = "MSI",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",msi_male_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],msi_male_list[i],label = "MSI",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-msi-male.png",dpi = 2560)
plt.show()


for i in range(len(cin_female_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",cin_female_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],cin_female_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",cin_female_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],cin_female_list[i],label = "CIN",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",cin_female_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],cin_female_list[i],label = "CIN",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-cin-female.png",dpi = 2560)
plt.show()

for i in range(len(ebv_female_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",ebv_female_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],ebv_female_list[i],label = "EBV",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",ebv_female_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],ebv_female_list[i],label = "EBV",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",ebv_female_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],ebv_female_list[i],label = "EBV",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-ebv-female.png",dpi = 2560)
plt.show()

for i in range(len(gs_female_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",gs_female_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],gs_female_list[i],label = "GS",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",gs_female_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],gs_female_list[i],label = "GS",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",gs_female_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],gs_female_list[i],label = "GS",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-gs-female.png",dpi = 2560)
plt.show()

for i in range(len(msi_female_class_list)):
    if (re.match("HLA-A[0-9][0-9]:[0-9][0-9]",msi_female_class_list[i])):
        color = '#0000ff'
        plt.bar(name_list[i],msi_female_list[i],label = "MSI",fc=color)
    elif (re.match("HLA-B[0-9][0-9]:[0-9][0-9]",msi_female_class_list[i])):
        color = '#00ff00'
        plt.bar(name_list[i],msi_female_list[i],label = "MSI",fc=color)
    elif (re.match("HLA-C[0-9][0-9]:[0-9][0-9]",msi_female_class_list[i])):
        color = '#ffa500'
        plt.bar(name_list[i],msi_female_list[i],label = "MSI",fc=color)        

plt.ylabel("Number of Neoantigens Per Patient")
plt.xticks=([])
plt.gca().set_xticks([])
plt.savefig("../bar-msi-female.png",dpi = 2560)
plt.show()
'''