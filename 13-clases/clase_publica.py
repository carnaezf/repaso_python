# Definición de una clase pública con un nombre más descriptivo
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return f"{self.name} {self.surname}"

# Uso de la clase pública
person = Person("Jose", "Arnaez")
print(person.get_full_name())  # Imprime: Jose Arnaez


