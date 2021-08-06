from __future__ import print_function
import math

#  função para criar vetores


def crieVetor(nColunas):
    v = []
    for i in range(nColunas):
        v.append(0)
    return v

#  função para criar matrizes


def crieMatriz(nLinhas, nColunas):
    matriz = []
    for i in range(nLinhas):
        linha = crieVetor(nColunas)
        matriz.append(linha)
    return matriz

#  função para fazer um fatorial


def fatorialProcedural(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat


#  função para quantidade de formas de contar


def quantidadeFormasContar(ordem, repeticao, n, r):
    ordem = ordem.upper()
    repeticao = repeticao.upper()
    n = int(n)
    r = int(r)
    retorno = 0
    if n >= 1 and n <= 10:
        if ordem == "S" and repeticao == "S":
            if r >= 1 and r <= n:
                retorno = int(math.pow(n, r))
            else:
                print("ERRO - r menor que 0 ou maior que 10")
                retorno = 0
        elif ordem == "S" and repeticao == "N":
            if r >= 1 and r <= n:
                retorno = int(math.factorial(n) / math.factorial(n - r))
            else:
                print("ERRO - r menor que 0 ou maior que 10")
                retorno = 0
        elif ordem == "N" and repeticao == "S":
            if r >= 1:
                dividendo = math.factorial(n + r - 1)
                divisor = math.factorial(r) * math.factorial(n - 1)
                retorno = int(dividendo / divisor)
            else:
                print("ERRO - r menor que 0")
                retorno = 0
        elif ordem == "N" and repeticao == "N":
            if r >= 1 and r <= n:
                dividendo = math.factorial(n)
                divisor = math.factorial(r) * math.factorial(n - r)
                retorno = int(dividendo / divisor)
            else:
                print("ERRO - r menor que 0 ou maior que 10")
                retorno = 0
        else:
            print("ERRO - ordem ou repeticao diferentes de s ou n")
    else:
        print("ERRO - n menor que 1 ou maior que 10")
    return retorno


#  Função para os possiveis conjuntos


def conjuntos(ordem, repeticao, n, r, qtdFormas):
    ordem = ordem.upper()
    repeticao = repeticao.upper()
    n = int(n)
    r = int(r)
    arranjo = int(math.pow(n, r))
    m = crieMatriz(arranjo, r)
    v = crieVetor(r)
    #  coloca 1 em toda posição do vetor
    for i in range(r):
        v[i] = 1
    #  começando da direita para esquerda no vetor
    i = r - 1
    j = 0
    #  formando o arranjo de maneiras
    while j < arranjo:
        if v[i] <= n:
            if i < (r - 1):
                while i < (r - 1):
                    i += 1
                    v[i] = 1
            for k in range(r):
                m[j][k] = v[k]
            j += 1
            v[i] += 1
        else:
            i -= 1
            v[i] += 1
    if ordem == "S" and repeticao == "S":
        return m
    elif ordem == "S" and repeticao == "N":
        ma = crieMatriz(qtdFormas, r)
        k = 0
        for i in range(arranjo):
            flag = 0
            for j in range(r):
                for w in range(r):
                    if m[i][j] == m[i][w]:
                        if j != w:
                            flag += 1
                            break
            if flag == 0:
                for w in range(r):
                    ma[k][w] = m[i][w]
                k += 1
        return ma
    elif ordem == "N" and repeticao == "S":
        ma = crieMatriz(qtdFormas, r)
        v = crieVetor(n)
        va = crieVetor(n)
        j = 0
        for i in range(qtdFormas):
            flag = 0
            while j < arranjo:
                for w in range(n):
                    v[w] = 0
                for w in range(n):
                    if v[w] == 0:
                        for y in range(r):
                            if m[j][y] == w + 1:
                                v[w] += 1
                flag = 0
                for w in range(qtdFormas):
                    test = 0
                    for y in range(n):
                        va[y] = 0
                    for y in range(n):
                        if va[y] == 0:
                            for z in range(r):
                                if ma[w][z] == y + 1:
                                    va[y] += 1
                    for y in range(n):
                        if v[y] == va[y]:
                            test += 1
                    if test == n:
                        break
                    else:
                        flag += 1
                if flag == qtdFormas:
                    break
                j += 1
            if flag == qtdFormas:
                for w in range(r):
                    ma[i][w] = m[j][w]
                j += 1
        return ma
    elif ordem == "N" and repeticao == "N":
        ma = crieMatriz(qtdFormas, r)
        v = crieVetor(n)
        va = crieVetor(n)
        j = 0
        for i in range(qtdFormas):
            flag = 0
            while j < arranjo:
                cont = 0
                for w in range(n):
                    v[w] = 0
                for w in range(n):
                    if v[w] == 0:
                        for y in range(r):
                            if m[j][y] == w + 1:
                                v[w] += 1
                for w in range(n):
                    if v[w] > 1:
                        cont += 1
                if cont == 0:
                    flag = 0
                    for w in range(qtdFormas):
                        test = 0
                        for y in range(n):
                            va[y] = 0
                        for y in range(n):
                            if va[y] == 0:
                                for z in range(r):
                                    if ma[w][z] == y + 1:
                                        va[y] += 1
                        for y in range(n):
                            if v[y] == va[y]:
                                test += 1
                        if test == n:
                            break
                        else:
                            flag += 1
                    if flag == qtdFormas:
                        break
                j += 1
            if flag == qtdFormas:
                for w in range(r):
                    ma[i][w] = m[j][w]
                j += 1
        return ma