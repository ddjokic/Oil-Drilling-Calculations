# -*- coding: utf-8 -*-
"""
Created on Wed May 20 07:20:18 2015

Brine density with Temperature correction calculation: use it on your own risk - no warranties whatsoever

@author: D. Djokic
"""
surface_t = float(input("Surface temperature, F: "))
wellbore_t = float(input("Welbore temperature at true depth, F: "))
brine_density_req = float(input("Density of brine required, ppg: "))

if brine_density_req >8.4 and brine_density_req<9.0:
    weight_loss = 0.0017
elif brine_density_req >9.1 and brine_density_req <11.0:
    weight_loss = 0.0025
elif brine_density_req >11.1 and brine_density_req <14.5:
    weight_loss = 0.0033
elif brine_density_req >14.6 and brine_density_req <17.0:
    weight_loss = 0.0040
elif brine_density_req >17.1 and brine_density_req<19.2:
    weight_loss = 0.0048
else:
    print "\nProvided Weigh Loss Factor(s): "
    print "\nBrine Weight in ppg \t Weight Loss Factor"
    print "\n8.4 - 9.0 \t 0.0017"
    print "\n9.1 - 11.0 \t 0.0025"
    print "\n11.1 - 14.5 \t 0.0033"
    print "\n14.6 - 17.0 \t 0.0040"
    print "\n17.1 - 19.2 \t 0.0048"
    weight_loss = float(input("Enter Weight Loss Factor in ppg: "))

wellbore_t_average = round((surface_t + wellbore_t)/2, 3)
brine_density_mix = round(brine_density_req+(wellbore_t_average-surface_t)*weight_loss, 3)

print "Average Wellbore Temperature, F: ", wellbore_t_average
print "Brine Density to Mix, ppg: ", brine_density_mix