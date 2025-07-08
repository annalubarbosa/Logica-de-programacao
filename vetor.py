#Acessar os elementos
vetor = ["a", "b", "c", 1, 2, 3]
primeiro = vetor[0] # a

#Para destacar os dados ou elementos de vetores, usamos []

#Fatiamento (slicing)
#Pega uma faixa de elementos
sub_vetor = vetor[1:4]
print(sub_vetor)

#Adicionar elementos
vetor.append("d") #adicionar elemento ao final do vetor
print(vetor)

#adicionar vários elementos de uma vez
vetor.extend([4,5])

#Remover elementos
vetor.remove("b")

#Remove elemento por índice(posição)
del vetor[2]

#Atualizar elementos
