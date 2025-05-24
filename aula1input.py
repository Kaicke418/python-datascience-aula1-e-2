# INPUT () ENTRADA 

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso // altura ** 2

print(f'''
      
      SEU IMC É {imc}
        
      ''')

print(f'SEU IMC É\n {imc}')
print()
print('SEU IMC É {}'.format(imc))
print('SEU IMC É %s'%(imc))
print('SEU IMC É' + ' ' +  str(imc) )

# CONCATENAR - JUNTAR DADOS DA SAÍDA DO PRINT
