while True:
    nome = input("Informe seu nome de usuário: ")
    
    if  len(nome) >= 3:
        break
    else:
        print("ERRO: o nome deve conter pelo menos 3 caracteres")
        
        
while True:        

    idade = int(input("Informe sua idade: "))
    
    if idade > 0 and idade <= 150:
        break
    else:
        print("Idade inválida. A idade deve ser entre 0 e 150")
        
        
while True:
         
    salario = float(input("Informe seu salário: "))
    
    if salario > 0:
        break
    else:
        print("O salário deve ser maior que 0!")
        
while True:   
    genero = input("Informe seu gênero. Pressione F para Feminino, M para Masculino e O para outros: ").upper()
    
    if genero in ["F", "M", "O"]:
        break
        
    else:
        print("Caractere errado. Informe novamente")
        
while True:
    estado_civil = input("Informe seu estado civil (S-Solteiro, C-Casado, V-Viúvo, D-Divorciado): ").upper()
    if estado_civil in ["S", "C", "V", "D"]:
        break
    else:
        print("Opção inválida. Informe S, C, V ou D.\n")
        
print("Informações dadas: \n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Gênero: {genero}")
print(f"Estado civil: {estado_civil}")


