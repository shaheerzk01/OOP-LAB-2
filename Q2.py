# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:25:12 2021

@author: Latitude E5430
"""

minutes = int(input("Enter the minutes : "))
a = 24*60
days = minutes//a
years = days//365
remaining_days = days % 365
print("Number of days in given minutes are ",(years))
print("number of days in given minutes are ",(remaining_days))