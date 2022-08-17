# GUSTAVO PEREIRA FIORI

# Programa que lê um arquivo .txt, que nele possui vários conjuntos de dados com várias operações.

def organizacao_print(Operacao, l1, l2, resultado_retorno):
    l1 = "".join(map(str, l1)).strip()
    l2 = "".join(map(str, l2)).strip()
    resultado_retorno = ", ".join(map(str, resultado_retorno)).strip()
    print(
        Operacao + " 1° conjunto " + "{" + l1 + "}" + " 2° conjunto " + "{" + l2 + "}" + " Resultado: " + "{" + resultado_retorno + "}")


# Abertura do código
arquivo = open("teste2.txt", "r")
linhasArquivo = arquivo.readlines()

Array1 = [l.rstrip('\n').split(',') for l in linhasArquivo]

Remover_elemento = Array1.pop(0)

Array_modelos = []
tamanho_Array1 = len(Array1)
for y in range(0, tamanho_Array1, 3):
    Array_modelos.append(Array1[y:y + 3])

Modo_Dicionario = {}

for Var1, Var2 in enumerate(Array_modelos):
    Modo_Dicionario[Var1] = Var2


# Função das operações da resolução.
def Operacao_Uniao(l1, l2):
    resultado_retorno = l1 + l2
    Operacao = "união"
    organizacao_print(Operacao, l1, l2, resultado_retorno)
    return resultado_retorno


def Operacao_Intersecao(l1, l2):
    Operacao = "interseção"
    resultado_retorno = [value for value in l1
                         if value in l2]
    organizacao_print(Operacao, l1, l2, resultado_retorno)
    return resultado_retorno


def Operacao_Diferenca(l1, l2):
    Operacao = "diferença"
    resultado_retorno = [value for value in l1
                         if value not in l2]
    organizacao_print(Operacao, l1, l2, resultado_retorno)
    return resultado_retorno


def Operacao_ProdutoCartesiano(l1, l2):
    resultado_retorno = [a + (b) for a in l1 for b in l2]
    Operacao = "cartesiano"
    organizacao_print(Operacao, l1, l2, resultado_retorno)
    return resultado_retorno


# Looping da operação que faz a leitura das linhas e chama a função.
for key in Modo_Dicionario:
    Inicio = Modo_Dicionario[key][0][0]

    if Inicio == "U":
        Operacao_Uniao(Modo_Dicionario[key][1], Modo_Dicionario[key][2])

    elif Inicio == "D":
        Operacao_Diferenca(Modo_Dicionario[key][1], Modo_Dicionario[key][2])

    elif Inicio == "I":
        Operacao_Intersecao(Modo_Dicionario[key][1], Modo_Dicionario[key][2])

    elif Inicio == "C":
        Operacao_ProdutoCartesiano(Modo_Dicionario[key][1], Modo_Dicionario[key][2])