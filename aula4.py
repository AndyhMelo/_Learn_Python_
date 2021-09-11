print('Calculadora de médias versão beta 2.1\n')
a = int(input('Entre com a nota 1º bim: '))
while a > 10:
    a = int(input('Nota {} inválida, notas válidas de 0 a 10!!\nEntre com a nota 1º bim: '.format(a)))
b = int(input('Entre com a nota 2º bim: '))
while b > 10:
    b = int(input('Nota {} inválida, notas válidas de 0 a 10!!\nEntre com a nota 2º bim: '.format(b)))
c = int(input('Entre com a nota 3º bim: '))
while c > 10:
    c = int(input('Nota {} inválida, notas válidas de 0 a 10!!\nEntre com a nota 3º bim: '.format(c)))
d = int(input('Entre com a nota 4º bim: '))
while d > 10:
    d = int(input('Nota {} inválida, notas válidas de 0 a 10!!\nEntre com a nota 4º bim: '.format(d)))
media = (a + b + c + d) / 4
print('Média: {}' .format(media))

# print('Calculadora de médias versão beta 2.1\n')
# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota {} inválida, notas válidas de 0 a 10!!\nEntre com a nota: '.format(nota)))


# a = 0
# while a < 10:
#     a += 1
#     print(a)


# a = int(input('Entre com um número: '))
# for num in range (a + 1):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Entre com um número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('Número {} é primo!!' .format(a))
# else:
#     print('Número {} não é primo!!'.format(a))