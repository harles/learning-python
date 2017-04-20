# Teise nädala 1. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304030

def vahimatest_suurim(jarjend):
    vahimad = []
    for rida in jarjend:
        vahimad.append(min(rida))
    return max(vahimad)