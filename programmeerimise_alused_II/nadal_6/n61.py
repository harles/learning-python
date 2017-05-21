# Kuuenda nädala 1. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=308647

def koosta_nimekiri(nimede_fail_nimi):
    nimekiri = {}

    nimede_fail = open(nimede_fail_nimi, encoding='UTF-8')

    for rida in nimede_fail:
        osad = rida.split()
        nimi = ""

        for osa in range(1, len(osad)):
            if len(nimi) == 0:
                nimi = osad[osa]
            else:
                nimi = nimi + " " + osad[osa]

        nimekiri[osad[0]] = nimi

    nimede_fail.close()

    return nimekiri

def seosta_lapsed_ja_vanemad(laste_fail_nimi, nimede_fail_nimi):

    vanemate_lapsed = {}
    isikud = koosta_nimekiri(nimede_fail_nimi)

    laste_fail = open(laste_fail_nimi, encoding='UTF-8')

    for rida in laste_fail:
        osad = rida.split()

        if isikud[osad[0]] in vanemate_lapsed:
            lapsed = set(vanemate_lapsed[isikud[osad[0]]])
        else:
            lapsed = set()

        lapsed.add(isikud[osad[1]])
        vanemate_lapsed[isikud[osad[0]]] = lapsed

    laste_fail.close()

    return vanemate_lapsed

if __name__ == "__main__":
    print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))

