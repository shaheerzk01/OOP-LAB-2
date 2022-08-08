# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:36:35 2021

@author: Latitude E5430
"""

amount_of_water = eval(input("enter the amount of water in kilograms : "))
final_temperature = int(input("Enter the final temperature : "))
initial_temperature = int(input("Enter the initail temperature : "))
energy = amount_of_water*(final_temperature-initial_temperature)
print("The amonut of energy needed to heat the water is ",(energy),"joules")