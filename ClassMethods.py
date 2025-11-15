class Person:
    name = "ADNAN"

    @classmethod
    def change_name(cls, name):
        cls.name = name

p = Person()
p.change_name("Adnan DHUDDI")
print(Person.name)  # preferred way to access class variable
