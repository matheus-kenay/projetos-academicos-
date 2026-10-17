#3PP1
soma_pares = 0
qtd_pares = 0

soma_impares = 0
qtd_impares = 0

soma_total = 0
qtd_total = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    
    if num == 0:
        break
    
    soma_total += num
    qtd_total += 1
    
    if num % 2 == 0:
        soma_pares += num
        qtd_pares += 1
    else:
        soma_impares += num
        qtd_impares += 1

# Cálculo das médias
media_pares = soma_pares / qtd_pares if qtd_pares > 0 else 0
media_impares = soma_impares / qtd_impares if qtd_impares > 0 else 0

print("\nRESULTADOS:")
print("Quantidade total:", qtd_total)
print("Soma total:", soma_total)
print("Média dos pares:", media_pares)
print("Média dos ímpares:", media_impares)


#3PP2
qtd = 0
soma = 0
maior = None
menor = None
qtd_maior_50 = 0

while True:
    valor = float(input("Digite um valor (0 para sair): "))
    
    if valor == 0:
        break
    
    qtd += 1
    soma += valor
    
    if maior is None or valor > maior:
        maior = valor
    
    if menor is None or valor < menor:
        menor = valor
    
    if valor >= 50:
        qtd_maior_50 += 1

media = soma / qtd if qtd > 0 else 0

print("\nRESULTADOS:")
print("Quantidade:", qtd)
print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Valores >= 50:", qtd_maior_50)


#3PP3
cand1 = cand2 = cand3 = 0
nulos = brancos = 0
total = 0

while True:
    voto = int(input("Digite seu voto (0 para encerrar): "))
    
    if voto == 0:
        break
    
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Código inválido!")
        continue
    
    total += 1

perc_nulos = (nulos / total * 100) if total > 0 else 0
perc_brancos = (brancos / total * 100) if total > 0 else 0

print("\nRESULTADOS:")
print("Candidato 1:", cand1)
print("Candidato 2:", cand2)
print("Candidato 3:", cand3)
print("Nulos:", nulos)
print("Brancos:", brancos)
print("Percentual nulos: {:.2f}%".format(perc_nulos))
print("Percentual brancos: {:.2f}%".format(perc_brancos))


#3PP4
salario_minimo = float(input("Digite o valor do salário mínimo: "))

menos_5 = 0
entre_5_10 = 0
mais_10 = 0
folha_total = 0

while True:
    salario = float(input("Digite o salário (0 para encerrar): "))
    
    if salario == 0:
        break
    
    folha_total += salario
    
    if salario < 5 * salario_minimo:
        menos_5 += 1
    elif salario < 10 * salario_minimo:
        entre_5_10 += 1
    else:
        mais_10 += 1

print("\nRESULTADOS:")
print("Menos de 5 salários mínimos:", menos_5)
print("Entre 5 e 10 salários mínimos:", entre_5_10)
print("10 ou mais salários mínimos:", mais_10)
print("Folha total da empresa:", folha_total)