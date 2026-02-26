
class Main:
    def __init__(self):
        self.number = 0
        self.square = 0
        self.cube = 0

    def display(self, number):
        print(f"¿Qué valor desea calcular?")
        self.number = int(input())
    
    def calculate(self):
        self.square = self.number ** 2
        self.cube = self.number ** 3
        print(f"El cuadrado de {self.number} es: {self.square}")
        print(f"El cubo de {self.number} es: {self.cube}")
        
main = Main()
main.display(main.number)
main.calculate()