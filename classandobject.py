class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("woo is a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} year old".format(blu.name , blu.age))
print("{} is {} yar old".format(woo.name, woo.age))
