# Kuuenda nädala 3. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304035

def pikim_pikkus(jarjend):

    def uuenda_pikim(pikim, pikkus):
        if pikkus > pikim:
            pikim = pikkus

        return pikim

    pikim = 0
    pikkus = len(jarjend)

    pikim = uuenda_pikim(pikim, pikkus)

    for element in jarjend:

        if type(element) is list:
            pikkus = pikim_pikkus(element)

            pikim = uuenda_pikim(pikim, pikkus)

    return pikim

if __name__ == "__main__":
    print(pikim_pikkus([[[[[]]]]]))
