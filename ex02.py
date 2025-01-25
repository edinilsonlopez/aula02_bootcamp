#Escreva um programa que calcule a área de um círculo
#, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio do circulo"))
result = math.pi * raio** 2
print(f"{result:.2f}")