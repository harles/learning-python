# Teise nädala 3. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304028


def voitis_nurkademangu(manguleht):
    for rida in (0, 4):
        for veerg in (0, 4):
            if not manguleht[rida][veerg] == 'X':
                return False
    return True

def x_peadiagonaalil(manguleht):
    x_arv = 0
    for i in range (5):
        if manguleht[i][i] == 'X':
            x_arv += 1
    return x_arv

def x_korvaldiagonaalil(manguleht):
    x_arv = 0
    for i in range (5):
        if manguleht[i][4-i] == 'X':
            x_arv += 1
    return x_arv

def voitis_diagonaalidemangu(manguleht):
    if x_peadiagonaalil(manguleht) == 5 and x_korvaldiagonaalil(manguleht) == 5:
        return True
    else:
        return False

def voitis_taismangu(manguleht):
    for rida in range (0, 4):
        for veerg in range (0, 4):
            if not manguleht[rida][veerg] == 'X':
                return False
    return True
