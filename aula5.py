lista = [1, 3, 15, 5, 7, 4]
lista_animal = ['cachorro', 'gato', 'elefante', 'zebra', 'arara']

lista_animal [0] = str(input('Entre com o animal a ser incluído na posição 1: '))
lista_animal.append(str(input('Entre com o animal a ser incluído: ')))
print(lista_animal)

tupla = (1,10,23,4,2)
print(tupla)
print(len(tupla))
print(len(lista_animal))
lista_animal.sort()
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
lista_numerica [0] = 99
print(type(lista_numerica))
print(lista_numerica)

# print(lista_animal[2])
# nova_lista = lista_animal * 3
# print(nova_lista)

# lista_animal.append(str(input('Entre com o animal a ser incluído: ')))
# lista_animal.remove(str(input('Entre com o animal a ser retirado: ')))
# lista_animal.sort()
# print(lista_animal)
# lista.sort()
# print(lista)
# lista_animal.reverse()
# print(lista_animal)

# if 'onça' in lista_animal:
#     print('Existe onça na lista!!')
# else:
#     print('Não existe uma onça na lista, será adicionado!!')
#     lista_animal.append('onça')
#     print(lista_animal)

# lista_animal.pop(1)
# print('Já existe um felino, portanto, gato será retirado!!')
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)