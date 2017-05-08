# Viienda nädala 2. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304033


def paarissumma(arv):

    summa = 0

    if (arv % 2) == 1:
        arv -= 1

    if arv > 0:
        summa += arv + paarissumma(arv-2)

    return summa

if __name__ == "__main__":
    print(paarissumma(100))
