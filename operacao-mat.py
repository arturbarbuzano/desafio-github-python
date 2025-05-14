num = int(input("Digite um número:"))
operacao = input("Digite a operação desejada(+,-,*,/):")
num2 = int(input("Digite o segundo número:"))

if (operacao == '+'):
    print("O resultado é:", num+num2)

elif (operacao == "-"):
        print("O resultado é:", num-num2)

elif (operacao == "*"):
        print("O resultado é:", num*num2)
        
elif (operacao == "/"):
        print("O resultado é:", num/num2)