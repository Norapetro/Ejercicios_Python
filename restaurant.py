def obtener_bebida(menu_elegido):
    if menu_elegido == "carne":
        return "vino tinto"
    elif menu_elegido == "pescado":
        return "vino blanco"
    elif menu_elegido == "verdura":
        return "agua"
    else:
        return None 
def main():
    menu_elegido = input("¿Qué menú desea (carne, pescado, verdura)? ").lower()
    bebida_ofrecida = obtener_bebida(menu_elegido)

    if bebida_ofrecida is not None:
        print(f"El acompañamiento al menú de {menu_elegido}, le ofrecemos: {bebida_ofrecida}")
    else:
        print("Elija carne, pescado o verdura.")

if __name__ == "__main__":
    main()
