# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:14:40 2015

Calculates annular velocity: use it on your own riskuse it on your own risk - no warranties whatsoever

@author: D. Djokic, 2015
"""

def formula1 (flow_bbl, annular_cap):
    AV = flow_bbl/annular_cap
    return AV
    
def formula2 (flow_gpm, d_casing, d_pipe):
    AV = (24.51*flow_gpm)/(d_casing**2 - d_pipe**2)
    return AV
    
def formula3 (flow_bbl, d_casing, d_pipe):
    AV = (flow_bbl*1029.4)/(d_casing**2 - d_pipe**2)
    return AV
    
print ("1-Input Flow in bbl and Annular Capacity in bbl/ft")
print ("2-Input Flow in gpm, Inside Dia of casing or hole and Outer dia of pipe")
print ("3-Input Flow in bbl, Inside Dia of casing or hole and Outer dia of pipe")
choice = input ("Choose 1, 2 or 3: ")

if choice == 1:
    flow_bbl=float(input("Input Flow Rate in bbl: "))
    annular_cap = float(input("Input Annular Capacity in bbl/ft: "))
    annular_velocity = formula1(flow_bbl, annular_cap)
    print ("Annular velocity, ft/min: ", round(annular_velocity, 3))
    
elif choice == 2:
    flow_gpm = float(input("Input Flow Rate in gpm: "))
    dc = float(input("Inside Diameter of Casing or Hole size, inch: "))
    dp = float(input("Outer Diameter of Pipe or Collar: "))
    annular_velocity = formula2(flow_gpm, dc, dp)
    print ("Annular velocity, ft/min: ", round(annular_velocity, 3))
    
elif choice == 3:
    flow_bbl=float(input("Input Flow Rate in bbl: "))
    dc = float(input("Inside Diameter of Casing or Hole size, inch: "))
    dp = float(input("Outer Diameter of Pipe or Collar: "))
    annular_velocity = formula3(flow_bbl, dc, dp)
    print ("Annular velocity, ft/min: ", round(annular_velocity, 3))
    
else:
    print ("Wrong Input!!! Try again!")