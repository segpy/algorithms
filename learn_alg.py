def two_sum(num_list, target_value):
    num_dict = {}
    for i in range(len(num_list)):
        num_dict[num_list[i]] = i
    for i in range(len(num_list)):
        if target_value - num_list[i] in num_dict:
            return [i, num_dict[target_value - num_list[i]]]


def binary_search(num_list, target_value):
    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == target_value:
            return mid
        elif num_list[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def aumentar_numero_en_string(z, m):
    i = 1
    while i < len(z) and z[i].isdigit():
        i += 1
    numero = int(z[1:i])  # Extrae el número del string
    numero += m  # Aumenta el número
    return (f'Z{numero}{z[i:]}')  # Imprime el nuevo string


if __name__ == "__main__":
    # input
    #     3 2
    # asd 123 Z1
    # Z2
    # Z3xxxx
    # output
    #     Z3
    # Z4
    # Z5xxxx
    n, m = map(int, input().split())
    for _ in range(n):
        z = input().split()
        for i, _ in enumerate(z):
            if z[i][0] == 'Z' and z[i][1].isdigit():
                z[i] = aumentar_numero_en_string(z[i], m)
        print(*z)

    # Prueba
    # print(aumentar_z("Z123", 5))

    # Prueba
    # aumentar_numero_en_string("Z123xasdh", 5)
