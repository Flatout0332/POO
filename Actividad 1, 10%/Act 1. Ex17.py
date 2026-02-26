class Main:
    def __init__(self):
        self.radius = 0
        self.pi = 3.1416
        self.long = 0
        self.area = 0
    
    def operations(self):
        self.radius = float(input("¿Cuál es el radio del círculo?: "))
        self.long = 2 * self.pi * self.radius
        self.area = self.pi * (self.radius ** 2)

    def display(self):
        self.operations()
        print(f"La longitud del círculo es: {self.long}")
        print(f"El área del círculo es: {self.area}")
        
main = Main()
main.display()

    