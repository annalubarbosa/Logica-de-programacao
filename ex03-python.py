'''Crie uma função'''

def maior_de_tres(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >=a and b >= c:
        print(b)
    else:
        print(c)
    

maior_de_tres(10, 25, 07)

#def maior_de_tres_2(num1,num2,num3):
#   return max(num1,num2,num3)

#maior_de_tres_2(10, 25, 7)

def maior_de_tres_com_input(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >=a and b >=c:
        print(b)
    else:
        print(c)


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


