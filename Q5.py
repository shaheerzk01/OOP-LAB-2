# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:42:42 2021

@author: Latitude E5430
"""

weight_in_pounds = int(input("Enter your weight in pounds : "))
height_in_inches = int(input("Enter your height in inches"))
weight_in_kg = weight_in_pounds * 0.45356237
height_in_meters = height_in_inches *0.0254
BMI = weight_in_kg/(height_in_inches)**2
print("Body mass index is ",(BMI))