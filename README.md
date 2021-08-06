# Analise-Combinatoria_Python

Para a produção do programa decidi utilizar a linguagem de programação Python devido a
facilidade de utilizar-se fatoriais.
O código foi divido em dois arquivos, __init__.py e analise_combinatoria.py.
Em __init__.py são feitas a criação ou abertura, caso já exista um arquivo, para salvar as
saídas do programa.
analise_combinatoria.py possui 5 funções, crieVetor, crieMatriz, fatorialProcedural,
quantidadeFormasContar e conjuntos.
A função crieVetor cria um vetor com valores nulos e a função crieMatriz utiliza a função
crieVetor para criar um vetor bidimencional.
A função fatorialProcedural faz um fatorial pelo método procedural.
QuantidadeFormasContar é a função responsável pelo retorno da quantidade de conjuntos
possiveis para cada caso, foi utilizado as formulas disponibilizadas no pdf da APS.
A função conjuntos cria a o arranjo de possibilidades para o caso, se for o caso 1 retorno o
arranjo criado.
Caso 2, ela confere se o elemento do arranjo possui repetidos nele, se sim ela vai para
o próximo, se não ela adiciona na matriz de saída.
Caso 3, neste conta-se a quantidade de vezes que se repete um numero no elemento
do arranjo, e testa se a matriz de saida possui alguns elementos com os mesmo casos repetidos, se
sim, vai para o próximo elemento do arranjo, se não, adiciona na matriz de saída.
Caso 4, é o mesmo que o caso 3, porém a um teste antes de conferir com a matriz, se
um elementos do arranjo tem mais que uma repetição vai para o próximo elemento do arranjo, se
não, adiciona na matriz de saída.
