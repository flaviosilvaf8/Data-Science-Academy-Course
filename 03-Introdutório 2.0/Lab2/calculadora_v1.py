# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Selecione o numero da operação desejada:")

print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

operacao = int(input("Digite a opção desejada (1/2/3/4): "))

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

def soma(): 
    result = str(num1 + num2)
    print('O resultado da soma entre esses dois numeros é: ' + result)

def sub(): 
    result = str(num1 - num2)
    print("O resultado da subtração entre esses dois numeros é: " + result)

def mult(): 
    result = str(num1 * num2)
    print("O resultado da multiplicação entre esses dois numeros é: " + result)

def div(): 
    result = str(num1 / num2)
    print("O resultado da divisão entre esses dois numeros é: " + result)



if operacao == 1:
    soma()

if operacao == 2:
    sub()

if operacao == 3:
    mult()

if operacao == 4:
    div()








