# Teise nädala 4. ülesanne
# Allikas: https://courses.cs.ut.ee/2017/eprogalused2/spring/Main/PART2C
# Näidis sisendfail: arvud.txt

import csv

sisendfaili_nimi = input("Sisestage failinimi: ")

ridade_summad = []
rea_summa = 0

sisendfail = open(sisendfaili_nimi, encoding='UTF-8')
sisendfail_loetud = csv.reader(sisendfail, delimiter=" ")

for rida in sisendfail_loetud:
    for number in range (len(rida)):
        rea_summa += int(rida[number])
    ridade_summad.append(rea_summa)
    rea_summa = 0
sisendfail.close()

print("Suurim summa on failis " + str(ridade_summad.index(max(ridade_summad))+1) +
       ". real ja see on " + str(max(ridade_summad))+".")
