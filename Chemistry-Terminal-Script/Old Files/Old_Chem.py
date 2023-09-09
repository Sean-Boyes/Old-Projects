#Def Var
atm = 1
kPa = 101.3
mmHg = 760
torr = 760
psi = 14.1
Avo = 6.022*10**23
atmcon = .0821
mmhgcon = 62.4
torrcon = 62.4
kPacon = 8.314
#Dictionary
table = { "H":"1.008", "He":"4.003", "Li":"6.941", "Be":"9.012", "B":"10.81", "C":"12.01", "N":"14.01", "O":"16", "F":"19", "Ne":"20.18", "Na":"22.99", "Mg":"24.31", "Al":"26.98", "Si":"28.09", "P":"30.97", "S":"32.07", "Cl":"35.45", "Ar":"39.95", "K":"39.10", "Ca":"40.08", "Sc":"44.96", "Ti":"47.88", "V":"50.94", "Cr":"51.99", "Mn":"54.94", "Fe":"55.85", "Co":"58.93", "Ni":"58.69", "Cu":"63.55", "Zn":"65.39", "Ga":"69.72", "Ge":"72.61", "As":"74.92", "Se":"78.96", "Br":"79.9", "Kr":"83.8", "Rb":"85.47", "Sr":"87.62", "Y":"88.91", "Zr":"91.22", "Nb":"92.91", "Mo":"95.94", "Te":"98", "Ru":"101.07", "Rh":"102.91", "Pd":"106.42", "Ag":"107.87", "Cd":"112.41", "In":"114.82", "Sn":"118.71", "Sb":"121.76", "Te":"127.6", "I":"126.9", "Xe":"131.29", "Cs":"132.91", "Ba":"137.38", "La":"138.91", "Ce":"140.12", "Pr":"140.91", "Nd":"144.24", "Pm":"145", "Sm":"150.36", "Eu":"151.96", "Gd":"157.96", "Tb":"158.93", "Dy":"162.5", "Ho":"164.93", "Er":"167.26", "Tm":"168.93", "Yb":"173.04", "Lu":"174.97", "Hf":"178.49", "Ta":"180.95", "W":"183.84", "Re":"186.21", "Os":"190.23", "Ir":"192.22", "Pt":"195.08", "Au":"196.97", "Hg":"200.59", "Tl":"204.38", "Pb":"207.2", "Bi":"208.98", "Po":"209", "At":"210", "Rn":"222", "Fr":"223", "Ra":"226", "Ac":"227", "Th":"232.04", "Pa":"231.04", "U":"238.04", "Np":"237", "Pu":"244", "Am":"243", "Cm":"247", "Bk":"247", "Cf":"251", "Es":"252", "Fm":"257", "Md":"258", "No":"254", "Lr":"262", "Rf":"261", "Db":"262", "Sg":"263", "Bh":"264", "Hs":"269", "Mt":"268", "Ds":"271", "Rg":"272", "Uub":"277"}
#Functions
def infosplit(info):
    global splitinfo
    splitinfo = info.split(" ")
def pressureconv(pressure):
    global Px
    infosplit(pressure)
    if splitinfo[1] == "atm":
        Px = float(splitinfo[0])
    elif splitinfo[1] == "kPa":
        Px = float(splitinfo[0])/101.3
    elif splitinfo[1] == "mmHg":
        Px = float(splitinfo[0])/760
    elif splitinfo[1] == "torr":
        Px = float(splitinfo[0])/760
    elif splitinfo[1] == "psi":
        Px = float(splitinfo[0])/14.1
def tempconv(T):
    global Tx
    infosplit(T)
    if splitinfo[1] == "K":
        Tx = float(splitinfo[0])
    if splitinfo[1] == "C":
        Tx = float(splitinfo[0])+273
    if splitinfo[1] == "F":
        Tx = ((float(splitinfo[0])-32)*5/9)+273
def volumeconv(V):
    global Vx
    infosplit(V)
    if splitinfo[1] == "L":
        Vx = float(splitinfo[0])
    elif splitinfo[1] == "mL":
        Vx = float(splitinfo[0])/1000
    elif splitinfo[1] == "cm":
        Vx = float(splitinfo[0])/1000
def pressureans():
    print(str(float(Pan)) + " atm")
    print(str(float(Pan)*kPa) + " kPa")
    print(str(float(Pan)*mmHg) + " mmHg")
    print(str(float(Pan)*torr) + " torr")
    print(str(float(Pan)*psi) + " psi")
def volumeans():
    print(str(float(Van)) + " L")
    print(str(float(Van)/1000) + " mL")
def tempans():
    print(str(float(Tan)) + " K")
    print(str(float(Tan) - 273) + " C")
    print(str(((float(Tan) - 273)*(9/5)) + 32) + " F")
def molmass(eq):
    global n
    c = 0
    n = 0
    eqlist = []
    equ = eq.split(" ")
    for x in equ:
        v = equ[c]
        z = v.isnumeric()
        if z is False:
            eqlist.append("false")
            b = table[equ[c]]
            n = float(n) + float(b)
        else:
            eqlist.append("true")
            b = table[equ[c - 1]]
            b = float(b) * (int(equ[c]) - 1)
            n = (n + b)
        c = int(c) + 1
#Code
while 1 == 1:
    problem = input("What type? Density [0] Combined [1] Ideal [2] Effusion [3] ")
    if problem == "0":
        M = input("Mass = ")
        V1 = input("Volume = ")
        if str(V1) != "x":
            volumeconv(V1)
            V1 = Vx
            pass
        D = input("Density = ")
        if str(D) == "x":
            D = float(M)/float(V1)
            print("Density = " + str(D))
        if str(M) == "x":
            M = float(D)*float(V1)
            print("Mass = " + str(M))
        if str(V1) == "x":
            V1 = float(M)/float(D)
            print("Volume = " + str(V1) + " L")
    elif problem == "1":
        P1 = input("P1 = ")
        if str(P1) != "x":
            pressureconv(P1)
            P1 = Px
            pass
        V1 = input("V1 = ")
        if str(V1) != "x":
            volumeconv(V1)
            V1 = Vx
            pass
        T1 = input("T1 = ")
        if str(T1) != "x":
            tempconv(T1)
            T1 = Tx
            pass
        P2 = input("P2 = ")
        if str(P2) != "x":
            pressureconv(P2)
            P2 = Px
            pass
        V2 = input("V2 = ")
        if str(V2) != "x":
            volumeconv(V2)
            V2 = Vx
            pass
        T2 = input("T2 = ")
        if str(T2) != "x":
            tempconv(T2)
            T2 = Tx
            pass
        print(str(P1) + " atm")
        if str(P1) == "x":
            Pan = (float(P2)*float(V2)*float(T1))/(float(V1)*float(T2))
            pressureans()
        if str(P2) == "x":
            Pan = (float(P1)*float(V1)*float(T2))/(float(T1)*float(V2))
            pressureans()
        if str(V1) == "x":
            Van = (float(P2)*float(V2)*float(T1))/(float(P1)*float(T2))
            volumeans()
        if str(V2) == "x":
            Van = (float(P1)*float(V1)*float(T2))/(float(T1)*float(P2))
            volumeans()
        if str(T1) == "x":
            Tan = (float(P1)*float(V1)*float(T2))/(float(P2)*float(V2))
            tempans()
        if str(T2) == "x":
            Tan = (float(P2)*float(V2)*float(T1))/(float(P1)*float(V1))
            tempans()
    elif problem == "2":
        P1 = input("P = ")
        if str(P1) != "x":
            info = P1
            pressureconv(P1)
            P1 = Px
            pass
        V1 = input("V = ")
        if str(V1) != "x":
            info = V1
            volumeconv(V1)
            V1 = Vx
            pass
        n = input("n = ")
        T1 = input("T = ")
        if str(T1) != "x":
            info = T1
            tempconv(T1)
            T1 = Tx
            pass
        if str(P1) == "x":
            P1 = (float(n)*float(atmcon)*float(T1))/(float(V1))
            print("P = " + str(P1) + " atm")
        if str(V1) == "x":
            V1 = (float(n)*float(atmcon)*float(T1))/(float(P1))
            print("V = " + str(V1) + " L")
        if str(n) == "x":
            n = (float(P1)*float(V1))/(float(atmcon)*float(T1))
            print("n = " + str(n) + " mol")
        if str(T1) == "x":
            T = (float(P1)*float(V1))/(float(atmcon)*float(R1))
            print("T = " + str(T1) + " K")
    elif problem == "3":
        R1 = input("R1 = ")
        if str(R1) != "x":
            R1split = R1.split("/")
            volumeconv(R1split[0])
            if R1split[1] == "min":
                R1 = float(Vx)
            elif R1split[1] == "hour":
                R1 = float(Vx)/60
            elif R1split[1] == "sec":
                R1 = float(Vx)*60
        R2 = input("R2 = ")
        if str(R2) != "x":
            R2split = R2.split("/")
            volumeconv(R2split[0])
            if R2split[1] == "min":
                R2 = float(Vx)
            elif R2split[1] == "hour":
                R2 = float(Vx)/60
            elif R2split[1] == "sec":
                R2 = float(Vx)*60
        M1 = input("M1 = ")
        if M1 != "x":
            molmass(M1)
            M1 = n
        M2 = input("M2 = ")
        if M2 != "x":
            molmass(M2)
            M2 = n
        if str(R1) == "x":
            Ans = ((float(M1) / float(M2)) ** .5) * R2
            print(str(Ans) + " L/min")
        elif str(R2) == "x":
            Ans = ((float(M1) / float(M2)) ** .5) * R1
            print(str(Ans) + " L/min")
        elif str(M1) == "x":
            Ans = (float(M2) / ((float(R1) / float(R2)) ** 2))
            print(str(Ans) + " g/mol")
        elif str(M2) == "x":
            Ans = ((float(R1) / float(R2)) ** 2) * M1
            print(str(Ans) + " g/mol")
        else:
            print("Error")
            pass
    print(" ")
