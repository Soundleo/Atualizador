#atualizador de conteúdo


nomes = ['Alex', 'Simone', 'Bernado', 'Cesar', "Leandro", "Lia"]

indice = int(input('Informe qual o índice desejado:'))
indice -= 1 

# novo nome
nomes[indice] = input('Informe o novo nome: ')

# exibe a lista

for nome in nomes:
    print(nome)