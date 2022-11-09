# -- Numero de Alunos ---------------------------------------------------------------------------
qtdAlunos = 4                    # --------------------------------------------------------------
# -- Cria Dicionario Vazio ----------------------------------------------------------------------
dictSala = {}                    # --------------------------------------------------------------
# -- Preencher o dicionario ---------------------------------------------------------------------
for cont in range(qtdAlunos):    # --------------------------------------------------------------
    nome = input("Digite o nome do %iº aluno: " %(cont + 1)) # ------------------------------------
    nota = float(input("Digite a nota do %iº aluno: " %(cont +1))) # ----------------------------

    dictSala[nome]  = nota

print("\nDicionario apos o preenchimento:")
print(dictSala)

busca = input("Informe o nome para a busca: ")
if busca in dictSala:
    resultado = dictSala[busca]
    print("A nota do %s é %.2f" % (busca, resultado))
else:
    print("%s não existe no dicionario!"%(busca))



