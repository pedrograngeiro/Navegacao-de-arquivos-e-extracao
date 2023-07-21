
<!-- TOC -->
  * [Etapas a fazer](#etapas-a-fazer)
  * [Funcionalidades](#funcionalidades)
  * [Personalização](#personalização)
  * [Funções existentes](#funções-existentes)
<!-- TOC -->

Este é um script em Python que percorre uma estrutura de diretórios em
busca de arquivos em determinados formatos e gera um arquivo CSV com os
dados coletados.
<br>
Ele inclui funcionalidades para filtrar os dados por ano e mês.

## Etapas a fazer

- Clone este repositório para o seu ambiente local.
- Configure o diretório raiz e os tipos de arquivos desejados no código.
- Execute o arquivo `lista_ultimo_arquivo.py`.

## Funcionalidades

O script irá percorrer a estrutura de diretórios a parti do caminho
especifica e coletar dados de acordo com os critérios definidos.
Em seguida, ele imprimirá os caminhos dos dados coletados e gerará um
arquivo CSV com os resultados.

## Personalização

Você pode personalizar o script de acrodo com suas necessidades.
Algumas possíveis modificações incluem:
<br>
  - Adicionar novos tipos de arquivo na lista `tipo_arquivos_pastas`.
  - Modificar as siglas dos estados na lista `siglas_estados`.
  

## Funções existentes
- listar_ultimo_arquivo.py
  - percorrer_pastas

- util
  - gerar_csv.py
    - gerar_csv


