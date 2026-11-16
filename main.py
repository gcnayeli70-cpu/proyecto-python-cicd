def calcular_area(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos")
    return base * altura


if __name__ == "__main__":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = calcular_area(base, altura)
    print(f"Área del rectángulo: {area:.2f}")
