# Importing library
from Chem_Numbers import *
import P_Table

# To-Do
# need recursive check

# ~Chem Equations~ #

def get_pressure() -> (int):
    if (volume.value == None):
        # get volume function
        get_volume()
    if (n.value == None):
        # get mole function
        print("need 'n' variable")
        return 0
    if (temp.value == None):
        # get temp function
        print("need 't' variable")
        return 0
    # Run when all variables need are acquired 
    if (temp.value != None) and (n.value != None) and (volume.value != None):
        pressure.value = ( (float(n.value) * R_atm * float(temp.value)) / (float(volume.value)) ) # temp is in kelvin*

def get_volume() -> (int):
    if (density.value == None):
        # get density function
        return 0
    if (mass.value == None):
        # get mass function
        return 0
    if (mass.value != None and density.value != None):
        volume.value = float(mass.value) / float(density.value)
        return
    if (temp.value == None):
        # get temp function
        return 0
    if (n.value == None):
        # get n function
        return 0 
    if (pressure.value == None):
        pressure.value = get_pressure()
    