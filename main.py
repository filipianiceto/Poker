from Mesa import Mesa
from Jogo import Jogo
from Mao import Mao

mao = Mao()
mesa = Mesa(mao.c1,mao.c2)
jogo = Jogo()
''''
print(mao.c1)
print(mao.c2)
print("------------")
print(mesa.m1)
print(mesa.m2)
print(mesa.m3)
print(mesa.m4)
print(mesa.m5)
print("-------------")
jogo.par(mao.c1,mao.c2,mesa.m1,mesa.m2,mesa.m3,mesa.m4,mesa.m5)
print("")
'''
jogo.s_flush([6,'copas'],[11,'espadas'],[10,'espadas'],[11,'copas'],[12,'copas'],[13,'copas'],[1,'copas'])