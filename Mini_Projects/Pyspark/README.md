# Análise de Séries do TMDB com PySpark

Neste projeto, usei **Python, PySpark e Databricks** para montar um pequeno pipeline de dados utilizando informações da API do **The Movie Database (TMDB)**.

A ideia foi praticar algumas etapas comuns em um pipeline de dados: buscar informações em uma API, armazená-las em uma tabela, fazer o processamento com Spark e, por fim, extrair alguns insights a partir dos dados das 100 séries mais populares.

## Como o projeto funciona

O projeto foi dividido em dois notebooks principais, cada um responsável por uma etapa do pipeline.

### 1. Ingestão dos dados — `01_ingestao_dados.ipynb`

Nesta etapa, faço a extração dos dados diretamente da API do TMDB.

O processo inclui:

- Consulta ao endpoint `/tv/popular`;
- Paginação para coletar os dados necessários;
- Tratamento de erros utilizando `try-except`;
- Tratamento específico para erros de requisição (`RequestException`) e respostas HTTP inválidas (`HTTPError`);
- Conversão dos dados recebidos em um DataFrame do PySpark;
- Persistência dos dados no Databricks como uma tabela Delta.

Os dados são armazenados na tabela:

`default.top_100_tmdb`

### 2. Insights — `02_insights.ipynb`

Depois da ingestão, utilizo a tabela Delta para realizar as transformações e análises.

Primeiro, faço uma limpeza básica dos dados, removendo séries que possuem popularidade igual a zero. Isso evita problemas na hora de realizar os cálculos.

Em seguida, criei uma métrica chamada `base_fa`, calculada a partir da relação entre a quantidade de votos e a popularidade da série.

Com essa métrica, utilizei uma **Window Function** com `row_number()` para criar um ranking das séries.

Depois, as séries foram divididas em cinco categorias:

- **S**
- **A**
- **B**
- **C**
- **D**

Essa classificação foi feita de acordo com a posição de cada série no ranking, utilizando a função condicional `when()` do PySpark.

Por fim, agrupei os resultados para descobrir quantas séries ficaram em cada Tier.

## Segurança das credenciais

A chave da API não fica diretamente dentro dos notebooks.

Para isso, utilizo um arquivo separado chamado `credenciais.py`, responsável por armazenar a `TMDB_API_KEY`.

Esse arquivo deve ficar fora do controle de versão para evitar que uma chave de API seja exposta no repositório.

## Tecnologias utilizadas

- **Python** — linguagem utilizada no projeto;
- **PySpark** — processamento e transformação dos dados;
- **Databricks** — ambiente utilizado para executar o pipeline;
- **Spark SQL Functions** — funções utilizadas nas transformações e análises;
- **Delta Lake** — armazenamento dos dados em formato Delta;
- **Requests** — consumo da API do TMDB.

## O que pratiquei neste projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Engenharia de Dados**.

Além de praticar PySpark, a ideia foi entender melhor como funciona um fluxo simples de dados, passando por etapas de **extração → armazenamento → transformação → análise**.

Também aproveitei o projeto para praticar conceitos como **Window Functions, DataFrames, tratamento de exceções, APIs, Delta Lake e processamento distribuído com Spark**.
