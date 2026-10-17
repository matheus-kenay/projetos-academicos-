#4PP1
ct = 0
VF = int(input('Qual o valor final desejado?'))
for i in range(0,VF):
    print(i)
    i = i + 1
print(f"Quantidade dos valores: {i}")


#4PP2
ct = 0
VI = int(input('Qual o valor inicial desejado?'))
for i in range(VI,-1,-1):
    print(i)
    ct = ct + 1
print(f"Quantidade dos valores: {ct}")


#4PP3
impar = 0
M3 = 0
for i in range (0,501):
    if i % 2 == 1:
        impar = impar + i
    if i % 3 == 0:
        M3 = M3 + i
print(f"a soma dos numeros impares e multiplos de 3 = {impar + M3}")


#4PP4
for lado_esquerdo in range(7):
    for lado_direito in range(7):
        print(f"{lado_esquerdo} - {lado_direito}")
        

#4PP5
for lado_esquerdo in range(7):
    for lado_direito in range(lado_esquerdo, 7):
        print(f"{lado_esquerdo} - {lado_direito}")


#4PP5
for lado_esquerdo in range(7):
    for lado_direito in range(lado_esquerdo, 7):
        print(f"{lado_esquerdo} - {lado_direito}")


#4PP6
for lado_esquerdo in range(7):
    for lado_direito in range(lado_esquerdo, 7):
        print(f"{lado_esquerdo} - {lado_direito}")

