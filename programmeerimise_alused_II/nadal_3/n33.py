# Kolmanda nädala 3. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304038

def vordle_lubadusi(lubadused):
    lubadusi = len(lubadused)
    vordlus = []

    for i in range(lubadusi - 1):
        for j in range(i + 1, lubadusi):
            vordlus.append([i, j, len(lubadused[i].intersection(lubadused[j]))])

    return vordlus

def kooslubajad(lubadused):

    uhisosa = vordle_lubadusi(lubadused)

    uhisosa_tulemused = list(zip(*uhisosa))[2]

    suurim_uhisosa_indeks = uhisosa_tulemused.index(max(uhisosa_tulemused))

    return (uhisosa[suurim_uhisosa_indeks][0], uhisosa[suurim_uhisosa_indeks][1])
