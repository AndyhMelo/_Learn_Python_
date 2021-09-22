class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def canal_up(self):
         if self.ligada:
            self.canal += 1
    def canal_down(self):
        if self.ligada:
            self.canal -= 1

televisao = Televisao()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.canal_up()
print('Canal: {}'.format(televisao.canal))
televisao.canal_up()
print('Canal: {}'.format(televisao.canal))
televisao.canal_up()
print('Canal: {}'.format(televisao.canal))
televisao.canal_down()
print('Canal: {}'.format(televisao.canal))
televisao.canal_down()
print('Canal: {}'.format(televisao.canal))
televisao.canal_down()
print('Canal: {}'.format(televisao.canal))
