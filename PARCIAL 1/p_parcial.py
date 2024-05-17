def main():
    while True:
        try:
            inicio = int(input("Ingrese el valor inicial: "))
        except ValueError:
            print("Fin")
            return

        if inicio != 1:
            print("Retornar al inicio")
            continue

        while True:
            if inicio == 2:
                if inicio == 4:
                    print("Paso 6")
                    print("Fin")
                    return
                else:
                    inicio = 5
            else:
                inicio = 3

            if inicio != 1:
                print("Fin")
                break

if __name__ == "__main__":
    main()
