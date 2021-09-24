from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste

calculadora = Calculadora(20, 6)
televisao = Televisao()
televisao.power()
print(calculadora.divisao())
print(televisao.ligada)
lista = ['anderson', 'patrick', 'vinicius']
print(lista)
total_letras = contador_letras(lista)
print('Total de letras por palavra na lista: {}\nFim do programa!!' .format(contador_letras(lista)))
print(teste())