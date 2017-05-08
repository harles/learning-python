# Neljanda nädala 4a. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=306897


def on_alglopuline(jarjend):

    if len(jarjend) > 0:
        return jarjend[0] > jarjend[-1]
    else:
        return 0