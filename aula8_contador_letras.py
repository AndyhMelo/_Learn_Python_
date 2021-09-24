def contador_letras (lista_letras):
    contador = []
    for x in lista_letras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
def teste():
    print('Hello world!!')

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'pato', 'ganso', 'vaca', 'boi']
    print(contador_letras(lista))