# Teise nädala 5a. ülesanne
# Allikas: https://courses.cs.ut.ee/2017/eprogalused2/spring/Main/PART2C
# Näidis sisendfail(id): korrektne.txt, ebakorrektne.txt

import csv
import re

sisendfaili_nimi = input("Sisestage failinimi: ")

sisendfail = open(sisendfaili_nimi, encoding='UTF-8')

sudoku_maatriks = []
sudoku_rida = []

for rida in sisendfail:
    osad = rida.split()
    for number in range (len(osad)):
        osad[number] = re.sub("[^0-9]", "", osad[number])
        sudoku_rida.append(int(osad[number]))
    sudoku_maatriks.append(sudoku_rida)
    sudoku_rida = []

sisendfail.close()


def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            # Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):
                return False
    return True


def read_korras(maatriks):
    for rida in maatriks:
        if sorted(rida) != list(range(1, 10)):
            return False
    return True


def veerud_korras(maatriks):
    for i in range(9):
        veerg = []
        for j in range(9):
            veerg.append(int(maatriks[j][i]))
        if sorted(veerg) != list(range(1, 10)):
            return False
    return True

if kastid_korras(sudoku_maatriks) and read_korras(sudoku_maatriks) and veerud_korras(sudoku_maatriks):
    print("OK")
else:
    print("VIGA")
