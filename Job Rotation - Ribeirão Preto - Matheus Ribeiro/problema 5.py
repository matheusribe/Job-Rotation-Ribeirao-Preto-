#Função
def inverter_string(string):
    string_invertida = string[::-1]
    return string_invertida


#Main
teste = input('Digite seu a palavra que deseja inverter: ')
print(inverter_string(teste))