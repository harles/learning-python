# Teise nädala 2. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304027

def kontrolli_veergu(veerg, number):
    alad = [[1, 16], [16, 31], [31, 46], [46, 61], [61, 76]]
    if number in range(alad[veerg][0], alad[veerg][1]):
        return True
    else:
        return False

def on_bingo_tabel(manguvali):
    for rida in manguvali:
        for veerg in range(5):
            print(rida[veerg])
            if kontrolli_veergu(veerg, rida[veerg]) == False:
                return False
    return True
