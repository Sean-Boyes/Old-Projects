# ~Chem Conversions~ #
import Chem_Numbers

# Pressure 
def pressureConvert(pressure, type):
    match type:
        case "atm":
            return pressure
        case "kPa":
            return (pressure / 101.3)
        case "mmHg" | "torr":
            return (pressure / 760)
        case "psi":
            return (pressure / 14.1)
        case _:
            print("Not a valid pressure type")
            return False
        
# Temperature
def tempCovert(temp, type):
    match type:
        case "K":
            return temp
        case "C":
            return (temp / + 273)
        case "F":
            return ((temp - 32) * (5/9) + 273) 
        case _:
            print("Not a valid temperature")
            return False
        
# Volume
def volumeConvert(volume, type):
    match type:
        case "L":
            return volume
        case "mL":
            return (volume / 1000)
        case "cm": # cm^3 to meters^3
            return (volume / 1000)
        case _:
            print("Not a valid volume")
            return False