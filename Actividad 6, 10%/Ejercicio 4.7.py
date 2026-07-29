from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        self.sonido = ""
        self.alimentos = ""
        self.habitat = ""
        self.nombre_cientifico = ""

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


class Canido(Animal):
    pass


class Perro(Canido):
    def get_sonido(self):
        return "Ladrido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Doméstico"

    def get_nombre_cientifico(self):
        return "Canis lupus familiaris"


class Lobo(Canido):
    def get_sonido(self):
        return "Aullido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Bosque"

    def get_nombre_cientifico(self):
        return "Canis lupus"


class Felino(Animal):
    pass


class Leon(Felino):
    def get_sonido(self):
        return "Rugido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Praderas"

    def get_nombre_cientifico(self):
        return "Panthera leo"


class Gato(Felino):
    def get_sonido(self):
        return "Maullido"

    def get_alimentos(self):
        return "Ratones"

    def get_habitat(self):
        return "Doméstico"

    def get_nombre_cientifico(self):
        return "Felis silvestris catus"


def main():
    animales = [
        Gato(),
        Perro(),
        Lobo(),
        Leon()
    ]

    for animal in animales:
        print(animal.get_nombre_cientifico())
        print("Sonido:", animal.get_sonido())
        print("Alimentos:", animal.get_alimentos())
        print("Hábitat:", animal.get_habitat())
        print()


if __name__ == "__main__":
    main()