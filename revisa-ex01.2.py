#usando importação

from datetime import datetime


nome =(input("Informe seu nome completo: "))
idade = int(input("Informe sua idade: "))

ano_atual = datetime.now().year

ano_cem = ano_atual + (100 - idade)

print(f"Nome completo: {nome}")
print(f"Idade atual: {idade}")
print(f"Voce terá 100 anos no ano de {ano_cem}")
