conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}' .format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}' .format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica entre 1 e 2: {}' .format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}' .format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}' .format(conjunto_superset))

lista = ['cachorro', 'gato', 'elefante', 'gato', 'cachorro']
print(lista)
conjunto_animais = set(lista)
print('A converção da "lista" em conjunto: {}. '
      '\nForam removidos os elementos duplicados.'.format(conjunto_animais))
lista_animais = list(conjunto_animais)
# lista_animais.append('GIRAFA')
print('O "conjunto de animais" foi convertido para "lista de animais": {}' .format(lista_animais))

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(4)
# print(type(conjunto))
# print(conjunto)