# -*- coding: utf-8 -*-
"""
calculates drill collar weight required to prevent buckling: use it on your own risk - no warranties whatsoever
inclination of drill line is from vertical - 0 degrees is vertical hole

@author: Deki
"""

import math

def cos_deg (theta):
    cos_deg = math.cos(math.pi*theta/180)
    return cos_deg

WOB = float(input("Required weight on bit, lib: "))
SF_per = float(input("Safety factor in %: "))
MW = float(input ("Mud Weight in ppg: "))
Angle = float(input("Well inclination in degrees - 0 deg is vertical well: "))

#mud buoyancy factor calc
BF = (65.5 - MW)/65.5

SF = 1+SF_per/100

WDC = (WOB*SF)/(BF*cos_deg(Angle))   

print ("Mud buoyancy factor: ", round(BF,3))
print ("Drill Collar weight in air, lb: ", round(WDC,3))