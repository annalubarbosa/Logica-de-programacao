while True:
    nome = input("Informe seu nome de usuário: ")
    
    if  len(nome) >= 3:
        print("O nome deve conter mais de 3 caracteres")
    else:
        print("Usuário correto!")

    idade = int(input("Informe sua idade: "))
    
    if idade > 0 and idade <= 150:
        print("Idade correta")
        
    salario = float(input("Informe seu salário: "))
    
    if salario < 0:
        print("O salário deve ser um valor maior que 0. Tente novamente")
        continue
    else:
        print("O salário é um valor maior que 0!")
        
    genero = bool(input("Informe seu gênero. Pressione F para Feminino, M para Masculino e O para outros: "))
    
    if genero in ["F", "M", "Outros"]:
        print("Gênero Registrado: {genero}")
        
    else:
        print("Caractere errado. Informe novamente")
        
    estado_civil = input("Informe seu estado civil: ")
    
    if estado_civil in ["S", "C", "V", "D"]:
        print("Estado civil: {genero}")
    else:
        print("Estado civil: {estado_civil}")
        
    break
    
    


        
    