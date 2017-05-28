import calendar


def paevikuus(aasta, kuu):
    return calendar.monthrange(aasta, kuu)[1]


def minuteidkuus(aasta, kuu):
    return paevikuus(aasta, kuu) * 24 * 60


def laadiintsidendid(fail):
    intsidendid_nimekiri = open(fail, encoding='UTF-8')
    intsidendid = []

    for rida in intsidendid_nimekiri:
        osad = rida.strip().split(",")
        intsident = []

        for osa in osad:

            if osa.isdigit() == True:
                intsident.append(int(osa))
            else:
                intsident.append(osa)

        intsidendid.append(intsident)

    intsidendid_nimekiri.close()

    return intsidendid


def kuuintsidentidekestvus(intsidendid, systeem, aasta, kuu):

    minuteid = 0

    for intsident in intsidendid:

        if intsident[0] == systeem and intsident[1] == aasta and intsident[2] == kuu:

            minuteid += intsident[4]

    return minuteid


def kuuraport(kaideldavuse_eesmargid, intsidendid, aasta, kuu):
    raport = []

    for rida in kaideldavuse_eesmargid:
        raportirida = []
        minutitearv = minuteidkuus(aasta, kuu)
        intsidentidekestvus = kuuintsidentidekestvus(intsidendid, rida, aasta, kuu)
        tegelikkaideldavus = round((minutitearv-intsidentidekestvus)/minutitearv*100,2)

        raportirida.append(rida)
        raportirida.append(kaideldavuse_eesmargid[rida])
        raportirida.append(minutitearv)
        raportirida.append(intsidentidekestvus)
        raportirida.append(tegelikkaideldavus)
        if kaideldavuse_eesmargid[rida] > tegelikkaideldavus:
            raportirida.append("Ei ole täidetud")
        else:
            raportirida.append("Täidetud")

        raport.append(raportirida)

    return raport

if __name__ == "__main__":
    systeemid = {"Eksamid", "Majutus", "Tudengid"}
    kaideldavuse_eesmargid = {}

    for key in systeemid:
        kaideldavus = 0

        while kaideldavus not in range(1, 100):
            kaideldavus = int(input("Sistesta süsteemi '" + key + "' SLA [1-99]: "))

        kaideldavuse_eesmargid[key] = kaideldavus

    intsidentidefail = input("Intsidendid loen failist: ")
    aruandeaasta = int(input("Aasta number, mille kohta aruannet soovin: "))
    aruandekuu = int(input("Kuu number, mille kohta aruannet soovin: "))

    intsidendid = laadiintsidendid(intsidentidefail)

    print(kuuraport(kaideldavuse_eesmargid, intsidendid, aruandeaasta, aruandekuu))