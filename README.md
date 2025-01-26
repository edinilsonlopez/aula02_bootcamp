# Inteiros (int)
    Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

Números de Ponto Flutuante (float)

    Escreva um programa que receba dois números flutuantes e realize sua adição.
    Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
    Faça um programa que converta a temperatura de Celsius para Fahrenheit.

Strings (str)

    Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
    Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

    Escreva um programa que concatene duas strings fornecidas pelo usuário.

Booleanos (bool)

    Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
    Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
    Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
    Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
    Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

Exercícios Resolução
Exercício 1: Soma de Dois Números Inteiros

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 8  # Exemplo de entrada
num2 = 12  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

Exercício 2: Resto da Divisão por 5

# num = int(input("Digite um número: "))
num = 18  # Exemplo de entrada
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

Exercício 3: Multiplicação de Dois Números

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
num1 = 5  # Exemplo de entrada
num2 = 7  # Exemplo de entrada
resultado_multiplicacao = num1 * num2
print("O resultado da multiplicação é:", resultado_multiplicacao)

Exercício 4: Divisão Inteira do Primeiro pelo Segundo Número

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 20  # Exemplo de entrada
num2 = 3  # Exemplo de entrada
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é:", resultado_divisao_inteira)

Exercício 5: Quadrado de um Número

# num = int(input("Digite um número: "))
num = 6  # Exemplo de entrada
resultado_quadrado = num ** 2
print("O quadrado do número é:", resultado_quadrado)

Exercício 6: Adição de Dois Números Flutuantes

# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 2.5  # Exemplo de entrada
num2 = 4.5  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

Exercício 7: Média de Dois Números Flutuantes

# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 3.5  # Exemplo de entrada
num2 = 7.5  # Exemplo de entrada
media = (num1 + num2) / 2
print("A média é:", media)

Exercício 8: Potência de um Número

# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
base = 2.0  # Exemplo de entrada
expoente = 3.0  # Exemplo de entrada
potencia = base ** expoente
print("O resultado da potência é:", potencia)

Exercício 9: Conversão de Celsius para Fahrenheit

# celsius = float(input("Digite a temperatura em Celsius: "))
celsius = 30.0  # Exemplo de entrada
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

Exercício 10: Área de um Círculo

# raio = float(input("Digite o raio do círculo: "))
raio = 5.0  # Exemplo de entrada
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)

Exercício 11: Converter String para Maiúsculas

# texto = input("Digite um texto: ")
texto = "Olá, mundo!"  # Exemplo de entrada
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

Exercício 12: Imprimir Nome Completo em Minúsculas

# nome_completo = input("Digite seu nome completo: ")
nome_completo = "Fulano de Tal"  # Exemplo de entrada
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)

Exercício 13: Remover Espaços em Branco de uma Frase

# frase = input("Digite uma frase: ")
frase = "  Olá, mundo!  "  # Exemplo de entrada
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

Exercício 14: Separar Dia, Mês e Ano de uma Data

# data = input("Digite uma data no formato dd/mm/aaaa: ")
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

Exercício 15: Concatenar Duas Strings

# parte1 = input("Digite a primeira parte do texto: ")
# parte2 = input("Digite a segunda parte do texto: ")
parte1 = "Olá,"  # Exemplo de entrada
parte2 = " mundo!"  # Exemplo de entrada
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

Exercício 16. Operador and (E lógico)

# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

Exercício 17. Operador or (OU lógico)

# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

Exercício 18. Operador not (NÃO lógico)

# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

Exercício 19. Operador == (Igualdade)

# Exemplo de entrada
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

Exercício 20. Operador != (Diferença)

# Exemplo de entrada
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)