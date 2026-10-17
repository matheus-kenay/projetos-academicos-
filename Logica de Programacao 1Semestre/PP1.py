#1PP1
import math
raio = float(input("Digite o raio da esfera: "))

volume = (4/3) * math.pi * raio**3

print("O volume da esfera é:", volume)




#1PP2
massa = float(input("Digite seu peso em kg: "))

agua = massa * 0.03

print("Você deve beber", agua, "litros de água por dia.")


#1PP3
x1 = float(input("Digite x1:"))
y1 = float(input("Digite y1:"))
x2 = float(input("Digite x2:"))
y2 = float(input("Digite y2:"))
distancia = (((((x2 - x1)**2 + (y2 - y1)**2))**(1/2)))
print("Distancia entre os pontos é:",distancia)


#1PP4
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    print("Ordem crescente:", num1, num2)
else:
    print("Ordem decrescente:", num2, num1)