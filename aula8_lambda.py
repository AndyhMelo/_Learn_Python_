contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cavalo', 'gato', 'peixe']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
divisao = lambda a, b: a / b
multiplicacao = lambda a, b: a * b

print(soma(5,8))
print(subtracao(4, 1))
print(divisao(60, 4))
print(multiplicacao(56, 4))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'divisao': lambda a, b: a / b,
    'multiplicacao': lambda a, b: a * b
}
print(type(calculadora))
soma = calculadora['soma']
# soma = lambda a, b: a + b
subtracao = calculadora['subtracao']
divisao = calculadora['divisao']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(1, 4)))
print('A multiplicação é: {}'.format(multiplicacao(3, 7)))
print(type(soma))
