class Ejemplo:
    def __init__(self, valor):
        # Inicializa el atributo valor
        self.valor = valor
    
    @staticmethod
    def metodo_estatico():
        # Método estático que no usa self y no depende de ninguna instancia
        print("Este es un método estático")

   
    def metodo_instancia(self):
        # Método de instancia que usa self y depende de una instancia
        print(f"Este es un método de instancia con valor: {self.valor}")



# Crear una instancia de la clase Ejemplo
ejemplo = Ejemplo(42)

# Llamar al método estático
Ejemplo.metodo_estatico()  # Salida: Este es un método estático

# Llamar al método de instancia
ejemplo.metodo_instancia()  # Salida: Este es un método de instancia con valor: 42

