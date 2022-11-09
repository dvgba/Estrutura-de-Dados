# -- Numero de Alunos ---------------------------------------------------------------------------
qtdFilmes = 1  # --------------------------------------------------------------
# -- Cria Dicionario Vazio ----------------------------------------------------------------------
dictFilme = {}
dictFilme1 = {}
dictFilme2 = {}
dictFilme3 = {}
# -- Preencher o dicionario ---------------------------------------------------------------------
for cont in range(qtdFilmes):  # --------------------------------------------------------------
    nome = input("[Filme %i] Digite o nome do filme: " % (cont + 1))  # ------------------------------------
    vilao = input("[Filme %i] Informe o Vilão do filme:  " % (cont + 1))  # ------------------------------------
    ano = int(input("[Filme %i] Informe o Vilão do filme:  " % (cont + 1)))  # ------------------------------------
    dictFilme1[nome] = ("{" + vilao + "," + str(ano) + "}")



print("\nDicionario ")
print(cont for cont in range(qtdFilmes))
