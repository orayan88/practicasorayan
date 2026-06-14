"""Calcula el promedio de 6 edades."""

def promedio_edades(edades):
    return sum(edades) / len(edades)


def main():
    edades = []
    print("Ingrese 6 edades para calcular el promedio:")
    for i in range(1, 7):
        while True:
            try:
                edad = int(input(f"Edad {i}: ").strip())
                if edad < 0:
                    raise ValueError("La edad no puede ser negativa.")
                edades.append(edad)
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}")

    promedio = promedio_edades(edades)
    print(f"\nLas edades ingresadas son: {edades}")
    print(f"El promedio de las 6 edades es: {promedio:.2f}")


if __name__ == "__main__":
    main()
