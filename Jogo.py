class Jogo:
  
  def par(self,c1,c2,m1,m2,m3,m4,m5): #recebe como parâmetro as cartas do jogo
    cont = 0
    par = []
    #verificação de quantas vezes um valor se repete no baralho, e armazenando na lista par
    if (c1[0] == c2[0]):
      cont+=1
      par.append(c1[0])
    if (c1[0] == m1[0]):
      cont+=1
      par.append(c1[0])
    if (c1[0] == m2[0]):
      cont+=1
      par.append(c1[0])
    if (c1[0] == m3[0]):
      cont+=1
      par.append(c1[0])
    if (c1[0] == m4[0]):
      cont+=1
      par.append(c1[0])
    if (c1[0] == m5[0]):
      cont+=1
      par.append(c1[0])
    if (c2[0] == m1[0]):
      cont+=1
      par.append(c2[0])
    if (c2[0] == m2[0]):
      cont+=1
      par.append(c2[0])
    if (c2[0] == m3[0]):
      cont+=1
      par.append(c2[0])
    if (c2[0] == m4[0]):
      cont+=1
      par.append(c2[0])
    if (c2[0] == m5[0]):
      cont+=1
      par.append(c2[0])
    if (m1[0] == m2[0]):
      cont+=1
      par.append(m1[0])
    if (m1[0] == m3[0]):
      cont+=1
      par.append(m1[0])
    if (m1[0] == m4[0]):
      cont+=1
      par.append(m1[0])
    if (m1[0] == m5[0]):
      cont+=1
      par.append(m1[0])
    if (m2[0] == m3[0]):
      cont+=1
      par.append(m2[0])
    if (m2[0] == m4[0]):
      cont+=1
      par.append(m2[0])
    if (m2[0] == m5[0]):
      cont+=1
      par.append(m2[0])
    if (m3[0] == m4[0]):
      cont+=1
      par.append(m3[0])
    if (m3[0] == m5[0]):
      cont+=1
      par.append(m3[0])
    if (m4[0] == m5[0]):
      cont+=1
      par.append(m4[0])
    
    par.sort() #deixa em ordem (alfabética)
    par.reverse() #inverte esta ordem, par o maior valor ficar na frente

    #faz a troca dos valores das cartas-palhaço
    for x in range(0, len(par)): 
      if par[x] == 1:
        del par[x]
        par.insert(x,"A") 
      if par[x] == 11:
        del par[x]
        par.insert(x,"J") 
      if par[x] == 12:
        del par[x]
        par.insert(x,"Q") 
      if par[x] == 13:
        del par[x]
        par.insert(x,"K") 

    #verificando todas as condições, baseadas na variável cont e quantas vezes ela "conta" as repetições
    if (cont == 0): 
      print("Você não tem nenhum par :(")
      return
    if (cont == 1): #par simples
      print("Você tem UM par de",par[0],":)")
      return
    
    #EXISTE UM ERRO AQUI, QUANDO TEM TRES PARES NO JOGO
    if (cont == 2 or cont==3): 
      if (len(par) == 2): #dois pares
        print("Você tem DOIS pares de",par[0],"e",par[1],":D")
        return
      if (par[0] == par[1] == par[2]): #uma trinca
        print("Você tem um trio de",par[-1],"\O/")
        return
      #entra neste if quando temos três pares distintos, nesse caso retorna os dois maiores
      elif ((par[0] == par[1] != par[2]) or (par[1] == par[2] != par[0]) or (par[0] == par[2] != par[1])):
        print("Você tem DOIS pares de",par[0],"e",par[1],":D")
        return 0

    if (cont == 4): #um full house
      print("Você tem um FULL HOUSE com",par[0],"e",par[-1],"\O/\O/")
      return 0

    if (cont == 6): #uma quadra
      print("Você tem uma QUADRA de",par[0],"!!!!!")
      return 0

  
  def s_flush(self,c1,c2,m1,m2,m3,m4,m5):
    # VERIFICAÇÃO SE EXISTE UMA SEQUÊNCIA
    # A parte mais complicada das se quências é que pode haver erros nela, por isso 
    # tantas verificações. Por exemplo, pode existir uma sequência de 2,3,4 e depois de 9,
    # 10. O primeiro for iria considerar uma sequência. O segundo já dá uma filtrada nisso,
    # verificando se existe uma ordem correta nesses valores recebidos. E por último, 
    # envolve um certo cálculo matemático para a verificação final nos ifs, que 
    # envolveu muitas tentativas e entendimento desse sistema ~Filipi
    
    np = [c1[1],c2[1],m1[1],m2[1],m3[1],m4[1],m5[1]] #np recebe os naipes das cartas
    nm1 = [c1[0],c2[0],m1[0],m2[0],m3[0],m4[0],m5[0]] #nm recebe os numeros das cartas

    #verificação se existe um flush de qualquer naipe
    if (np.count('ouros') >= 5):
      print("VOCÊ TEM UM FLUSH DE OUROS !!!")
    elif (np.count('espadas') >= 5):
      print("VOCÊ TEM UM FLUSH DE ESPADAS !!!")
    elif (np.count('copas') >= 5):
      print("VOCÊ TEM UM FLUSH DE COPAS !!!")
    elif (np.count('paus') >= 5):
      print("VOCÊ TEM UM FLUSH DE PAUS !!!")
    else:
      print("Você não tem um flush :(")
    
    print("")

    #nm recebe todas as cartas
    nm = [(c1[0],c1[1]),(c2[0],c2[1]),(m1[0],m1[1]),(m2[0],m2[1]),(m3[0],m3[1]),(m4[0],m4[1]),(m5[0],m5[1])]
    cont=[]
    n = 0
    i = []
    #ordenando as listas
    nm.sort()
    print(nm)
    #for para verificar se existe uma seqência
    for x in range(0, len(nm)):
      try:
        if nm[x][0] == (nm[x+1][0] - 1):
          cont.append(x)
          i.append(nm[x])
          ''' 
        if x == 2 and len(cont) == 0:
          if(a>0):
            continue
          else:
            break '''
      except IndexError:
        break

    #for para verificar se esta sequência é VÁLIDA
    for x in range(0, len(cont)):
      try:
        if cont[x] == (cont[x+1]-1):
          n+=1
      except IndexError:
        break

    # última etapa de verificação. Esta parte de seqências é complicada mesmo,
    # recomenda-se inserir prints das váriáveis n e cont dentro dos fors para
    # melhor entendimento
    i.reverse()
    print("A - ",i)
    print("B- ", len(cont))
    print("C - ", n)
    print("D -",cont)
    print("E - ",len(cont))
    print("F - ",n)

    #verificando se existe uma sequência de flush, e se esta sequência é um royal straight flush
    rf = []
    rfv = 0

    #Estava tendo dificuldades para verificar a existência de uma sequência com Ás (10,J,Q,K,A), então fiz este for para ferificar separadamente se ela existe
    for x in range(0, len(nm)):
      if nm[x][0] == 1:
        rf.append(nm[x])
      elif nm[x][0] == 10:
        rf.append(nm[x])
      elif nm[x][0] == 11:
        rf.append(nm[x])
      elif nm[x][0] == 12:
        rf.append(nm[x])
      elif nm[x][0] == 13:
        rf.append(nm[x])

    #Verificação se existe um royal straight flush
    if (len(rf)>=5):
      for x in range(0, len(rf)):
        try:
          if rf[x][1] == rf[x+1][1]:
            rfv+=1
        except IndexError:
          break

    if rfv >=3: 
      print("VOCÊ TEM UM ROYAL STRAIGHT FLUSH !!!!")
      return
    elif (len(rf)>=5):
      print("Você tem uma sequência! Carta mais alta: A")
      return
        
        
    i.reverse()
    
    if (len(cont) < 4):
      print("Você não tem uma sequência :(")
    elif (n == len(cont)- 1 or (len(cont) == 5 and cont[-1] ==5)): 
      if (len(i) == 4):
        i.insert(0,nm[cont[-1]+1])
        if (i[0][1] == i[1][1] == i[2][1] == i[3][1] == i[4][1]):
          print("VOCÊ TEM UMA SEQUÊNCIA DE FLUSH !!!!")
          print(i)
        else:
          print("VOCÊ TEM UMA SEQUÊNCIA !!!")
      else: 
        if (i[0][1] == i[1][1] == i[2][1] == i[3][1] == i[4][1]):
          print("VOCÊ TEM UMA SEQUÊNCIA DE FLUSH !!!!")
        else:
          print("VOCÊ TEM UMA SEQUÊNCIA !!!")
    else:
      print("Você não tem uma sequência :(")