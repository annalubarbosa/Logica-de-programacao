#Criar o quadrado do número
quadrado = lambda x: x **2
# lambda é a palavra chave que define a função anônima
#x é o argumento de entrada
#x**2 é a expressão de retorno
print(quadrado(5))

def quadrado(x):
    return x**2

'''Crie uma função anônima que receba um número e retorne "Par" se for par e "Ímpar" se for ímpar'''
par_ou_impar = lambda x: "Par" if x % 2 == 0 else "Ímpar"