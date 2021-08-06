# -*- coding: utf-8 -*-
from __future__ import print_function
from analise_combinatoria import *


def main():
    arq = open("saida.txt", "a")
    print("Analise combinatoria")
    print("Digite a entrada de dados no seguinte padrao:")
    print("<ordem> <repeticao> <n> <r>")
    print("Digite:")
    ordem, repeticao, n, r = input("").split(' ')
    qtdFC = quantidadeFormasContar(ordem, repeticao, n, r)
    if qtdFC != 0:
        arq.write(str(qtdFC) + "\n")
        m = conjuntos(ordem, repeticao, n, r, qtdFC)
        for i in range(qtdFC):
            for j in range(int(r)):
                arq.write(str(m[i][j]) + " ")
            arq.write("\n")
        arq.write(str(math.factorial(qtdFC)) + " : " + str(fatorialProcedural(qtdFC)) + "\n\n")
        print("Resultado em saida.txt")


if __name__ == "__main__":
    main()