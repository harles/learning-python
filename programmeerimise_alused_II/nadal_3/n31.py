# Kolmanda nädala 1. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304040


def symbolite_sagedus(sisend):
    koond = {}

    for tahemark in sisend:
        if not tahemark in koond:
            koond.update({tahemark : 1})
        else:
            koond.update({tahemark : koond[tahemark]+1})

    return koond