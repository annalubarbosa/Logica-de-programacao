''' Crie uma função estado_luz(status) que recebe uma string com 
o estado da luz: "ligado", "desligado", "piscando". 
Use match-case para retornar as seguintes mensagens:
"Luz ligada" para "on"
"Luz apagada" para "off"
"Luz piscando" para "blink"
se for qualquer outro valor, "Estado desconhecido"
'''

def estado_luz(status):
    
    match status:
        case "ligada":
            return "On"
        case "desligada":
            return "Off"
        case "piscando":
            return "Blink"
        case _:
            return "Estado desconhecido"
        
print(estado_luz("ligada"))
        
        