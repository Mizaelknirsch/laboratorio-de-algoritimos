def
    array = list(range(1, 11))
    return array

def mostrar_array(array):
    print("Array na ordem normal:")
    for elemento in array:
        print(elemento, end=" ")
    print("\n")

    print("Array na ordem inversa:")
    for elemento in reversed(array):
        print(elemento, end=" ")
    print("\n")


def main():
    array = preencher_array()
    mostrar_array(array)


if __name__ == "__main__":
    main()
