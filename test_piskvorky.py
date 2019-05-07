from ai import tah
from piskvorky import vyhodnot
import pytest

def test_tah_mimo_pole():
    try:
        tah(20*"-", 100, "x")
    except ValueError:
        pass
    else:
        assert False,"Chybi ValueError"

def test_zaporne_policko():
    try:
        tah(20*"-", -5, "x")
    except ValueError:
        pass
    else:
        assert False, "Chybi ValueError"

def test_vyhodnot():
    testovaci_vstup1 = '----------------------'
    testovaci_vstup2 = 'ooo-------------------'
    testovaci_vstup3 = '------xxx-------------'
    testovaci_vstup4 = 'xoxoxoxoxxooxoxoxox'
    assert vyhodnot(testovaci_vstup1) == '-'
    assert vyhodnot(testovaci_vstup2) == 'o'
    assert vyhodnot(testovaci_vstup3) == 'x'
    assert vyhodnot(testovaci_vstup4) == '!'
