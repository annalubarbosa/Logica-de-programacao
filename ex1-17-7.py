'''Construa um programa qu receba o nome e o preço de 5 medicamentos 
de uma drogaria (considere que o usuário informou cinco medicamentos
distintos.) O programa deve informar o nome e o preço do 
medicamento mais barato, bem como a média aritmética dos preços informados.'''

#criar vetor medicamentos
medicamentos = []

#receber o nome e o preço de 5 medicamentos
for i in range(5):
    nome = input(f"Digite o nome do {i+1} ° medicamento: ")
    preco_str = float(input(f"Digite o preço do {1+1} ° medicamento: R$ "))
    preco = float(preco_str. replace(","))
    #replace: subtitui ou muda um valor por outro. Ex: a vírgula por ponto
    medicamentos.append({"nome": nome, "preco":preco})
    
# informar o nome e o preço do medicamento mais barato
mais_barato = min(medicamentos, key=lambda x: x['preco'])

#função anônima(lambda): função sem nome
#lambda argumentos : expressão
#argumentos x parâmetros
#parametro = declarando na definição de uma função/método
#argumento = valor real que fornece ao chamar a função

media = sum(medicamento["preco"] for medicamento in medicamentos)/5

print(f"\n Medicamento mais barato: {mais_baratos["nome"]} (R$) {mais_barato}")
