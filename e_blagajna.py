izdelek = {"mleko": 0.80, "kruh": 2.30, "jogurt": 1.10, "sir": 1.50, "banane": 1.29, "sok": 1.45, "cokolada": 3.22, "pivo": 0.88, "meso": 5.70, "vino": 4.57}

#funkcija za prikazovanje cene posameznega izdelka
def cena_izdelka(x):
    cena = izdelek[x]
    return cena

def main():

    print "V nasi trgovini lahko izbiras med naslednjimi izdelki: "
    for x,y in izdelek.iteritems():
        print x

    izbira_izdelka = raw_input("Za prikaz cene vpisite enega izmed zgornjih izdelkov: ")
    if izbira_izdelka in izdelek:
        print "Cena za izdelek %s je: %.2f eur" % (izbira_izdelka, cena_izdelka(izbira_izdelka))
    else:
        print "Tega izdelka v nasi trgovini nimamo na zalogi."

main()

if "__name__" == "__main__":
    main()