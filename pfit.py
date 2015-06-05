# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:11:27 2015

formation integrity test:
Formation Integrity Test is the method to test strength of formation and shoe by increasing Bottom Hole Pressure (BHP) to designed pressure. FIT is normally conducted to ensure that formation below a casing shoe will not be broken while drilling the next section with higher BHP or circulating gas influx in a well control situation.

@author: D. Djokic, 2015
"""

FIT = float(input("Required FIT, psi: :"))
CMW = float(input("Current Mud Weight, ppg: "))
SD = float(input("Shoe Depth, feet: "))

PFIT = (FIT-CMW)*0.052*SD
print "Pressure Required for Formation Integity Test (FIT), psi: ", round(PFIT,3)