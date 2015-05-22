#!usr/bin/env python

#Calculates Equivalent Pipe diameter: use it on your own risk - no warranties whatsoever

segment_number = int(input("Number of different diameters: "))

pdiam = []
plength = []
pdia_leng = []

for cnt in range (0, segment_number):
    print "Pipe Segment: ", cnt+1
    pdia = float(input("Diameter of current pipe segment in inches: ")) 
    length = float (input("Lenght of current pipe segment in feet: "))
    pdia_len = pdia*length
    pdiam.append(pdia)
    plength.append(length)
    pdia_leng.append(pdia_len)
    
eq_dia = sum(pdia_leng)/sum(plength)
print "Equivalent pipe diameter in inches: ", eq_dia
