# --- Funcoes auxiliares ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_adjacente_1(posicao):
    return (obter_pos_x(posicao), obter_pos_y(posicao)-1)

def get_adjacente_2(posicao):
    return (obter_pos_x(posicao)-1, obter_pos_y(posicao))

def get_adjacente_3(posicao):
    return (obter_pos_x(posicao)+1, obter_pos_y(posicao))

def get_adjacente_4(posicao):
    return (obter_pos_x(posicao), obter_pos_y(posicao)+1)

def is_inteiro_nao_negativo(n):
    if type(n) is int and n>-1:
        return True
    else: return False

def is_inteiro_positivo(n):
    if type(n) is int and n>0:
        return True
    else: return False

def cria_labirinto(dimensoes, walls, unidades1, unidades2):
    n_colunas = dimensoes[0]
    n_linhas = dimensoes[1]
    labirinto = []

    for y in range(n_linhas):
        labirinto += [[1]]
        for x in range(1,n_colunas):
            if y == 0 or y == n_linhas-1 or (x,y) in walls: 
                labirinto[y] += [1]
            else:
                if x == 0 or x == n_colunas-1:
                    labirinto[y] += [1]
                else:  
                    labirinto[y] += [0]
    return labirinto

def walls_dentro_das_dimensoes(d, walls):
    dx = d[0]
    dy = d[1]
    for posicao in walls:
        if not(posicao[0] > 0 and posicao[0] < dx-1 and posicao[1] > 0 and posicao[1] < dy - 1):
            return False
    return True

def ordenar_ordem_leitura(tuplos):
    """Retorna um tuplo de tuplos."""
    length = len(tuplos)
    tuplos_aux = transforma_tuplos_em_listas(tuplos)

    while not are_ordenados(tuplos_aux):
        for i in range(length-1):
            x_anterior = tuplos_aux[i][0]
            y_anterior = tuplos_aux[i][1]
            x_seguinte = tuplos_aux[i+1][0]
            y_seguinte = tuplos_aux[i+1][1]

            if y_anterior > y_seguinte:
                aux = tuplos_aux[i+1]
                tuplos_aux[i+1] = tuplos_aux[i]
                tuplos_aux[i] = aux
            elif y_anterior == y_seguinte:
                if x_anterior > x_seguinte:
                    aux = tuplos[i+1]
                    tuplos_aux[i+1] = tuplos_aux[i]
                    tuplos_aux[i] = aux
    return transforma_listas_em_tuplos(tuplos_aux)

def obter_indice_unidade(tuplos, tuplo):
    length = len(tuplos)
    for i in range(length):
        if tuplos[i] == tuplo:
            return i
    raise(ValueError("obter_indice_unidade: tuplo not in tuplos"))

def converte_tuplo(posicao):
    return (obter_pos_x(posicao), obter_pos_y(posicao))

def transforma_unidades_em_posicoes(unidades):
    resultado = ()
    for unidade in unidades:
        resultado += (obter_posicao(unidade),)
    return resultado

def obter_extremos(dimensoes):
    Dx = dimensoes[0]
    Dy = dimensoes[1]
    extremos = ()
    for y in range(Dy):
        for x in range(Dx):
            if x == 0 or y == 0 or x == Dx-1 or y == Dy-1:
                extremos += ((x,y),)
    return extremos

def transforma_tuplos_em_listas(tuplos):
    lista_resultado = []
    for tuplo in tuplos:
        lista_resultado += [list(tuplo)]
    return lista_resultado

def transforma_listas_em_tuplos(listas):
    tuplo_resultado = []
    for lista in listas:
        tuplo_resultado += [tuple(lista)]
    return tuple(tuplo_resultado)

def are_ordenados(tuplos):
    length = len(tuplos)
    tuplos_aux = transforma_tuplos_em_listas(tuplos)

    for i in range(length-1):
        x_anterior = tuplos_aux[i][0]
        y_anterior = tuplos_aux[i][1]
        x_seguinte = tuplos_aux[i+1][0]
        y_seguinte = tuplos_aux[i+1][1]
        if y_anterior > y_seguinte:
            return False
        elif y_anterior == y_seguinte:
            if x_anterior > x_seguinte:
                return False
    return True

def get_posicoes_adjacentes(posicao):
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

def obter_nome_exercito1(mapa):
    return obter_exercito(obter_unidades1(mapa)[0])

def obter_nome_exercito2(mapa):
    return obter_exercito(obter_unidades2(mapa)[0])

def get_inimigo_cima(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 

    if y == 0:
        return 0
    else:
        posicao = (x,y-1)
        if obter_unidade(mapa, posicao) != False and obter_exercito(obter_unidade(mapa, posicao)) != exercito:
            return obter_unidade(mapa, posicao)
        else: return 0

def get_inimigo_esquerda(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 

    if x == 0:
        return 0
    else:
        posicao = (x-1,y)
        if obter_unidade(mapa, posicao) != False and obter_exercito(obter_unidade(mapa, posicao)) != exercito:
            return obter_unidade(mapa, posicao)
        else: return 0

def get_inimigo_direita(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 
    Dx = obter_tamanho_mapa(mapa)[0]
    Dy = obter_tamanho_mapa(mapa)[1]

    if x == Dx-2: # ver se não dá problemas (em vez de -1)
        return 0
    else:
        posicao = (x+1,y)
        if obter_unidade(mapa, posicao) != False and obter_exercito(obter_unidade(mapa, posicao)) != exercito:
            return obter_unidade(mapa, posicao)
        else: return 0

def get_inimigo_baixo(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 
    Dx = obter_tamanho_mapa(mapa)[0]
    Dy = obter_tamanho_mapa(mapa)[1]

    if y == Dy-2: # ver se não dá problemas (em vez de -1)
        return 0
    else:
        posicao = (x,y+1)
        if obter_unidade(mapa, posicao) != False and obter_exercito(obter_unidade(mapa, posicao)) != exercito:
            return obter_unidade(mapa, posicao)
        else: return 0

def encontra_indice(unidades, unidade):
    for i in range(len(unidades)):
        if obter_posicao(unidades[i]) == obter_posicao(unidade):
            return i
    else: raise(ValueError("encontra_unidades: a unidade nao existe neste conjunto de unidades."))

def ordena_muitas_unidades(lista_de_unidades):
    n = len(lista_de_unidades)
    for j in range(len(lista_de_unidades)-1):
        for i in range(0, n-j-1):
            x = obter_pos_x(obter_posicao(lista_de_unidades[i]))
            y = obter_pos_y(obter_posicao(lista_de_unidades[i]))
            x_seg = obter_pos_x(obter_posicao(lista_de_unidades[i+1]))
            y_seg = obter_pos_y(obter_posicao(lista_de_unidades[i+1]))

            if y > y_seg:
                #aux = lista_de_unidades[i+1]
                #lista_de_unidades[i+1] = lista_de_unidades[i]
                #lista_de_unidades[i] = aux
                lista_de_unidades[i], lista_de_unidades[i+1] = lista_de_unidades[i+1], lista_de_unidades[i]
            elif y == y_seg:
                if x > x_seg:
                    #aux = lista_de_unidades[i+1]
                    #lista_de_unidades[i+1] = lista_de_unidades[i]
                    #lista_de_unidades[i] = aux
                    lista_de_unidades[i], lista_de_unidades[i+1] = lista_de_unidades[i+1], lista_de_unidades[i]
    return lista_de_unidades  
        
def encontra_indice_2(posicao, lista_unidades):
    for i in range(len(lista_unidades)):
        if posicao == obter_posicao(lista_unidades[i]):
            return i
    raise(ValueError("encontra_indice_2: nao existe uma unidade com esta pocicao nesta lista de unidades"))

def obter_posicoes_objetivo(mapa, unidade):
    posicoes_resultado = ()
    unidades1 = obter_unidades1(mapa)
    unidades2 = obter_unidades2(mapa)

    if unidade in unidades1:
        for elemento in unidades2:
            if get_posicao_cima(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_cima(mapa, elemento),)
            if get_posicao_esquerda(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_esquerda(mapa, elemento),)
            if get_posicao_direita(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_direita(mapa, elemento),)
            if get_posicao_baixo(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_baixo(mapa, elemento),)
    if unidade in unidades2:
        for elemento in unidades1:
            if get_posicao_cima(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_cima(mapa, elemento),)
            if get_posicao_esquerda(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_esquerda(mapa, elemento),)
            if get_posicao_direita(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_direita(mapa, elemento),)
            if get_posicao_baixo(mapa, elemento) != 0:
                posicoes_resultado += (get_posicao_baixo(mapa, elemento),)

    return posicoes_resultado

def get_posicao_cima(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 

    if y == 0:
        return 0
    else:
        posicao = (x,y-1)
        if obter_unidade(mapa, posicao) == False and posicao not in obter_walls(mapa):
            return posicao
        else: return 0

def get_posicao_esquerda(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 

    if x == 0:
        return 0
    else:
        posicao = (x-1,y)
        if obter_unidade(mapa, posicao) == False and posicao not in obter_walls(mapa):
            return posicao
        else: return 0

def get_posicao_direita(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 
    Dx = obter_tamanho_mapa(mapa)[0]
    Dy = obter_tamanho_mapa(mapa)[1]

    if x == Dx-2:
        return 0
    else:
        posicao = (x+1,y)
        if obter_unidade(mapa, posicao) == False and posicao not in obter_walls(mapa):
            return posicao
        else: return 0

def get_posicao_baixo(mapa, unidade):
    exercito = obter_exercito(unidade)
    posicao = obter_posicao(unidade)
    x = posicao[0]
    y = posicao[1] 
    Dx = obter_tamanho_mapa(mapa)[0]
    Dy = obter_tamanho_mapa(mapa)[1]

    if y == Dy-2:
        return 0
    else:
        posicao = (x,y+1)
        if obter_unidade(mapa, posicao) == False and posicao not in obter_walls(mapa):
            return posicao
        else: return 0

def transforma_string_em_tuplo_de_tuplos(string):
    length = len(string)
    numero_tuplos = 0
    tuplos_resultado = ()

    for carater in string:
        if carater == "(":
            numero_tuplos += 1

    for i in range(1,length-1):
        if string[i] == "(":
            novo_tuplo = ()
            tuplos_resultado += (novo_tuplo,)
        elif string[i] != "," and string[i] != ")" and string[i] != " " and string[i] != "\n":
            novo_tuplo += (string[i])
    return tuplos_resultado
            



# 2ª Parte ---------------------------------------------------------------------------------------
# 2.1.1 Construtores - Posicao
def cria_posicao(x,y):
    if is_inteiro_nao_negativo(x) and is_inteiro_nao_negativo(y):
        return (x,y)
    else: raise(ValueError("cria_posicao: argumentos invalidos"))

def cria_copia_posicao(posicao):
    if eh_posicao(posicao):
        copia = posicao # Acho que esta certo porque esta a crira uma copia e nao um alias, ja testei
        return copia
    else: raise(ValueError("cria_copia_posicao: argumento invalido"))

# 2.1.2 Seletores - Posicao
def obter_pos_x(posicao):
    return posicao[0]

def obter_pos_y(posicao):
    return posicao[1]

# 2.1.3 Reconhecedores - Posicao
def eh_posicao(universal):
    if type(universal) is tuple:
        return len(universal) == 2 and is_inteiro_nao_negativo(universal[0]) and is_inteiro_nao_negativo(universal[1])
    else: return False

# 2.1.4 Testes - Posicao
def posicoes_iguais(p1, p2):
    return obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2)

# 2.1.5 Transformadores - Posicao
def posicao_para_str(posicao):
    return f"({obter_pos_x(posicao)}, {obter_pos_y(posicao)})"

# 2.1.6 Funcoes de alto nivel - Posicao
def obter_posicoes_adjacentes(posicao):
    if obter_pos_x(posicao) == 0 and obter_pos_y(posicao) != 0: 
        return (get_adjacente_1(posicao), get_adjacente_3(posicao), get_adjacente_4(posicao))
    elif obter_pos_x(posicao) != 0 and obter_pos_y(posicao) == 0:
        return (get_adjacente_2(posicao), get_adjacente_3(posicao), get_adjacente_4(posicao)) 
    elif obter_pos_x(posicao) == 0 and obter_pos_y(posicao) == 0:
        return (get_adjacente_3(posicao), get_adjacente_4(posicao))
    else:
        return (get_adjacente_1(posicao),get_adjacente_2(posicao), get_adjacente_3(posicao), get_adjacente_4(posicao))

# 2.2.1 Construtores - Unidade
def cria_unidade(p, v, f, string):
    if eh_posicao(p) and is_inteiro_positivo(v) and is_inteiro_positivo(f) and type(string) == str:
        return {"posicao" : p, "vida" : v, "forca" : f, "exercito" : string}
    else: raise(ValueError("cria unidade: argumentos invalidos"))

def cria_copia_unidade(unidade):
    if eh_unidade(unidade):
        copia = cria_unidade(obter_posicao(unidade), obter_vida(unidade), obter_forca(unidade), obter_exercito(unidade))
        return copia
    else: raise(ValueError("cria_copia_unidade: argumento invalido"))

# 2.2.2 Seletores - Unidade
def obter_posicao(unidade):
    return unidade["posicao"]

def obter_exercito(unidade):
    return unidade["exercito"]

def obter_forca(unidade):
    return unidade["forca"]

def obter_vida(unidade):
    return unidade["vida"]

# 2.2.3 Modificadores - Unidade
def muda_posicao(unidade, posicao):
    unidade["posicao"] = posicao
    return unidade

def remove_vida(unidade, n):
    unidade["vida"] -= n
    return unidade

# 2.2.4 Reconhecedores - Unidade
def eh_unidade(u):
    if type(u) == dict:
        if len(u) == 4 and "posicao" in u and "vida" in u and "forca" in u and "exercito" in u:
            if eh_posicao(obter_posicao(u)) and is_inteiro_positivo(obter_vida(u)) and is_inteiro_positivo(obter_forca(u)) and type(obter_exercito(u)) == str:
                return True
    return False

# 2.2.5 Testes - Unidade
def unidades_iguais(u1, u2):
    return u1["posicao"] == u2["posicao"] and u1["forca"] == u2["forca"] and u1["vida"] == u2["vida"] and u1["exercito"] == u2["exercito"]

# 2.2.6 Transformadores - Unidade
def unidade_para_char(unidade):
    return obter_exercito(unidade)[0].upper()

def unidade_para_str(unidade):
    return f"{unidade_para_char(unidade)}[{obter_vida(unidade)},{obter_forca(unidade)}]@{obter_posicao(unidade)}"

# 2.2.7. Funcoes de alto nivel - Unidade
def unidade_ataca(u1, u2):
    """ Tira vida a unidade 2 correspondente ao valor de forca da unidade 1."""
    forca = obter_forca(u1)
    #remove_vida(u2, forca)
    u2["vida"] -= forca
    return obter_vida(u2) < 1

def ordenar_unidades(tuplo_unidades):
    x1 = obter_pos_x(obter_posicao(tuplo_unidades[0]))
    y1 = obter_pos_y(obter_posicao(tuplo_unidades[0]))
    x2 = obter_pos_x(obter_posicao(tuplo_unidades[1]))
    y2 = obter_pos_y(obter_posicao(tuplo_unidades[1]))

    if y1 < y2 or (x1 < x2 and y1 <= y2):
        return (tuplo_unidades[0], tuplo_unidades[1])
    else: return (tuplo_unidades[1], tuplo_unidades[0])

# 2.3.1 Construtores - Mapa
def cria_mapa(d, w, e1, e2): # dimensoes, walls, unidades_exercito1, unidades_exercito2
    if is_inteiro_positivo(d[0]) and d[0] > 3 and is_inteiro_positivo(d[1]) and d[1] > 3:
        if walls_dentro_das_dimensoes(d, w):
            for elemento in e1:
                if not eh_unidade(elemento):
                    raise(ValueError("cria_mapa: argumentos invalidos"))
            for elemento in e2:
                if not eh_unidade(elemento):
                    raise(ValueError("cria_mapa: argumentos invalidos"))
            posicoes1 = ()
            posicoes2 = ()
            for unidade in e1:
                posicoes1 += (obter_posicao(unidade),)
            for unidade in e2:
                posicoes2 += (obter_posicao(unidade),)
            labirinto = cria_labirinto(d,w,e1,e2)
            return {"Dx":d[0], "Dy":d[1], "walls":w, "unidades1":e1, "unidades2":e2}
    raise(ValueError("cria_mapa: argumentos invalidos"))

def cria_copia_mapa(mapa):
    if is_inteiro_positivo(mapa["Dx"]) and mapa["Dx"] > 3 and is_inteiro_positivo(mapa["Dy"]) and mapa["Dy"] > 3:
        if walls_dentro_das_dimensoes((mapa["Dx"], mapa["Dy"]), mapa["walls"]):
            for elemento in mapa["unidades1"]:
                if not eh_unidade(elemento):
                    raise(ValueError("cria_mapa: argumentos invalidos"))
            for elemento in mapa["unidades2"]:
                if not eh_unidade(elemento):
                    raise(ValueError("cria_mapa: argumentos invalidos"))
            d = (mapa["Dx"], mapa["Dy"])
            novo_mapa = cria_mapa(d, mapa["w"], mapa["unidades1"], mapa["unidades2"])
            return novo_mapa
    raise(ValueError("cria_copia_mapa: argumentos invalidos"))

# 2.3.2 Seletores - Mapa
def obter_tamanho_mapa(mapa):
    return (mapa["Dx"], mapa["Dy"])

def obter_nome_exercitos(mapa):
    return (obter_exercito(mapa["unidades1"][0]), obter_exercito(mapa["unidades2"][0]))

def obter_unidades_exercito(mapa, string):
    if obter_nome_exercitos(mapa)[0] == string:
        return mapa["unidades1"]
    else: 
        return mapa["unidades2"]

def obter_todas_unidades(mapa):
    resultado = ()
    for elemento in mapa["unidades1"]:
        resultado += (elemento,)
    for elemento in mapa["unidades2"]:
        resultado += (elemento,)
    return ordenar_ordem_leitura(resultado)             

def obter_unidade(mapa, posicao):
    posicao_tuplo = (obter_pos_x(posicao), obter_pos_y(posicao))
    posicoes1 = transforma_unidades_em_posicoes(mapa["unidades1"])
    posicoes2 = transforma_unidades_em_posicoes(mapa["unidades2"])

    if posicao_tuplo in posicoes1:
        indice = obter_indice_unidade(posicoes1, posicao_tuplo)
        return mapa["unidades1"][indice]
    elif posicao_tuplo in posicoes2:
        indice = obter_indice_unidade(posicoes2, posicao_tuplo)
        return mapa["unidades2"][indice]
    else: return False

def obter_walls(mapa): # funcao minha
    return mapa["walls"]

def obter_unidades1(mapa): # funcao minha
    return mapa["unidades1"]

def obter_unidades2(mapa): # funcao minha
    return mapa["unidades2"]

# 2.3.3 Modificadores - Mapa
def eliminar_unidade(mapa, unidade): 
    novas_unidades = ()
    if obter_posicao(unidade) in transforma_unidades_em_posicoes(obter_unidades1(mapa)):
        unidades = obter_unidades1(mapa)
        for elemento in unidades:
            if obter_posicao(elemento) != obter_posicao(unidade):
                p = obter_posicao(elemento)
                v = obter_vida(elemento)
                f = obter_forca(elemento)
                string = obter_exercito(elemento)
                novas_unidades += (cria_unidade(p, v, f, string),)
        mapa["unidades1"] = novas_unidades
    else:
        unidades = obter_unidades2(mapa)
        for elemento in unidades:
            if obter_posicao(elemento) != obter_posicao(unidade):
                p = obter_posicao(elemento)
                v = obter_vida(elemento)
                f = obter_forca(elemento)
                string = obter_exercito(elemento)
                novas_unidades += (cria_unidade(p, v, f, string),)
        mapa["unidades2"] = novas_unidades
    return mapa

def mover_unidade(mapa, unidade, posicao):
    novas_unidades = ()
    if obter_posicao(unidade) in transforma_unidades_em_posicoes(obter_unidades1(mapa)):
        unidades = obter_unidades1(mapa)
        for elemento in unidades:
            v = obter_vida(elemento)
            f = obter_forca(elemento)
            string = obter_exercito(elemento)
            if obter_posicao(elemento) != obter_posicao(unidade):
                p = obter_posicao(elemento)
                novas_unidades += (cria_unidade(p, v, f, string),)
            else: 
                p = posicao
                novas_unidades += (cria_unidade(p, v, f, string),)
        mapa["unidades1"] = novas_unidades
    else:
        unidades = obter_unidades2(mapa)
        for elemento in unidades:
            v = obter_vida(elemento)
            f = obter_forca(elemento)
            string = obter_exercito(elemento)
            if obter_posicao(elemento) != obter_posicao(unidade):
                p = obter_posicao(elemento)
                novas_unidades += (cria_unidade(p, v, f, string),)
            else:
                p = posicao
                novas_unidades += (cria_unidade(p, v, f, string),)
        mapa["unidades2"] = novas_unidades
    return mapa

# 2.3.4. Reconhecedores - Mapa
def eh_posicao_unidade(mapa, posicao):
    p = converte_tuplo(posicao)
    if p in mapa["unidades1"] or p in mapa["unidades2"]:
        return True
    else: return False

def eh_posicao_corredor(mapa, posicao):
    p = converte_tuplo(posicao)
    if p not in mapa["walls"]:
        return True
    else: return False

def eh_posicao_parede(mapa, posicao):
    p = converte_tuplo(posicao)
    if p in mapa["walls"]:
        return True
    else: return False

# 2.3.5. Testes - Mapa
def mapas_iguais(mapa1, mapa2):
    return mapa1["Dx"]==mapa2["Dx"] and mapa1["Dy"]==mapa2["Dy"] and mapa1["walls"]==mapa2["walls"] and mapa1["unidades1"]==mapa2["unidades1"] and mapa1["unidades2"]==mapa2["unidades2"]  

# 2.3.6. Transformadores - Mapa
def mapa_para_str(mapa):
    string_resultado = ""
    walls = obter_walls(mapa)
    unidades1 = obter_unidades1(mapa)
    unidades2 = obter_unidades2(mapa)
    posicoes1 = transforma_unidades_em_posicoes(unidades1)
    posicoes2 = transforma_unidades_em_posicoes(unidades2)
    letras_exercitos = obter_nome_exercitos(mapa)
    letra1 = letras_exercitos[0][0].upper()
    letra2 = letras_exercitos[1][0].upper()
    extremos = obter_extremos(obter_tamanho_mapa(mapa))
    Dx = obter_tamanho_mapa(mapa)[0]
    Dy = obter_tamanho_mapa(mapa)[1]

    for y in range(Dy):
        if y != 0:
            string_resultado += "\n"
        for x in range(Dx):
            if (x,y) in walls or (x,y) in extremos:
                string_resultado += "#"
            elif (x,y) in posicoes1:
                string_resultado += letra1
            elif (x,y) in posicoes2:
                string_resultado += letra2
            else: string_resultado += "."
    return string_resultado
    
# 2.3.7. Funcoes de alto nivel - Mapa
def obter_inimigos_adjacentes(mapa, unidade):
    inimigos_resultado = ()

    if get_inimigo_cima(mapa, unidade) != 0:
        inimigos_resultado += (get_inimigo_cima(mapa, unidade),)
    if get_inimigo_esquerda(mapa, unidade) != 0:
        inimigos_resultado += (get_inimigo_esquerda(mapa, unidade),)
    if get_inimigo_direita(mapa, unidade) != 0:
        inimigos_resultado += (get_inimigo_direita(mapa, unidade),)
    if get_inimigo_baixo(mapa, unidade) != 0:
        inimigos_resultado += (get_inimigo_baixo(mapa, unidade),)

    return inimigos_resultado

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

# --- Funcoes adicionais :

def calcula_pontos(mapa, nome_exercito):
    int_resultado = 0
    if obter_nome_exercito1(mapa) == nome_exercito:
        for unidade in obter_unidades1(mapa):
            int_resultado += obter_vida(unidade)
    else:
        for unidade in obter_unidades2(mapa):
            int_resultado += obter_vida(unidade)
    return int_resultado

# confirmar se unidades1 e unidades2 já estão ordenadas!!!!!!!!!
def simula_turno(mapa):
    unidades1 = obter_unidades1(mapa)
    unidades2 = obter_unidades2(mapa)
    
    todas_as_unidades = list(unidades1) + list(unidades2)
    todas_as_unidades_lista_ordenadas = ordena_muitas_unidades(todas_as_unidades)

    for unidade in todas_as_unidades_lista_ordenadas:
        # mover:
        if obter_posicoes_objetivo(mapa, unidade):
            nova_posicao = obter_movimento(mapa, unidade) # !!!
            if obter_unidade(mapa, nova_posicao) not in obter_unidades_exercito(mapa, obter_exercito(unidade)):
                mover_unidade(mapa, unidade, nova_posicao) 
                unidade = obter_unidade(mapa, nova_posicao)
        # atacar: 
        if obter_inimigos_adjacentes(mapa, unidade):
            inimigos_adjacentes = obter_inimigos_adjacentes(mapa, unidade)
            atacada = inimigos_adjacentes[0]
            if unidade_ataca(unidade, inimigos_adjacentes[0]) == True:
                eliminar_unidade(mapa, inimigos_adjacentes[0])
                indice = encontra_indice_2(obter_posicao(inimigos_adjacentes[0]), todas_as_unidades_lista_ordenadas)
                todas_as_unidades_lista_ordenadas.remove(todas_as_unidades_lista_ordenadas[indice])
    return mapa
    
def simula_batalha(nome, booleano):
    ficheiro = open(nome, "r")
    linhas = ficheiro.read().splitlines()
    dimensoes = linhas[0]
    exercito1, vida1, forca1 = linhas[1][0], linhas[1][1], linhas[1][2]
    exercito2, vida2, forca2 = linhas[2][0], linhas[2][1], linhas[2][2]
    walls = linhas[3]
    pseudo_posicoes1 = linhas[4]
    pseudo_posicoes2 = linhas[5]
    posicoes1 = ()
    posicoes2 = ()
    e1 = ()
    e2 = ()

    for pseudo_posicao in pseudo_posicoes1:
        posicoes1 += (cria_posicao(pseudo_posicao[0], pseudo_posicao[1]),)
    for pseudo_posicao in pseudo_posicoes2:
        posicoes2 += (cria_posicao(pseudo_posicao[0], pseudo_posicao[1]),)

    for posicao in posicoes1:
        e1 += (cria_unidade(posicao, vida1, forca1, exercito1),)
    for posicao in posicoes2:
        e2 += (cria_unidade(posicao, vida2, forca2, exercito2),)

    mapa = cria_mapa(dimensoes, walls, e1, e2)
    return mapa
    

# --- Codigo Teste :
# --- 1os Testes :
#p1 = cria_posicao(2, 3)
#p2 = cria_posicao(7, 0)
#print(posicoes_iguais(p1, p2))
#print(posicao_para_str(p1))
#print(obter_posicoes_adjacentes(p2))
#tuplo = tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2))
#print(tuplo)

# --- 2os Testes :
#p3 = cria_posicao(2,3)
#vida = 10
#forca = 5
#string = "exercito1"
#unidade1 = cria_unidade(p3, vida, forca, string)
#print(unidade1)
#print(muda_posicao(unidade1,[5,7]))
#print(unidade_para_str(unidade1))

#p = cria_posicao(2, 3)
#u1 = cria_unidade(p, 30, 4, "elfos")
#print(unidade_para_str(u1))
#print(unidade_para_char(u1))
#u2 = cria_copia_unidade(u1)
#print(unidades_iguais(u1, u2))
#u1 = muda_posicao(u1, cria_posicao(3, 3))
#print(unidade_para_str(u1))
#print(unidade_para_str(u2))
#print(unidades_iguais(u1, u2))
#print(tuple(unidade_para_str(u) for u in ordenar_unidades((u1, u2))))
#u2 = remove_vida(u2, 25)
#print(unidade_ataca(u1, u2))
#print(unidade_para_str(u2))    
#print(unidade_ataca(u1, u2))

#labirinto1 = cria_labirinto((5,7),(0,0))    
#print(labirinto1)

# --- 3os Testes :
#d = (7, 5)
#w = (cria_posicao(4,2), cria_posicao(5,2))
#e1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 20, 4, "humans") for p in ((3, 2),(1, 1)))
#e2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 10, 2, "cylons") for p in ((3, 1), (1, 3), (3, 3), (5, 3)))
#m1 = cria_mapa(d, w, e1, e2)
#print(mapa_para_str(m1))
#print(obter_nome_exercitos(m1))
#u1 = obter_unidade(m1, cria_posicao(1,1))
#print(unidade_para_str(u1))
#print(tuple(unidade_para_str(u) for u in obter_unidades_exercito(m1, "humans")))
#print(mapa_para_str(mover_unidade(m1, u1, cria_posicao(2,1))))
#(meu)eliminar_unidade(m1, cria_unidade(cria_posicao(3, 2), 20, 4, "humans"))
#u2 = obter_unidade(m1, cria_posicao(5,3))
#print(mapa_para_str(eliminar_unidade(m1, u2))) 
#u3 = obter_unidade(m1, cria_posicao(3,2))
#print(tuple(unidade_para_str(u) for u in obter_inimigos_adjacentes(m1,u3)))
#(meu)print(obter_inimigos_adjacentes(m1,u3))
#print(obter_movimento(m1, u3))
#u4 = obter_unidade(m1, cria_posicao(1,3))
#print(obter_movimento(m1, u4))

# --- 4os Testes : 
#d = (7, 6)
#w = (cria_posicao(2,3), cria_posicao(4,4))
#e1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 30, 5, "elfos") for p in ((4, 2), (5, 4)))
#e2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 20, 5, "orcos") for p in ((2, 1), (3, 4), (5, 2), (5, 3)))
#m1 = cria_mapa(d, w, e1, e2)
#print(mapa_para_str(m1))
#print((calcula_pontos(m1, "elfos"), calcula_pontos(m1, "orcos")))

# --- 4.2os Testes : 
#print(mapa_para_str(simula_turno(m1))) # 1.
#print((calcula_pontos(m1,"elfos"), calcula_pontos(m1, "orcos")))

#print(mapa_para_str(simula_turno(m1))) # 2.
#print((calcula_pontos(m1,"elfos"), calcula_pontos(m1, "orcos")))

#print(mapa_para_str(simula_turno(m1))) # 3.
#print((calcula_pontos(m1,"elfos"), calcula_pontos(m1, "orcos")))

#print(mapa_para_str(simula_turno(m1))) # 4.
#print((calcula_pontos(m1,"elfos"), calcula_pontos(m1, "orcos")))

# --- 5os Testes :
print(simula_batalha("teste.txt", True))
print("y")

# --- Testes Meus
#unidade1 = cria_unidade((1,1), 10, 6, "exercitoTeste")
#print(unidade1)
#remove_vida(unidade1, 4)
#print(unidade1)
#muda_posicao(unidade1, (2,2))
#print(unidade1)

#print(mapa_para_str(m1))
#eliminar_unidade(m1, e1[1])
#mover_unidade(m1, e1[0], (2,2))
#print(mapa_para_str(m1))
#print(e1[0])