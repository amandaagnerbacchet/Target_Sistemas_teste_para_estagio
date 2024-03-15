def inverter_string(string):
    tamanho = len(string)
    string_invertida = ""
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

def main():
    string_original = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(string_original)
    print("String original:", string_original)
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
