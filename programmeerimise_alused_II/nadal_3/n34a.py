# Kolmanda nädala 4a. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304032
from random import sample

def juhuslik_bingo():

    bingo_tabel = []

    for i in range(0,5):
        rida = sample(range(1+i*15, 16+i*15), 5)
        bingo_tabel.append(rida)

    print(bingo_tabel)

    bingo_tabel = list(map(list, list(zip(*bingo_tabel))))

    return bingo_tabel

if __name__ == "__main__":

    print(juhuslik_bingo())