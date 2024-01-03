def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n-1)


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibo_numb(n):
    if n <= 1:
        return n
    else:
        return fibo_numb(n-1) + fibo_numb(n-2)


def fibo_seq(n):
    for i in range(n+1):
        print(fibo_numb(i), end=" ")
    print()


def generar_secuencia(n):
    if n == 0:
        return []
    secuencia_anterior = generar_secuencia(n-1)
    nueva_secuencia = secuencia_anterior + [n]
    return nueva_secuencia


num_list = [2, 7, 11, 15]
target_value = 9


def main():
    # print(sum_natural(4))
    # print(factorial(5))
    # print(fibo_numb(6))
    # fibo_seq(6)
    # Ejemplo de uso de la función
    resultado = generar_secuencia(5)
    print(resultado)  # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
