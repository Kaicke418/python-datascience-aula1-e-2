lista = []
l = list(range(1, 11))

tupla = (1, 2, 3, 6)
t = tuple(range(1, 11))

print(len(tupla))

#a tupla é imutavel
#a lista é mutável
#é possível criar uma tupla sem os parênteses

#-----------------------------------------

#indexação fatia

tupla = (10, 20, 30, 60)

tupla2 = tupla[0:3]

print(tupla2)

variaveis = 1
lista = [10, 3, 6, 5]
tuplas = (12, 3, 650)
dicionario = {
    'key': 'value1',
    'key': 'value2'
}

pessoa = {
    'nome': 'maria',
    'idade': 15,
    'endereço': 'rua 35',
    'curso': 'python'
}

d = dict(a = 10, b = 30, c = 40)

print(pessoa['curso'])