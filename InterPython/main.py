our_dog = {"name": "bruno", "color": "brown"}
print(our_dog["name"])


def describe(dog):
    return f"{dog['name']} is {dog['color']}"


print(describe(our_dog))


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.energy = 1

    def describe(self):
        return f"{self.name} is {self.color}"

    def exercise(self):
        if self.energy >= 1:
            print(f"You take {self.name} for a walk.")
            self.energy -= 1
        else:
            raise RuntimeError(f"{self.name} is tired. It doesn't want a walk.")

    def feed(self):
        print(f"{self.name} eats the food.")
        self.energy += 1


class EnglishMessage:
    def __init__(self, message):
        self.message = message
        self.letter_to_morse = {
        }

    def encode(self):
        morse = []

        for letter in self.message:
            letter = letter.lower()
            morse.append(self.letter_to_morse[letter])


dog = Dog("bruno", "brown")
print(dog.color)
print(dog.name)
#
# print("This is from error handling")
# print(dog.describe())
# print(dog.exercise())
# print(dog.exercise())
# print(dog.exercise())
try:
    print("This is from error handling")
    dog.describe()
    dog.exercise()
    dog.exercise()
    dog.exercise()
except RuntimeError as e:
    print(f"Something is wrong.{e}")
