# -- Faça um programa que preencha uma lista com 10 números reais, calcule
# -- e mostre a quantidade de números negativos e a soma
# -- dos números positivos dessa lista.

# -----------------------------------------------------------------------
qtdNum = 10          # -- Quantidade de Numeros -------------------------
listaNum = []        # -- Cria a lista vazia ----------------------------
contNeg = 0          # -- Variavel que conta a quantidade de negativos --
contPos = 0          # -- Variavel que conta a quantidade de positivos --
somaPos = 0          # -- Variavel que soma os positivos ----------------
# -----------------------------------------------------------------------
# -- Preenche a lista ---------------------------------------------------
for cont in range(qtdNum):         # - Para contagem em qtdNum ----------
    numero = float(input("Digite o %dº número: " %(cont + 1))) # --------
    listaNum.append(numero)        # -- anexa o numero na lista ---------
# -- Percorre a lista ja preenchida -------------------------------------
# -- for cont in range(qtdNum): ou/ -------------------------------------
for item in listaNum:              # -- Para item na lista --------------
    if item < 0:                   # -- Se o item for menor que 0 -------
        contNeg += 1               # -- | contNeg = contNeg + 1 | -------
    else:                          # -- Senão ---------------------------
        somaPos = somaPos + item   # -- Somatorio dos Posit. na lista----
# -- Mostrar os resultados obtidos --------------------------------------
print("\nQuantidade de numeros negativos: %i" %(contNeg)) # -------------
print("\nSomade numeros positivos: %.2f" %(somaPos))      # -------------
# -- Fim ----------------------------------------------------------------








