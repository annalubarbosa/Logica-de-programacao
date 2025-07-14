
funcionarios = []

while True:
    nome = input("Digite o nome do funcionário ( ou 0 para encerrar): ")

    if nome == "0":
        break #parada
    

    if nome.strip() == "":  #Strip: remove espaços em branco
        print("O nome do funcionário não pode estar vazio. Tente novamente!")
        continue

    funcionarios.append(nome)


print("\n Lista de funcionários cadastrados: ")
for i, funcionario in enumerate(funcionarios, 1): #enumerate: repetir sobre a sequencia
#iterar = repetir
#enumerate( objeto a ser percorrido, valor inicial do índice)
    print(f"{i}. {funcionario}")





    