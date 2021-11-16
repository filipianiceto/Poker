from Cartas import Cartas

class Mao:
  #cria duas cartas da mao do jogador, verificando se não é a mesma
  def __init__(self):
    self.c1 = Cartas().get_carta()
    self.c2 = Cartas().get_carta()
    while (self.c1 == self.c2):
      self.c2 = Cartas().get_carta()