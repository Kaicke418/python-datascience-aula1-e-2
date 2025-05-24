# # **ATIVIDADE 1**

# Você foi contratado para analisar o desempenho de um grupo de alunos em uma disciplina, você vai analisar apenas pela média. As notas de cada aluno em diferentes provas 
# estão armazenadas em listas. O objetivo é usar listas bidimensionais para representar as notas de cada aluno e realizar algumas análises básicas, como:

# ***Calcular a média das notas de cada aluno.
# Identificar o aluno com a maior média.
# Calcular a média da classe (média geral de todos)***

notas = [[10,10,10],[5,2,3], [5,9,8],[10,0,6]] 

nomes = ['ana', 'fernanda', 'caio', 'fernando']

print(f'as notas do(a) aluno(a) {nomes[0]}, são {notas[0]}, e a média é {sum(notas[0]) / 3}')
print(f'as notas do(a) aluno(a) {nomes[1]}, são {notas[1]}, e a média é {sum(notas[1]) / 3 :.2f}')
print(f'as notas do(a) aluno(a) {nomes[2]}, são {notas[2]}, e a média é {sum(notas[2]) / 3 :.2f}')
print(f'as notas do(a) aluno(a) {nomes[3]}, são {notas[3]}, e a média é {sum(notas[3]) / 3 :.2f}')


print(f'O aluno(a) {nomes[0]} teve a maior nota?', notas[0] > notas[1], notas[0] > notas[2], notas[0] > notas[3])
print(f'O aluno(a) {nomes[1]} teve a maior nota?', notas[1] > notas[0], notas[1] > notas[2], notas[1] > notas[3])
print(f'O aluno(a) {nomes[2]} teve a maior nota?', notas[2] > notas[0], notas[2] > notas[1], notas[2] > notas[3])
print(f'O aluno(a) {nomes[3]} teve a maior nota?', notas[3] > notas[2], notas[3] > notas[1], notas[3] > notas[0])

media_ana = sum(notas[0]) / 3
media_fernanda = sum(notas[1]) / 3
media_caio = sum(notas[2]) / 3
media_fernando = sum(notas[3]) / 3

media_geral = (media_ana + media_fernanda + media_caio + media_fernando) / 4
print(f'média geral da turma é {media_geral}')