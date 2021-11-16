import random

class Cartas:
  # criam as cartas do jogo, sendo uma matriz com numero e naipe
  # 1=A, 11=J, 12=Q, 13=K
  numero = [1,2,3,4,5,6,7,8,9,10,11,12,13]
  naipe = ['espadas','copas','paus','ouros']

  def get_carta(self):
    num = random.choice(self.numero)
    nap = random.choice(self.naipe)
    carta = [num,nap]
    return carta