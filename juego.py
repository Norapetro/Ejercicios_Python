def ingresar_sala(sala_deseada):
    sala_deseada = int(sala_deseada)
    if sala_deseada == 4:
        return "Consola, Juegos 2D, Juegos 3D y Realidad Virtual."
    elif sala_deseada == 3:
        return "Consola, Juegos 2D y Juegos 3D."
    elif sala_deseada == 2:
        return "Consola y Juegos 2D."
    elif sala_deseada == 1:
        return "Consola."

def main():
    sala_deseada = input("¿Cuántas salas de Juego del 1 al 4 desea ingresar? ")
    sala_ofrecida = ingresar_sala(sala_deseada)

    if sala_ofrecida is not None:
        print(f"{sala_deseada} le ofrecemos: {sala_ofrecida}")
    else:
        print("Debe pagar por lo menos 1 sala.")

if __name__ == "__main__":
    main()
