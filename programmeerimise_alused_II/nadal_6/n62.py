# Kuuenda nädala 2. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=308759

def kuup(jarj):

    kuup_jarj = []

    if len(jarj) > 0:

        kuup_jarj.append(jarj[0] ** 3)
        jarj.pop(0)

        kuup_jarj += kuup(jarj)

    return kuup_jarj

if __name__ == "__main__":
    print(kuup([]))
