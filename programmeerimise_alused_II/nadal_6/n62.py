# Kuuenda nädala 2. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=308759

def kuup(jarj, i = 0, kuup_jarj=[]):

    if i < len(jarj):

        kuup_jarj.append(jarj[i] ** 3)

        kuup(jarj, i+1, kuup_jarj)

    return kuup_jarj

if __name__ == "__main__":
    print(kuup([0, 1, 3]))
