class Pedido:

    def calcular_pedido(
        self,
        primer_plato,
        costo_primer_plato,
        bebida,
        costo_bebida,
        segundo_plato=None,
        costo_segundo_plato=0,
        postre=None,
        costo_postre=0
    ):

        total = costo_primer_plato + costo_bebida

        descripcion = primer_plato

        if segundo_plato is not None:
            total += costo_segundo_plato
            descripcion += " + " + segundo_plato

        if postre is not None:
            total += costo_postre
            descripcion += " + " + postre

        descripcion += " + " + bebida

        print(f"El costo de {descripcion} es = ${total}")


if __name__ == "__main__":

    pedido1 = Pedido()
    pedido1.calcular_pedido(
        "Sancocho",
        5000,
        "Gaseosa",
        2000
    )

    pedido2 = Pedido()
    pedido2.calcular_pedido(
        "Crema de verduras",
        5000,
        "Gaseosa",
        2000,
        "Churrasco",
        6000
    )

    pedido3 = Pedido()
    pedido3.calcular_pedido(
        "Crema de espinacas",
        5000,
        "Gaseosa",
        2000,
        "Salmón",
        10000,
        "Tiramisú",
        5000
    )