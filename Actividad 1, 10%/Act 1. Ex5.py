class Main:
    def __init__(self):
        self.x = 20
        self.y = 40
        self.suma = 0
        
    def Operations(self):
        self.suma += self.x
        self.x += (self.y**2)
        self.suma += self.x//self.y

    def display(self):
        main.Operations()
        print(f"El valor de la suma es: {self.suma}")
        
main = Main()
main.display()
