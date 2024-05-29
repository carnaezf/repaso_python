class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
        self.surname = surname
    
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Christell", "Rodríguez")
print(my_person.full_name)  # Imprime: Christell Rodríguez
print(my_person.surname)    # Imprime: Rodríguez
my_person.walk()            # Imprime: Christell Rodríguez está caminando






 










