"""
 todas las clases no abstractas en Python también son públicas a menos que se restrinja el acceso.

"""


# Definición de una clase no abstracta (concreta) con un nombre más descriptivo
class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"

# Uso de la clase no abstracta
employee = Employee("Jane", "Doe")
print(employee.get_full_name())  # Imprime: Jane Doe
