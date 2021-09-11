a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado!! Digite primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado!! Digite segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado!! Digite terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado!! Digite quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}' .format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi digitada alguma nota errada!!')


# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# restoa = a % 2
# restob = b % 2
# if restoa == 0 or not restob > 0:
#     print('Foi digitado um número par!!')
# else:
#     print('Foi digitado um número ímpar!!')
# print('Final do programa!!')
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print ('O maior valor é: {}' .format(a))
# elif b > a and b > c:
#     print('O maior valor é: {}' .format(b))
# else:
#     print('O maior valor é : {}' .format(c))
# print('Final do programa!!')