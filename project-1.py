# 1ª Parte ---------------------------------------------------------------------------------------
# 1.2.1.1
def eh_labirinto(argumento):
    if type(argumento) is tuple:
        # número de colunas < 3
        if len(argumento) < 3:
            return False
        else:
            numero_linhas = len(argumento[0])

            # verificar se primeira coluna e toda parede
            for i in argumento[0]:
                if i == 0:
                    return False
            # verificar se última coluna tem e toda parede
            for i in argumento[-1]:
                if i == 0:
                    return False

            # verificar se número de linhas de cada coluna > 3
            for i in range(len(argumento)):
                if len(argumento[i]) < 3:
                    return False
            
            # verificar se todas as colunas têm o mesmo número de linhas
            for i in range(1,len(argumento)):
                if len(argumento[i]) != numero_linhas:
                    #print("Eco 3")
                    return False
                numero_linhas = len(argumento[i])

            return True
    else: return False


# 1.2.1.2
def eh_posicao(argumento):
    if type(argumento) is tuple:
        if len(argumento) != 2:
            return False
        else:
            for i in argumento:
                if i < 0:
                    return False
    else: return False
    return True


# 1.2.1.3
def eh_conj_posicoes(argumento):
    if type(argumento) is tuple:
        posicao_comparacao = argumento[0]
        # tuplos têm de ser únicos
        for i in range(1,len(argumento)):
            if argumento[i] == posicao_comparacao:
                return False
            posicao_comparacao = argumento[i]
        # posicoes dentro do labirinto
        for posicao in argumento:
            for numero in posicao:
                if numero <= 0:
                    return False
        return True
    else: return False


# 1.2.1.4
def tamanho_labirinto(labirinto):
    if not eh_labirinto(labirinto):
        raise ValueError("tamanho_labirinto: O labirinto introduzido não e válido.")
    else:
        tamanho_x = len(labirinto)
        tamanho_y = len(labirinto[0])
        return (tamanho_x, tamanho_y,)


# 1.2.1.5
def eh_mapa_valido(labirinto, conjunto_posicoes):
    if not eh_labirinto(labirinto) or not eh_conj_posicoes(conjunto_posicoes):
        raise ValueError("eh_mapa_valido: Algum dos argumentos e invalido.")

    # verificar se posição da unidade está dentro do labirinto
    dimensoes_labirinto = tamanho_labirinto(labirinto)
    for unidade in conjunto_posicoes:
        x_unidade = unidade[0]
        y_unidade = unidade[1]
        if x_unidade > dimensoes_labirinto[0]-1 or y_unidade > dimensoes_labirinto[1] - 1:
            return False

    # verificar se unidades não estão dentro de paredes
    for unidade_numero in range(len(conjunto_posicoes)):
        x = conjunto_posicoes[unidade_numero][0]
        y = conjunto_posicoes[unidade_numero][1]
        if labirinto[x][y] == 1:
            return False
    return True


# 1.2.1.6
def eh_posicao_livre(labirinto, conjunto_posicoes, posicao):
    if not eh_labirinto(labirinto) or not eh_conj_posicoes(conjunto_posicoes) or not eh_posicao(posicao) or not eh_mapa_valido(labirinto, conjunto_posicoes):
        raise ValueError("eh_posicao_livre: Algum dos argumentos e invalido.")
    else:
        x_posicao = posicao[0] 
        y_posicao = posicao[1]
        for unidade in conjunto_posicoes:
            if unidade == posicao or labirinto[x_posicao][y_posicao] == 1:
                return False
        return True


# 1.2.1.7
def get_posicoes_adjacentes(posicao):
    if not eh_posicao(posicao):
        raise ValueError("get_posicoes_adjacentes: Argumento invalido.")
    else:
        x = posicao[0]
        y = posicao[1]
        
        if x == 0 and y == 0:
            return ((1, 0), (0, 1))
        elif x == 0 and y != 0:
            return ((0, y-1), (0, y+1), (1, y))
        elif x!= 0 and y == 0:
            return ((x-1, y), (x+1, y), (x, 1))
        elif y == 1 and x != 0:
            return ((x-1, y), (x+1, y), (x, y+1))
        else:
            return ((x, y+1), (x, y-1), (x-1, y), (x+1, y))
        

# 1.2.1.8
def get_mapa_str(labirinto, conjunto_posicoes):
    if not eh_labirinto(labirinto) or not eh_conj_posicoes(conjunto_posicoes):
        raise ValueError("get_mapa_str: Algum dos argumentos e invalido.")
    else:
        lenx = len(labirinto)
        leny = len(labirinto[0])
        posicao_numero = 0
        resultado = ""

    for i in range(leny):
        if i != 0:
            resultado += "\n"
        for j in range(lenx):
            if (j,i) in conjunto_posicoes:
                resultado += "O"
            elif labirinto[j][i] == 1:
                resultado += "#"
            elif labirinto[j][i] == 0:
                resultado += "."

    return resultado


# 1.2.2.1
def get_objetivos(labirinto, conjunto_unidades, unidade_inicio):
    if not eh_mapa_valido(labirinto, conjunto_unidades):
        raise ValueError("get_objetivos: Algum dos argumentos e invalido.")
    else:
        resultado = ()
        for unidade in conjunto_unidades:
            if unidade != unidade_inicio:
                for posicao in get_posicoes_adjacentes(unidade):
                    # nota: para não obter repetidos podia ter feito list(set(...))
                    if posicao[0] == len(labirinto) - 1 or posicao[1] == len(labirinto[0]) - 1:
                        continue
                    else: resultado += (posicao,)
    return resultado


# 1.2.2.2
def get_caminho(labirinto, conjunto_unidades, unidade):
    if not eh_mapa_valido(labirinto, conjunto_unidades) or unidade not in conjunto_unidades:
        raise ValueError("get_caminho: Algum dos argumentos e invalido.")
    else:
        objetivos = get_objetivos(labirinto, conjunto_unidades, unidade)
        posicao_atual = unidade
        caminho_atual = ()
        lista_exploracao = ((posicao_atual,caminho_atual),)
        #print(f"print0: lista_exploracao: {lista_exploracao}")
        visitadas = ()
        resultado = ()

        while lista_exploracao != ():
        #while i != len(lista_exploracao) - 1:
            #print(f"eco: while")
            posicao_atual = lista_exploracao[0][0]
            caminho_atual = lista_exploracao[0][1]
            if posicao_atual not in visitadas: 
                visitadas += (posicao_atual,)
                #print(f"print1: visitadas: {visitadas}")
                caminho_atual += (posicao_atual,) 
                #print(f"print2: caminho_atual: {caminho_atual}")
                if posicao_atual in objetivos: 
                    resultado = caminho_atual  
                    #print(f"print3: resultado: {resultado}")
                    return resultado           
                else:         
                    posicoes_adjacentes = get_posicoes_adjacentes(posicao_atual)                 
                    for posicao_adjacente in posicoes_adjacentes:
                        if eh_posicao_livre(labirinto, conjunto_unidades, posicao_adjacente):
                            lista_exploracao += ((posicao_adjacente,caminho_atual),)
            lista_exploracao = lista_exploracao[1:]               
        return ()


# 1.2.2.3
def mover_unidade(labirinto, conjunto_unidades, unidade):
    if not eh_mapa_valido(labirinto, conjunto_unidades) or unidade not in conjunto_unidades:
        raise ValueError("mover_unidade: Algum dos argumentos e invalido.")
    else:
        resultado = ()
        caminho_objetivo = get_caminho(labirinto,conjunto_unidades, unidade)
        
        if len(caminho_objetivo) == 1:
            return conjunto_unidades

        nova_unidade = caminho_objetivo[1]

        for i in range(len(conjunto_unidades)):
            if i == 0:
                resultado += (nova_unidade,)
            else:
                resultado += (conjunto_unidades[i],)
    return resultado


# 2.1.1
labirinto1 = ((1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), 
              (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1))
labirinto2 = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1))
labirinto3 = ((0,0,0,0),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
#print(is_labirinto(labirinto1))
#print(is_labirinto(labirinto2))
#print(is_labirinto(labirinto3))

# 2.1.2
posicao1 = (1,2)
posicao2 = (-1,2)
posicao3 = (1,1,2)    
#print(is_posicao(posicao1))
#print(is_posicao(posicao2))
#print(is_posicao(posicao3))

# 2.1.3
conjunto_posicoes1 = ((1,1),(2,2))
conjunto_posicoes2 = ((1,1),(-5,5))
conjunto_posicoes3 = (((1,1),(2,2),(2,2)))
#print(is_conjunto_posicoes(conjunto_posicoes1))
#print(is_conjunto_posicoes(conjunto_posicoes2))
#print(is_conjunto_posicoes(conjunto_posicoes3))

# 2.1.4
labirinto4 = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
labirinto5 = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1))
#print(get_tamanho_labirinto(labirinto4))
#print(get_tamanho_labirinto(labirinto5))

# 2.1.5
labirinto6 = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
#print(is_mapa_valido(labirinto6, ((1,1), (2,2))))
#print(is_mapa_valido(labirinto6, ((1,1),(5,5))))
#print(is_mapa_valido(labirinto6, ((1,1),(-5,5))))

# 2.1.6
labirinto7 = maze = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades1 = ((2,1),(4,3))
unidades2 = ((2,0), (4,3))
#print(is_posicao_livre(labirinto7, unidades1, (2,2)))
#print(is_posicao_livre(labirinto7, unidades1, (2,0)))
#print(is_posicao_livre(labirinto7, unidades1, (4,3))) # DEVIA DAR FALSE
#print(is_posicao_livre(labirinto7, unidades1, (2,-1)))
#print(is_posicao_livre(labirinto7, unidades2, (2,2)))

# 2.1.7
#print(get_posicoes_adjacentes((2,1)))
#print(get_posicoes_adjacentes((3,2)))
#print(get_posicoes_adjacentes((0,0)))
#print(get_posicoes_adjacentes((-1,2)))

# 2.1.8
labirinto8 = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),
            (1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades3 = ((2,1),(4,3))
unidades4 = ((2, 0), (4, 3))
#print(get_mapa_str(labirinto8, unidades3))
#print(get_mapa_str(labirinto8,3))
#print(get_mapa_str(labirinto8,unidades4))

# 2.2.1
labirinto9 = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),
            (1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades5 = ((2,1),(4,3))
#print(get_objetivos(labirinto9, unidades5, (2,1)))
#print(get_objetivos(labirinto9, unidades5[:1], (2,1)))

# 2.2.2
labirinto10 = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),
            (1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades6 = ((2,1),(4,3))
unidades7 = ((2,1),(5,2),(4,3))
#print(get_caminho(labirinto10,unidades6, (2,1)))
#print(get_caminho(labirinto10, unidades6[:1], (2,1)))
#print(get_caminho(maze, unidades7, (2,1)))
#print(get_caminho(labirinto10, unidades7, (2,2)))

# 2.2.3
unidades8 = ((2,1),(4,3))
print(get_mapa_str(labirinto10, unidades8))
unidades8 = mover_unidade(labirinto10, unidades8, unidades8[0])
print(get_mapa_str(labirinto10, unidades8))
unidades8 = mover_unidade(labirinto10, unidades8, unidades8[0])
print(get_mapa_str(labirinto10, unidades8))
unidades8 = mover_unidade(labirinto10, unidades8, unidades8[0])
print(get_mapa_str(labirinto10, unidades8))
