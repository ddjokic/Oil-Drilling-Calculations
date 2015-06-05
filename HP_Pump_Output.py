# -*- coding: utf-8 -*-
"""
Calculates capacity of Duplex or Triplex HP Mud Pump

@author: D. Djokic, 2015
"""

print "1 - Triplex HP Mud Pump Capacity Calculation"
print "2 - Duplex HP Mud Pump Capacity Calculation"
choice = int(input("Enter your choice- 1 or 2: "))

if choice == 1 or choice == 2:

    eff = float(input("Efficiency in % - 100% will be calculated by default: "))
    LS = float(input("Liner Size, inches: "))
    SL = float(input("Stroke Length, inches: "))
    RD = float(input("Rod Diameter, inches: "))
else:
    print "Only 1 or 2 - Try again"
   

if choice == 1:
    TPO = 0.000243*SL*LS**2
    TPOeff = TPO*eff/100
    print "Triplex pump output @ 100%, bbl/stroke: ", TPO
    print "Triplex pump output @ given efficiency, bbl/stroke: ",TPOeff
elif choice ==2:
    TPO = 0.000162*SL*(2*LS**2-RD**2)
    TPOeff = TPO*eff/100
    print "Duplex pump output @ 100%, bbl/stroke: ", TPO
    print "Duplex pump output @ given efficiency, bbl/stroke: ",TPOeff
else:
    print "============"