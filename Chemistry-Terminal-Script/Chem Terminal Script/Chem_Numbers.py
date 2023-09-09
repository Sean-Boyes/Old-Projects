# Variable Class
class variable:
    def __init__(self, value = None, type = None, iteration = None):
        self.value = value
        self.type = type
        self.iteration = iteration

# Initalize Variable Objects
volume = variable()
n = variable()
temp = variable()
density = variable()
mass = variable()
pressure = variable()

# Atomic Structure
h = 6.626e-34 # Planck's Cosntant
c = 2.998e10 # Speed of Light
Avogadro = 6.022e23 # Avogadro's number in mol^-1
e = -1.602e-19 # Electron Charge in Coulomb

# Gas constants
R_mol = 8.314 #J mol^-1 K^-1
R_atm = 8.206e-2 # L atm mol^-1 K^-1
R_torr = 62.36 # torr mol^-1 K^-1

# Thermochemistry / Electrochemistry
F = 9.6485e4 # Faraday's Constant in coulombs per mole of electrons