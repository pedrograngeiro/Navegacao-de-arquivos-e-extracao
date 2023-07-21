import pandas as pd

def gerar_csv(dados, nome_arquivo, colunas=None):
    if not colunas:
        # Se a lista de colunas não for fornecida, usamos todas as chaves do primeiro dicionário como colunas
        colunas = dados[0].keys() if dados else []

    # Filtrar os dados para incluir apenas as colunas desejadas
    dados_filtrados = [{coluna: dado[coluna] for coluna in colunas} for dado in dados]

    # Criando um DataFrame com os dados filtrados
    df = pd.DataFrame(dados_filtrados)

    # Salvar o DataFrame como arquivo CSV
    df.to_csv(nome_arquivo, index=False)

    print("Arquivo CSV gerado com sucesso!")
