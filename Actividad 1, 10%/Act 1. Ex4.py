class Main:
    def __init__(self, age_juan):
        self.age_juan = age_juan
        self.age_alber = 0
        self.age_ana = 0
        self.age_mama = 0
        
    def operations(self, age_juan):
        self.age_alber = (2 * age_juan) / 3
        self.age_ana = (4 * age_juan) / 3
        self.age_mama = (self.age_juan + self.age_alber + self.age_ana)

    def display(self):
        self.operations(self.age_juan)
        print("La edad de Juan es:", int(self.age_juan))
        print("La edad de Alberto es:", int(self.age_alber))
        print("La edad de Ana es:", int(self.age_ana))
        print("La edad de la mamá es:", int(self.age_mama))


family = Main(9)
family.display()