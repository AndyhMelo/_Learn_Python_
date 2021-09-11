# Cria um dicionário com {} e : que significa uma chave e um valor
my_dict = {'key1':'value1','key2':'value2'}
# Chamando valores pela chave
print(my_dict['key2']) #Novamente print apenas para imprimir o valor no console.
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
# Vamos chamar itens do dicionário
print(my_dict['key3'])
# Podemos chamar itens de uma lista
print(my_dict['key3'][0])
# Podemos chamar métodos nos itens também
print(my_dict['key3'][0].upper())
# Podemos também alterar valores através da chave.
print(my_dict['key1'])
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])
# Uma nota rápida: o Python possui um método interno de fazer subtração ou adição automática (ou
# multiplicação ou divisão). Poderíamos ter usado += ou -= para atribuição. Por exemplo:
# Define o objeto como sendo ele mesmo menos 123
my_dict['key1'] -= 123
print(my_dict['key1'])
# Também podemos criar chaves por atribuição. Por exemplo, se começássemos com um dicionário vazio,
# poderíamos adicionar-lhe continuamente:
# Cria um novo dicionário
d = {}
# Cria uma chave por associação
d['animal'] = 'dog'
# Pode fazer isso com qualquer objeto
d['answer'] = 42
print(d)
# ANINHAMENTO DE DICIONÁRIOS
d = {'key1':{'nestkey':{'subnestkey': 'value'}}}
# Continue chamando as chaves...
print(d['key1']['nestkey']['subnestkey'])
# Alguns métodos de dicionários:
# Existem alguns métodos que podemos chamar em um dicionário. Vamos começar uma breve introdução
# a alguns deles:
# Cria um dicionário típico
d = {'key1':1,'key2':2,'key3':3}
# Retorna uma lista de todas as chaves
print(d.keys())
# Pega todos os valores
print(d.values())
# Método para retornar todas as tuplas de todos os itens
print(d.items())
#EXERCÍCIOS
#1. Usando chaves e indexação, pegue o "hello" dos seguintes dicionários:
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
# d = {'k1':[{'nestkey':['this is deep',['hello']]}]}
# print(d['k1'][0]['nestkey'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2['hello']]}]}]}
