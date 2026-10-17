#2PP1
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))

print('\nEscolha a operação:')
print('+ --> Soma')
print('- --> Subtração')
print('* --> Multiplicação')
print('/ --> Divisão')

operacao = input('Digite a operação desejada:')

if operacao == '+':
    resultado = num1 + num2
    print('Resultado:', resultado)
elif operacao == '-':
    resultado = num1 - num2
    print('Resultado:', resultado)
elif operacao == '*':
    resultado = num1 * num2
    print('Resultado:', resultado)
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print('Resultado:', resultado)
    else:
        print('Erro: divisão por zero não')
else:
    print('Operação inválida')


#2PP2
quantidade = 0
soma = 0
maiores_que_20 = 0

while True:
    valor = float(input('Digite um valor ( ou 0 para sair):'))

    if valor == 0:
        break

    quantidade +=1
    soma += valor

    if valor > 20:
        maiores_que_20 += 1 

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print('Resultados:')
print('Quantidade de valores:', quantidade)
print('Média:', media)
print('Valores maiores que 20:', maiores_que_20)


#2PP3
total_alunos = 0 
aprovados = 0
reprovados = 0 
soma_nota = 0

while True:
    nota = float(input('Digite a nota do aluno:'))

    if nota == -1:
        break

    total_alunos += 1 
    soma_nota += nota

    if nota >= 5:
        aprovados += 1 
    else:
        reprovados += 1

if total_alunos > 0:
    media = soma_nota / total_alunos
else:
    media = 0

print('Resultados:')
print('Total de alunos:', total_alunos)
print('Aprovados:', aprovados)
print('Reprovados:', reprovados)
print('Média da turma:', media)


#2PP4
quantidade = 0
soma_total = 0

soma_pares = 0 
qtd_pares = 0

soma_impares = 0
qtd_impares = 0

while True:
    num = int(input('Digite um número (0 para sair):'))

    if num == 0:
        break
    quantidade += 1 
    soma_total += num

    if num %2 == 0:
        soma_pares += num
        qtd_pares += 1
    else:
        soma_impares += num
        qtd_impares += 1

media_pares = soma_pares / qtd_pares if qtd_pares > 0 else 0
media_impares = soma_impares / qtd_impares if qtd_impares > 0 else 0

print('Resultados:')
print('Quantidade total:', quantidade)
print('Soma total:', soma_total)
print('Média dos pares:', media_pares)
print('Média dos impares:', media_impares)