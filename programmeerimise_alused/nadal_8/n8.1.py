# Arvestusülessanne - lõime pikuse arvutamine

def lõimede_pikkus(vaiba_pikkus, lõimede_arv):
    # Ülesande püstituses ette antud konstandid
    CONST_KOKKUTÕMBE_KOMP = 1.2
    CONST_OTSADEVARU      = 0.5

    # Arvutame lõimede kogupikkuse ja ümardame sentimeetri täpsusega (2 komakohta)
    lõimede_kogupikkus = round((vaiba_pikkus * CONST_KOKKUTÕMBE_KOMP + CONST_OTSADEVARU) * lõimede_arv, 2) 

    return lõimede_kogupikkus

lõimeniit_kokku = 0
vaibad          = []

vaibad_fail_nimi        = input("Sisestage failinimi: ")
lõimede_arv_viis_ja_yle = int(input("Sisestage 5-meetriste ja pikemate vaipade lõimede arv: "))
lõimede_arv_alla_viie   = int(input("Sisestage lühemate vaipade lõimede arv: "))

vaibad_fail = open(vaibad_fail_nimi, encoding="UTF-8")

for rida in vaibad_fail:
    vaibad.append(float(rida.strip("\n")))
    
vaibad_fail.close()

for vaip in vaibad:
    vaiba_pikkus = vaip
    if vaiba_pikkus >= 5:
        vaiba_lõimede_pikkus = lõimede_pikkus(vaiba_pikkus, lõimede_arv_viis_ja_yle)
    else:
        vaiba_lõimede_pikkus = lõimede_pikkus(vaiba_pikkus, lõimede_arv_alla_viie)

    print(vaiba_lõimede_pikkus)
    lõimeniit_kokku += vaiba_lõimede_pikkus

    # Tundub, et kahe komakohaga arvude liitmisel võib nende summa siiski omada rohkem komakohti,
    # ümardame ka siin kahe komakohani 
    lõimeniit_kokku = round(lõimeniit_kokku, 2)

print("Kõigi vaipade peale läheb vaja", lõimeniit_kokku, "meetrit lõimeniiti.")    