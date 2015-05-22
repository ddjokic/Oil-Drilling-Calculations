# -*- coding: utf-8 -*-
"""
Calculates pressure required to break mud gel strength after loss of circulation: use it on your own risk - no warranties whatsoever

@author: D. Djokic
"""
def annulus (gel_strength, string_L):
    dhole = float(input("Hole Diameter in inches: "))
    dst_out = float(input("Outer Diameter of Pipe in inches: "))
    pann = gel_strength/(300*(dhole-dst_out))*string_L
    return pann
    
def d_string (gel_strength, string_L):
    dpipe = float(input("Drill Pipe inner Diameter in inches: "))
    ppipe = gel_strength/300/dpipe*string_L
    return ppipe

print "1-Calculate Pressure Required to break gell strength in annulus"
print "2-Calculate Pressure required to break gell strenght in drill string"
print "3-Calculates both, 1 and 2"
choice = input("Enter 1, 2 or 3: ")

gel_strength = float(input ("Enter 10 min Gel Strength of Drilling Fluid in lb/100 sq ft: " ))
string_L = float(input("Length of Drill String, ft: "))

if choice == 1:
    pr_ann = annulus (gel_strength, string_L)
    print "Pressure required to break gel strength in annulus, psi: ", round(pr_ann, 3)
elif choice ==2:
    pr_pipe = d_string (gel_strength, string_L)
    print "Pressure required to break gel strength in drill string, psi: ", round(pr_pipe,3)
elif choice == 3:
    pr_ann = annulus (gel_strength, string_L)
    pr_pipe = d_string (gel_strength, string_L)
    pr_total = round (pr_ann, 3) + round(pr_pipe, 3)
    print "Pressure required to break gel strength in annulus, psi: ", round(pr_ann, 3)
    print "Pressure required to break gel strength in drill string, psi: ", round(pr_pipe,3)
    print "Pressure required to break gel strength in annulus AND drill string, psi: ", pr_total
else:
    print "Wrong input - only 1, 2 or 3. Try again"