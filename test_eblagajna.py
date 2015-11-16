from e_blagajna import *

def test_prikaz_cene():
    assert cena_izdelka("mleko") == izdelek["mleko"]
    assert cena_izdelka("kruh") == izdelek["kruh"]
    assert cena_izdelka("jogurt") == izdelek["jogurt"]
    assert cena_izdelka("sir") == izdelek["sir"]
    assert cena_izdelka("banane") == izdelek["banane"]
    assert cena_izdelka("sok") == izdelek["sok"]
    assert cena_izdelka("cokolada") == izdelek["cokolada"]
    assert cena_izdelka("pivo") == izdelek["pivo"]
    assert cena_izdelka("meso") == izdelek["meso"]
    assert cena_izdelka("vino") == izdelek["vino"]
    return "Funkcija cena_izdelka() deluje!"

print test_prikaz_cene()