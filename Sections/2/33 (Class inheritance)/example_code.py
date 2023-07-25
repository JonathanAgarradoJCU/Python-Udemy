class Person:
    def __init__(self, name, age, weight_in_kg, height_in_cm, favourite_instrument):
        self.name = name
        self.age = age
        self.weight_in_kg = weight_in_kg
        self.height_in_cm = height_in_cm
        self.favourite_instrument = favourite_instrument
        self.available = True

    def __str__(self):
        return f"({self.name!r}, Age: {self.age}, {self.weight_in_kg}kg, {self.height_in_cm}cm, favourite instrument: {self.favourite_instrument})"
    
    def tag_unavailable(self):
        self.available = False
        print(f"{self.name} is currently not present.")


person = Person("Jasmine Go", 23, 70, 169, "unknown")
print(person)

person2 = Person("Jonathan Agarrado", 22, 102.7, 169, "upright piano")
print(person2)