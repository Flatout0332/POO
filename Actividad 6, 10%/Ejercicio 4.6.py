class Profesor:

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):

    def __init__(self):
        self.años = 0

    def imprimir(self):
        print("Es un profesor titular.")

    def imprimir_años(self):
        print("Años =", self.años)


if __name__ == "__main__":

    profesor1 = ProfesorTitular()
    profesor1.imprimir_años()