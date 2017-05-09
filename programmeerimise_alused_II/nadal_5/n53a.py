# Viienda nädala 3a. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=308125


def on_rahulik(arvamus1, arvamus2, erinevus):
    if abs(arvamus1 - arvamus2) <= erinevus or arvamus1 * arvamus2 >= 0:
        return True
    return False


def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0

    for i in range(len(arvamused)-1):
        if not on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus):
            dissonantsid += 1

    return dissonantsid


