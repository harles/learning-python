# Kuuenda nädala 4a. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304042

def kes_on(number, raamat):

    raamat.sort()

    algus = 0
    lopp = len(raamat)-1
    kesk = (algus + lopp) // 2

    if lopp < 0:
        return None

    if number == raamat[kesk][0]:
        return raamat[kesk][1]

    elif number > raamat[kesk][0]:
        if lopp > kesk:
            return kes_on(number, raamat[kesk+1:lopp+1])
        else:
            return None

    else:
        if kesk > algus:
            return kes_on(number, raamat[0:kesk])
        else:
            return None

if __name__ == "__main__":
    print(kes_on(471020, [(4710209, 'Ernst'), (54125632, 'Uno'), (6524256, 'Arvo')]))