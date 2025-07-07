#Ler 10 números e imprimir a soma, o maior e o menor
numeros = []

def ler_numeros():
    soma = 0
    maior = None #None: nenhum valor/ valor indefinido
    menor = None


    for i in range(10):
        num = float(input(f"Digite o {i+1}° número: "))  
        #range: gera uma sequência de números inteiros no intervalo. Indica de onde sai de uma posição e até onde termina

        soma +=num

        if maior is None or num> maior:
            maior=num

        if menor is None or num < menor:
            menor=num

print(f"Soma dos números: {soma}")
print(f"Maior número: {maior}")
print(f"menor número:  {menor}")

ler_numeros()
    
