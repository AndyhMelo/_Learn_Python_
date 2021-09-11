a = int(input('Entre com o primeiro valor: '))#necessário declarar o tipo de variável que vai receber na entrada
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multipicacao = a * b
divisao =  a / b
resto = a % b
# print('soma: {}' .format(soma)) #Jeito correto, converte para string qual seja o tipo (int, float, etc)
# print('soma: ' + str(soma)) # Jeito "não correto"
# print('multipicacao: {}' .format(multipicacao))
# print('subtracao: {}' .format(subtracao))
# print('divisao: {}' .format(divisao))
# print('resto: {}' .format(resto))
# x = 1
# soma2 = int(x) + 1
# print('X: {}' .format(soma2))
#Ou fazer igual próximo exemplo
resultado = ('Soma: {soma} \nSubtração: {sub} \nMultiplicação: {mult} \nDivisão: {div} \nResto: {resto}'
      .format(soma=soma, sub=subtracao, mult=multipicacao, div=divisao, resto=resto))#\n pula linha (ENTER)
print(resultado)
print(type(resultado))