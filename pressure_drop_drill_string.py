# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:53:34 2015
Calculates pressure loss in Drill String: use it on your own risk - no warranties whatsoever

@author: D. Djokic
"""

def pipe_coef (id_pipe): #loss coeff through drill pipe
    cpipe = 5.86/(id_pipe**4.86)
    return cpipe
    
def joint_coef (id_joint):  #loss coeff through tool joint
    cjoint = 0.241/(id_joint**4.86)
    return cjoint
    
def collar_coef(id_collar):  #loss coeff through drill collar
    ccollar = 7.2/(id_collar**4.86)
    return ccollar
    
def write_table4 (fn, v1, v2, v3, v4):
	fn.write("\n")
	fn.write(v1)
	fn.write("\t")
	fn.write(v2)
	fn.write("\t")
	fn.write(v3)
	fn.write("\t")
	fn.write(v4)
	return
 
def write_table3 (fn, v1, v2, v3):
     fn.write("\n")
     fn.write(v1)
     fn.write("\t")
     fn.write(v2)
     fn.write("\t")
     fn.write(v3)
     fn.write("\t")
     return
    
#fname = input("Output file name - file will be written in same folder as this script: ")
fname = "Drill_String_losses"
np = input("Number of different drillpipe sizes: ")
nc = input("Number of different drillcollar sizes:")
W = float(input("Mud density, ppg: "))
PV = float(input("Plastic viscosity, centiposes: "))
Q = float(input("Flow rate in gpm: "))

# calculating viscosity correction factor
Vf = (PV/W)**0.14

# pressure drop through pipe and tool joint

pipe_friction = []
joint_friction = []
loss_pipe = []
collar_friction = []
loss_collar = []

for pipes in range (0, np):
    print "Pipe number: ", pipes+1
    pipe_id = float(input("Dill pipe inner dia in inches: "))
    joint_id = float(input("Tool joint inner dia in inches: "))
    pipe_len = float(input("Pipe lenght of current size: "))
    #pipe_l.append(pipe_len)
    cpipe = pipe_coef(pipe_id)
    cjoint = joint_coef(joint_id)
    friction_factor_pipe = round((0.378*(Q/pipe_id)**(-0.14)), 3)
    friction_factor_joint = round((0.378*(Q/joint_id)**(-0.14)), 3)
    pipe_loss = round((0.00001*pipe_len*(cpipe+cjoint)*W*Vf*(Q**1.86)), 3)
    pipe_friction.append(friction_factor_pipe)
    joint_friction.append(friction_factor_joint)
    loss_pipe.append(pipe_loss)
    
# pressure loss through drillcollar
    
for collars in range (0, nc):
    print "Collar number: ", collars+1
    collar_id = float (input("Drill Collar inner dia in inches: "))
    collar_len = float (input("Collar length of current size: "))
    friction_factor_collar = round((0.378*(Q/collar_id)**(-0.14)), 3)
    ccollar = collar_coef(collar_id)
    collar_loss = round((0.00001*collar_len*ccollar*W*Vf*(Q**1.86)), 3)
    collar_friction.append(friction_factor_collar)
    loss_collar.append(collar_loss)
    
total_pipe_loss = sum(loss_pipe)
total_collar_loss = sum(loss_collar)
total_string_loss = total_collar_loss+total_pipe_loss
# output pipes & joints

outfile = fname+".csv"
fn = open (outfile, "a")
fn.write("\n")
fn.write("Pipe and Tool Joint Losses: ")
fn.write("\nPipe No \t Friction Factor Pipe \t Friction Factor Joint \t Pipe Loss [psi]")
for pipes in range (0,np):
    cntp = pipes +1
    write_table4(fn, str(cntp), str(pipe_friction[pipes]),str(joint_friction[pipes]),str(loss_pipe[pipes]))

fn.write("\nTotal loss in pipes and joints in psi: ")
fn.write(str(total_pipe_loss))

#output drill collars
fn.write("\n")
fn.write("\nDrill Collar Losses:")
fn.write("\nCollar No \t Collar Friction Factor \t Collar Loss[psi]")
for collars in range (0, nc):
    cntc = collars+1
    write_table3(fn, str(cntc), str(collar_friction[collars]), str(loss_collar[collars]))

fn.write("\nTotal loss in collars in psi: ")
fn.write(str(total_collar_loss))
fn.write("\n")
fn.write("Total loss in drillstring in psi: ")
fn.write(str(total_string_loss))
fn.write("\n")

print("Total loss in drillstring in psi: ", round(total_string_loss,3))
print("Results are written in file 'Drill_String_losses.csv', located in same folder as script.")
print("Result file import in spreadsheet program")

fn.close

    


    