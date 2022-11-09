# -- Faça um programa que receba e armazene em uma lista 8 valores float, em seguida mostre:
# ------------------------------------------------------------------------------------------
# -- A lista preenchida com os valores recebidos. ------------------------------------------
# -- O maior valor dessa lista e em qual posição ele se encontra. --------------------------
# -- O menor valor dessa lista e em qual posição ele se encontra. --------------------------
# ------------------------------------------------------------------------------------------
# -- Observação: ---------------------------------------------------------------------------
# -- Não é permitido utilizar funções prontas do Python, como por exemplo MAX e MIN. -------
# ------------------------------------------------------------------------------------------
# -- Resolução -----------------------------------------------------------------------------
listNum = []                           # -- Cria a lista vazia -----------------------------
qtdNum = 8                             # -- Quantidade de numeros --------------------------
numMax = 0                             # -- Variavel do maior numero -----------------------
numMin = 0                             # -- Variavel do menor numero -----------------------
posMax = 0                             # -- Armazena a posição do maior numero -------------
posMin = 0                             # -- Armazena a posição do menor numero -------------
# ------------------------------------------------------------------------------------------
# -- Preenche a lista ----------------------------------------------------------------------
for c in range(qtdNum):                # -- Para c em qtdNum -------------------------------
    listNum.append(float(input('Digite o %dº número: ' %(c+1)))) # -------------------------
    if c == 0:                         # -- Condição com "c" sendo igual a "0" -------------
       numMax = numMin = listNum[c]    # -- Maior é igual a menor na lista -----------------
    else:                              # -- Senão ------------------------------------------
        if listNum[c] > numMax:        # -- Se o elemento c na lista for o maior -----------
            numMax = listNum[c]        # -- numMax vai ser o maior elemento ----------------
        if listNum[c] < numMin:        # -- Se o elemento c na lista for o menor -----------
            numMin = listNum[c]        # -- numMin vai ser o menor elemento ----------------
# ------------------------------------------------------------------------------------------
# -- Localizar o o maior e o menor ---------------------------------------------------------
for c in range(len(listNum)):         # -- Para o numero de elementos da lista -------------
    if listNum[c] == numMax:          # -- Se o elemento c  for o maior --------------------
        posMax += 1                   # ----------------------------------------------------
        posMax = c                    # -- essa é a sua posição ----------------------------
    elif listNum[c] == numMin:        # -- Se o elemento c for o menor ---------------------
        posMax += 1                   # ----------------------------------------------------
        posMin = c                    # -- essa é a sua posição ----------------------------
# ------------------------------------------------------------------------------------------
# -- Imprimi o programa  -------------------------------------------------------------------
print(listNum)                                                            # ----------------
print("O maior valor da lista é %.2f na posição %d " %(numMax, posMax))   # ----------------
print("O menor valor da lista é %.2f na posição %d " %(numMin, posMin))   # ----------------
# ------------------------------------------------------------------------------------------
# -- Fim  ----------------------------------------------------------------------------------


