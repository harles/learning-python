# Viienda nädala 1. ülesanne
# Allikas: https://moodle.ut.ee/mod/vpl/view.php?id=304034


def alla_ules(arv):

    if arv > 0:
        print(arv)

        alla_ules(arv-2)

        print(arv-1)

    elif arv <= 0:
        print("Põhi!")

if __name__ == "__main__":
    alla_ules(0)
