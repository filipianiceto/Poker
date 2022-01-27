from Cartas import Cartas

class Mesa:
  #criam as cartas da mesa, cerificando se nenhuma se repete
  def __init__(self,c1,c2): #recebe como parametro as cartas da mao, e verifica se elas repetem também
    self.m1 = Cartas().get_carta()
    while (self.m1 == (c1) or self.m1 == (c2)):
      self.m1 = Cartas().get_carta()
    self.m2 = Cartas().get_carta()
    while (self.m2 == (self.m1) or self.m2 ==(c1) or self.m2 ==(c2)):
      self.m2 = Cartas().get_carta()
    self.m3 = Cartas().get_carta()
    while (self.m3 == (self.m2) or self.m3==(self.m1) or self.m3==(c1) or self.m3==(c2)):
      self.m3 = Cartas().get_carta()
    self.m4 = Cartas().get_carta()
    while (self.m4==(self.m3) or self.m4==(self.m2) or self.m4==(self.m1) or self.m4==(c1) or self.m4==(c2)):
      self.m4 = Cartas().get_carta()
    self.m5 = Cartas().get_carta()
    while (self.m5==(self.m4) or self.m5==(self.m3) or self.m5==(self.m2) or self.m5==(self.m1) or self.m5==(c1) or self.m5==(c2)):
      self.m5 = Cartas().get_carta()