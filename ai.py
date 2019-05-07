def tah(herni_pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    if cislo_policka>=len(herni_pole) or cislo_policka<0:
        raise ValueError("Zadane policko se nachazi mimo herni pole.")
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]

def tah_pocitace(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if "-xx" in herni_pole:
        pozice = herni_pole.index("-xx")
    elif "xx-" in herni_pole:
        pozice = herni_pole.index("xx-")+2
    elif "x-x" in herni_pole:
        pozice = herni_pole.index("x-x")+1
    elif "-oo" in herni_pole:
        pozice = herni_pole.index("-oo")
    elif "oo-" in herni_pole:
        pozice = herni_pole.index("oo-")+2
    elif "o-o" in herni_pole:
        pozice = herni_pole.index("o-o")+1
    elif "-x-" in herni_pole:
        if "--x--" in herni_pole:
            pozice = herni_pole.index("--x--")+1
        elif "-x--" in herni_pole:
            pozice = herni_pole.index("-x--")+2
        elif "--x-" in herni_pole:
            pozice = herni_pole.index("--x-")+1
        else:
            pozice = herni_pole.index("-x-")
    elif "--x" in herni_pole:
        pozice = herni_pole.index("--x")+1
    elif "x--" in herni_pole:
        pozice = herni_pole.index("x--")+1
    elif "-o-" in herni_pole:
        if "--o-" in herni_pole:
            pozice = herni_pole.index("--o-")+1
        elif "-o--" in herni_pole:
            pozice = herni_pole.index("--o-")+3
        else:
            pozice = herni_pole.index("-o-")
    elif "---" in herni_pole:
        if "-------" in herni_pole:
            pozice = herni_pole.index("-----")+3
        elif "-----" in herni_pole:
            pozice = herni_pole.index("-----")+2
        else:
            pozice = herni_pole.index("---")+1
    else:
        # nahodne zvoli jedno z neobsazenych poli
        pocet_pozic = herni_pole.count("-")
        poradi_pozice = randrange(0,pocet_pozic)
        pozice = -1
        for i in range(poradi_pozice + 1):
            pozice = herni_pole.index("-",pozice + 1)
    print("Počítač hraje na pozici {}.".format(pozice))
    return tah(herni_pole, pozice, "x")
