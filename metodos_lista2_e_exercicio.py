#cria lista
l = [1,2,3]
#acrescentar
l.append('append me!')
#mostrar
print(l)
#retira um item do índice permanentemente
l.pop(0)
print(l)
#atribui o elemento retirado, lembre-se que o índice padrão é -1
popped_item = l.pop()
print(popped_item)
#mostra lista restante
print(l)
#criar lista
new_list = ['a','e','x','b','c']
print(new_list)
#use o reverse() para reverter a ordem (isto é permanente!!)
new_list.reverse()
print(new_list)
#use o sort() para classificar a lista (neste caso, em ordem alfabética)
new_list.sort()
print(new_list)
#LISTAS ANINHADAS
#Começamos com 3 listas
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]
#Faça uma lista de listas para formar uma matriz
matrix = [lst_1, lst_2, lst_3]
print(matrix)
#Pega o primeiro item no objeto da matriz
print(matrix[0])#Obs: sempre retirar o print, pois somente usado para conferir os valores
#Pega o primeiro item do primeiro item no objeto da matriz
print(matrix[0][0])
########################################################
#EXERCÍCIO
#2.Ordene a lista:
l = [5,3,4,6,1]
l.sort()
print(l)