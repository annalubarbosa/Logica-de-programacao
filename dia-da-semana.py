''' Faça uma função dia_da_semana(numero) que recebe um número de 1 a 7
e retorna o nome do dia da semana correspondente, sendo 1 para
"Segunda-feira", 2 para "Terça-feira", 3 para "Quarta-feira", 4 para
"Quinta-feira", 5  para "Sexta-feira", 6 para "Sábado" e 7 para "Domingo'''


def dia_da_semana(numero):
    
 match numero:
        case "1":
            return "Hoje é segunda-feira"
        case "2":
            return "Hoje é terça-feira"
        case "3":
            return "Hoje é quarta-feira"
            
        case "4":
            return "Hoje é quinta-feira"
            
        case "5":
            return "Hoje é sexta-feira"
        case "6":
            return "Hoje é sábado"
        case "7":
            return "Hoje é domingo"
            
        case _:
            return "Dia inválido!"
        
#FORA DA FUNÇÃO!
        
entrada = input("Informe um valor númerico de 1 a 7 e descubra o dia da semana: ")  
 
 #CHAMAR A FUNÇÃO COM VALOR DE ENTRADA
resultado = dia_da_semana(entrada)

print(resultado)
    
            

