# Neljanda nädala 2. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304039


def listid_sonastikuks(jarjend_1, jarjend_2):

    sonastik = {}

    for i in range(len(jarjend_1)):
        sonastik[jarjend_1[i]] = jarjend_2[i]

    return sonastik