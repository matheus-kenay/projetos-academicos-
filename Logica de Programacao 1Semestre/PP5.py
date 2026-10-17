#5PP1
def mostrar_mensagem(mensagem, numero):
    print("Mensagem:", mensagem)
    print("Número:", numero)


def main():
    mensagem = input("Digite uma mensagem: ")
    numero = int(input("Digite um número: "))

    mostrar_mensagem(mensagem, numero)


main()


#5PP2
def somar_valores(a, b, c):
    soma = a + b + c
    return soma


def main():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    resultado = somar_valores(valor1, valor2, valor3)

    print("Resultado da soma:", resultado)


main()



#5PP3
def calcular_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade


def main():
    ano = int(input("Digite seu ano de nascimento: "))

    idade = calcular_idade(ano)

    print("Sua idade é:", idade, "anos")


main()


#5PP4
def verificar_nota(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


def main():
    nota_aluno = float(input("Digite a nota do aluno: "))

    resultado = verificar_nota(nota_aluno)

    print("Resultado:", resultado)


main()