#6PP1
def somar(n1, n2):
    resultado = n1 + n2 
    print(f"O resultado da soma é: {resultado}")
def subtrair(n1, n2):
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")
def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")
def dividir(n1, n2):
    if n2 == 0:
        print("Vixe, erro! O professor falou que não dá pra dividir por zero.")
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado:.2f}")
def main_calculadora():
    print("\n--- MINHA CALCULADORA ---")
    v1 = float(input("Digite o 1º número: "))
    v2 = float(input("Digite o 2º número: "))
    op = input("Qual operação você quer? (+, -, x, /): ")
    if op == '+':
        somar(v1, v2)
    elif op == '-':
        subtrair(v1, v2)
    elif op == 'x':
        multiplicar(v1, v2)
    elif op == '/':
        dividir(v1, v2)
    else:
        print("Operador errado, digita direito na próxima!")
main_calculadora()


#6PP2
def calcular_fatorial(n):
    if n < 0:
        return -1 
    if n == 0 or n == 1:
        return 1
    for i in range(1, n + 1):
        fatorial = fatorial * i 
    return fatorial
def main_fatorial():
    print("\n---  BORA CALCULAR FATORIAL ---")
    numero = int(input("Digite um número inteiro: "))
    resposta = calcular_fatorial(numero)
    if resposta == -1:
        print("Erro: não existe fatorial de número negativo.")
    else:
        print(f"O fatorial de {numero}! é: {resposta}")
main_fatorial()


#6PP3
def calcula_desconto_steam(preco_cheio, porcentagem):
    desconto = preco_cheio * (porcentagem / 100) 
    preco_final = preco_cheio - desconto 
    return preco_final

def main_loja():
    print("\n--- DESCONTOS DA STEAM ---")
    nome_jogo = input("Qual jogo você quer comprar? ")
    preco = float(input(f"Quanto custa {nome_jogo}? R$ "))
    cupom = float(input("Qual o % de desconto da promoção? "))
    
    valor_com_desconto = calcula_desconto_steam(preco, cupom)
    
    print(f"\nBoa! O jogo {nome_jogo} vai sair por apenas R$ {valor_com_desconto:.2f}!")
main_loja()