# Kolmanda nädala 2. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304041


def failist_sonastik(faili_nimi):
    fail = open(faili_nimi, encoding='UTF-8')
    riikide_register = {}

    for rida in fail:
        osad = rida.split()

        riikide_register.update({osad[0] : osad[1]})

    return riikide_register


def tahised_nimedeks(tahised, riikide_register):
    tulemus = []

    for tahis in tahised:
        if not tahis in riikide_register:
            tulemus.append(None)
        else:
            tulemus.append(riikide_register[tahis])

    return tulemus

if __name__ == "__main__":

    andmebaas_nimi = input("Sisestage andmebaasi faili nimi: ")
    piiriuletajad = input("Piiriületajad: ")

    riikide_register = failist_sonastik(andmebaas_nimi)

    piiriuletajad_riik = tahised_nimedeks(piiriuletajad.split(), riikide_register)

    for riik in piiriuletajad_riik:
        if riik == None:
            print("Tundmatu maa")
        else:
            print(riik)
