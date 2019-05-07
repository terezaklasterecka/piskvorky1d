from random import randrange
import ai

def vyhodnot(herni_pole):
    """ Vyhodnotí stav herního pole a vrátí stav hry

    vstup je herní pole 1-D piškvorek
    výstup
        "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
        "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
        "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
        "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
    """
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    else:
        return "-"

def tah_hrace(herni_pole):
    "Zeptá se hráče, na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče"

    while True:
        pozice = input("Na kterou pozici chces hrát? ")
        if not pozice.isdigit():
            print("Nezadal jsi číslo.")
            continue
        pozice = int(pozice)
        if pozice<0 or pozice>19:
            print("Zadaná pozice {} se nachází mimo herní pole.".format(pozice))
        elif herni_pole[pozice] != "-":
            print("Pole na pozici {} uz je obsazene.".format(pozice))
        else:
            return ai.tah(herni_pole, pozice, "o")

def piskvorky1d():
    "1D piskvorky proti pocitaci"
    herni_pole = 20*"-"
    print(herni_pole)
    stav = "-"
    while stav == "-":
        herni_pole = tah_hrace(herni_pole)
        print(herni_pole)
        stav = vyhodnot(herni_pole)
        if stav=="-":
            print("Hraje počítač:")
            herni_pole = ai.tah_pocitace(herni_pole)
            print(herni_pole)
            stav = vyhodnot(herni_pole)
    if stav=="x":
        print("Vyhrál počítač.")
    elif stav=="o":
        print("Vyhráváš!")
    elif stav=="!":
        print("Remíza.")
    else:
        print("Došlo k nějaké chybě.")
