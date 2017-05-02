# Neljanda nädala 3. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=
import copy


def absoluutne_tabel(jarjend):

    absoluutne_jarjend = copy.deepcopy(jarjend)

    for i in range(len(absoluutne_jarjend)):
        for j in range(len(absoluutne_jarjend[i])):
            if absoluutne_jarjend[i][j] < 0:
                absoluutne_jarjend[i][j] = abs(absoluutne_jarjend[i][j])

    return absoluutne_jarjend


def absolutiseeri_tabel(jarjend):

    absoluutne_jarjend = jarjend

    for i in range(len(absoluutne_jarjend)):
        for j in range(len(absoluutne_jarjend[i])):
            if absoluutne_jarjend[i][j] < 0:
                absoluutne_jarjend[i][j] = abs(absoluutne_jarjend[i][j])
