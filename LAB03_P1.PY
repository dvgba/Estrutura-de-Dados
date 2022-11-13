# -- Numero de Alunos ---------------------------------------------------------------------------
qtdPessoas = 2                    # --------------------------------------------------------------
# -- Cria Dicionario Vazio ----------------------------------------------------------------------
dictSala = {}                  # --------------------------------------------------------------
dictSala2 = {}
# -- Preencher o dicionario ---------------------------------------------------------------------
for cont in range(qtdPessoas):
    nomes = input("[%iº pessoa] Digite o nome: " %(cont + 1)) # ------------------------------------
    qtdPessoas.append(nomes)


print("\nLista de nome: ")
print(qtdPessoas)
