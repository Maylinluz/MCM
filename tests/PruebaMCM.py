class src:
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(x, y):
        if x == 0 or y == 0:
            return 0
        return abs(x * y) // src.gcd(x, y)

if __name__ == "__main__":

    num1 = int(input("Introduce el número 1: "))
    num2 = int(input("Introduce el número 2: "))

    # Calculamos el MCM
    resultado = src.lcm(num1, num2)

    # Mostramos el resultado
    print(f"El mínimo común múltiplo de {num1} y {num2} es: {resultado}")