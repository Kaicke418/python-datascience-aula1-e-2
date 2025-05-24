#variaveis
#listas
#print()
#input()
# funções das listas

#e-commerce:

print('PRODUTOS: ')
print('''
id 1 - hd
id 2 - iphone
id 3 - fone
id 4 - notebook
''')

lista_produtos = ['', 'hd', 'iphone', 'fone', 'notebook']
lista_valores = ['', 500.0, 7000.0, 450.0, 8000.0]
carrinho = []
meus_valores = []

produto_1 = int(input('Digite o ID do  produto>>'))
produto_2 = int(input('Digite o ID do  produto>>'))
produto_3 = int(input('Digite o ID do  produto>>'))

carrinho.append(lista_produtos[produto_1])
carrinho.append(lista_produtos[produto_2])
carrinho.append(lista_produtos[produto_3])

meus_valores.append(lista_valores[produto_1])
meus_valores.append(lista_valores[produto_2])
meus_valores.append(lista_valores[produto_3])

soma = sum(meus_valores)

print(f'''SEUS PRODUTOS SÂO:
      {carrinho}
      --------------
      R${soma}
      ''')