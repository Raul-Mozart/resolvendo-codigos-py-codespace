sinais = ["+","-","*","/"]

num1 = int(input("Digite o primeiro valor: "))

sinal = input("Que tipo de calculo deseja? (+,-,*,/)\n ")
while sinal not in sinais:
    sinal = input("Por favor, digite um sinal válido (+,-,*,/)\n ")

num2 = int(input("Digite o segundo valor: "))

if sinal == "+":
    print("Soma: ",num1 + num2)
elif sinal == "-":
    print("Subtração: ",num1 - num2)
elif sinal == "*":
    print("Multiplicação: ",num1 * num2)
elif sinal == "/":
    print("Divisão: ",num1 / num2)