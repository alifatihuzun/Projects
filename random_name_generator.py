import random

def random_name():

    names = ["Ali", "Fatih", "Ahmet", "Mehmet"]
    surnames = ["Uzun", "Yıldırım", "Karataş", "Taş"]

    print(random.choice(names)+" "+random.choice(surnames))
random_name()