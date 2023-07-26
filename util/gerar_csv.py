import pandas as pd

def gerar_csv(dados, nome_arquivo, colunas=None):

    # Criando um DataFrame com os dados filtrados
    df = pd.DataFrame(dados)

    #Verificar se todas as colunas estão presentes no DataFrame
    if colunas:
        for coluna in colunas:
            if coluna not in df.columns:
                df[coluna] = ""
    # Verificar se a ordem das colunas foi especificada.
    if colunas:
        df = df[colunas]

    # Salvar o DataFrame como arquivo CSV
    df.to_csv(nome_arquivo, index=False)

    print("Arquivo CSV gerado com sucesso!")
