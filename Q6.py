# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:43:51 2021

@author: Latitude E5430
"""

year = int(input("Enter number of years : "))
a = year*365*24*60*60
birth_per_year = a/7
print("Total birth in a year",int(birth_per_year))
death_per_year = a/13
print("Total death in a year",int(death_per_year))
immigrant_per_year = a/45
print("Total immigrant in a year",int(immigrant_per_year))
rate_per_year = birth_per_year - death_per_year + immigrant_per_year
print("Total population in year is",int(rate_per_year))