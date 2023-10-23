def ler_arquivo(nome_arquivo):
    dados = []
    f = open(nome_arquivo, "r")
    linhas = f.readlines()
    for linha in linhas:
        dados.append(linha.strip().split(","))
    f.close()
    return dados

def distribuicao_doenca_por_sexo(dados):
    contagem_masculino = 0
    contagem_feminino = 0
    for linha in dados[1:]:
        if linha[1] == "Masculino" and linha[8] == "1":
            contagem_masculino += 1
        elif linha[1] == "Feminino" and linha[8] == "1":
            contagem_feminino += 1
    return {"Masculino": contagem_masculino, "Feminino": contagem_feminino}

def distribuicao_doenca_por_idade(dados):
    distribuicao_idade = {}
    for linha in dados[1:]:
        if linha[8] == "1":
            idade = int(linha[7])
            grupo_idade = int(idade / 5) * 5
            if grupo_idade not in distribuicao_idade:
                distribuicao_idade[grupo_idade] = 0
            distribuicao_idade[grupo_idade] += 1
    return distribuicao_idade

def distribuicao_doenca_por_glicose(dados):
    distribuicao_glicose = {}
    for linha in dados[1:]:
        if linha[8] == "1":
            nivel_glicose = int(linha[2])
            grupo_glicose = int(nivel_glicose / 10) * 10
            if grupo_glicose not in distribuicao_glicose:
                distribuicao_glicose[grupo_glicose] = 0
            distribuicao_glicose[grupo_glicose] += 1
    return distribuicao_glicose

def imprimir_tabela(distribuicao):
    for chave, valor in distribuicao.items():
        print(str(chave) + ": " + str(valor))

def principal():
    dados = ler_arquivo("diabetes_prediction_dataset.csv")
    
    print("Distribuição da doença por sexo:")
    distribuicao_sexo = distribuicao_doenca_por_sexo(dados)
    imprimir_tabela(distribuicao_sexo)
    
    print('\nDistribuição da doença por idade:')
    distribuicao_idade = distribuicao_doenca_por_idade(dados)
    imprimir_tabela(distribuicao_idade)
    
    print('\nDistribuição da doença por níveis de glicose:')
    distribuicao_glicose = distribuicao_doenca_por_glicose(dados)
    imprimir_tabela(distribuicao_glicose)

principal()