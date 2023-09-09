# Importing libraries
from Chem_Numbers import *
import P_Table
import Chem_Conversions
import Chem_Equations
from Input_Handler import *
import os
        
# thisIsVariable 
# this_is_function

# Initial message at start up

os.system('clear')
message = "What variables do you have? \n"
message += "\nenter <help> or <h> for help \n"
print(message)

while True:
    message_handeler(get_input())
