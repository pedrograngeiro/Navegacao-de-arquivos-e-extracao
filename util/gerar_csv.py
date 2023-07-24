import pandas as pd

def gerar_csv(dados, nome_arquivo, colunas=None):

    # Criando um DataFrame com os dados filtrados
    df = pd.DataFrame(dados)

    # Salvar o DataFrame como arquivo CSV
    df.to_csv(nome_arquivo, index=False)

    print("Arquivo CSV gerado com sucesso!")
