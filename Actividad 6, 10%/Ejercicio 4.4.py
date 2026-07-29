class Profesor:

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):

    def imprimir(self):
        print("Es un profesor titular.")


if __name__ == "__main__":

    profesor1 = ProfesorTitular()
    profesor1.imprimir()