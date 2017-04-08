# Esimese nädala ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=302356
# Näidis sisendfail: kalad.txt
import math

suurim_kala_kaal = 0
kaal = 0

def kala_kaal(kala_pikkus, tüsedusindeks):

    kaal = round(math.pow(kala_pikkus, 3) * tüsedusindeks / 100)

    return kaal

if __name__ == "__main__":

    sisendfail_nimi = input("Sisestage failinimi: ")
    alammõõt = int(input("Sisestage püügi alammõõt: "))
    tüsedusindeks = float(input("Sisestage Fultoni tüsedusindeks: "))

    sisendfail = open(sisendfail_nimi, encoding='UTF-8')

    for kala_pikkus in sisendfail:
        if int(kala_pikkus) < alammõõt:
            print("Kala lasti vette tagasi")
        else:
            kaal = kala_kaal(int(kala_pikkus), tüsedusindeks)
            print("Püütud kala kaaluga",kaal, "grammi")

            if kaal > suurim_kala_kaal:
                suurim_kala_kaal = kaal

    print("Kõige raskem püütud kala:", round(suurim_kala_kaal/1000, 3),"kg")

