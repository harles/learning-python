# Neljanda nädala 1. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304036


def yhisosa(jarjend_1, jarjend_2):

    jarjendite_yhisosa = []

    for j1element in jarjend_1:
        for j2element in jarjend_2:
            if j1element == j2element:
                if not j1element in jarjendite_yhisosa:
                    jarjendite_yhisosa.append(j1element)

    return jarjendite_yhisosa