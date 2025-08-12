'''Desenvolver um programa para ajudar o setor
de RH a analisar os salários dos colaboradores
de empresa
Crie ua função chamada analisa_salarios() que
receba uma quantidade variável de salários (números reais)
* A função eve realizar as análises
*calcular a média salarial
*Identificar o menor salário e o maior salário
*Contar quantos colaboradores ganham acima da média salarial
*Calcular o total  pago em salários


'''

'''def analisa_salarios(salario1,salario2,salario3):
    
    
      
    media = (salario1+ salario2 + salario3) / 3
    print(media)
    
    acima_media = 0
    
    if salario1 > salario2 and salario1 > salario3:
        return f"O maior salário é {salario1}"
    elif salario2 > salario1 and salario2 > salario3:
        return f"O maior salário é {salario2}"
    else:
        return f"O maior salário é {salario3}"
    
    if a > media:
        acima_media += 1
        
    if b > media:
        acima_media += 1
        
    if c > media:
        acima_media += 1
        
    menor = min(salario)'''
    
    
def analisa_salarios(*salarios):
    if not salarios:
        return "Nenhum salário foi fornecido"
    
    #calcular a média salarial
    
    media_salarial = sum(salarios)/ len(salarios)
    
    #Identificação do menor e maior salário
    menor_salario = min(salarios)
    maior_salario = max(salarios)
    
    #contar quantos colaboradores ganham acima da média
    acima_media =  0
    
    for salario in salarios:
        if salario > media_salarial:
            acima_media +=1
            
    #total pago do salário
    
    total_pago = sum(salarios)
    
    #Retornar resultados
    return {
        "media_salarial": media_salarial,
        "menor_salario" : menor_salario,
        "maior_salario" : maior_salario,
        "colaboradores_acima_da_media" : acima_media,
        "total_pago" : total_pago       
    }
print(analisa_salarios(1500,2000,2200,1800,3000,3500))
    
    
    

    
    