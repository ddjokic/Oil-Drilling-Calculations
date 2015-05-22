# -*- coding: utf-8 -*-
"""
Calculates Cutting Carrying Index (CCI)
If CCI <=0.5 hole cleaning is poor
If CCI =>1 hole cleaning is good

use it on your own risk - no warranties whatsoever

@author: D. Djokic, 2015
"""
import math

MW = float(input("Mud weight, ppg: "))
AV = float(input("Annular velocity, ft/min: "))
PV = float(input("Plastic viscosity of mud, centipoise (cp): "))
YP = float(input("Yield point of mud in lb/100sqft: "))

n = 3.322*math.log10((2*PV+YP)/(PV+YP))
K = ((511)**(1-n))*(PV+YP)
CCI = K*(AV*MW)/400000
print "Cutting Carring Index (CCI): ", round(CCI, 3)

if CCI <= 0.5:
    print "Hole Cleaning is Poor!!! Consider increasing annylar velocity or mud weight"
elif CCI >=1.0:
    print "Hole Cleaning is Good"
else:
    print "Hole Cleaning is moderate. Consider increasing annylar velocity or mud weight"