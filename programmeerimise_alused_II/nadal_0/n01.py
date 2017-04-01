# Kursuse kontrollülesanne
# Allikas: https://courses.cs.ut.ee/2017/eprogalused2/spring/Main/Kontrollylesanne
# Näidis sisendfail: kaugus.txt

def parandatud_tulemus(vigane_tulemus_m, mõõteparandus_cm):
    tegelik_tulemus = round(vigane_tulemus_m + mõõteparandus_cm/100, 2)
    return tegelik_tulemus

if __name__ == "__main__":
    print(parandatud_tulemus(1.1, 35))

    sisendfail_nimi = input("Sisestage failinimi: ")
    parandus_cm = int(input("Sisestage parandus sentimeetrites: "))
    normatiiv_m = float(input("Sisestage meistrivõistluste normatiiv meetrites: "))

    normatiivi_täitjad = 0
    normatiivi_täitjate_tulemuste_summa = 0

    sisendfail = open(sisendfail_nimi, encoding="UTF-8")

    print("Tegelikud tulemused")
    for tulemus in sisendfail:
        tegelik_tulemus = parandatud_tulemus(float(tulemus), parandus_cm)
        print(tegelik_tulemus)

        if tegelik_tulemus >= normatiiv_m:
            normatiivi_täitjad += 1
            normatiivi_täitjate_tulemuste_summa += tegelik_tulemus


    if normatiivi_täitjad >= 1:
        print("Normatiivi täitis",normatiivi_täitjad)
    print("Täitnute keskmine",round(normatiivi_täitjate_tulemuste_summa/normatiivi_täitjad, 2))
