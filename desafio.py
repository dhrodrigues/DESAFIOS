while True:
    try:
        number = int(input("Digite um número inteiro: "))
        if number % 2 == 0:
            print("O número é par\n")
        else:
            print("O número é ímpar\n")
        break
    except ValueError:
        print("Não é um número inteiro. Tente novamente.\n")
