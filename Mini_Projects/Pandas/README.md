# Análise de Mercado de Dados

Neste projeto, usei o dataset `lukebarousse/data_jobs` para explorar o mercado de trabalho na área de dados.

A ideia foi entender, através dos dados, quais cargos aparecem com mais frequência nas vagas, onde essas oportunidades estão concentradas e quais tecnologias e habilidades são mais procuradas pelas empresas.

## O que foi analisado

### 1. Panorama geral

Primeiro, fiz uma análise mais ampla do dataset para identificar:

- Os 20 cargos com maior número de vagas;
- Os países com maior quantidade de oportunidades;
- As empresas que mais aparecem na base.

Essas análises ajudam a ter uma visão geral de como as vagas estão distribuídas no mercado.

### 2. Habilidades mais procuradas

Depois, foquei no mercado dos Estados Unidos e analisei os três principais cargos encontrados na etapa anterior.

A partir disso, levantei quais habilidades e tecnologias aparecem com maior frequência nas vagas de cada cargo.

### 3. Evolução das tecnologias

Por fim, analisei as vagas para **Data Analyst** nos Estados Unidos ao longo do tempo.

Criei uma tabela dinâmica para acompanhar, mês a mês, a presença das cinco principais tecnologias encontradas nas vagas e visualizar como essa demanda se comportou durante o período analisado.

## Tratamento dos dados

Antes das análises, foi necessário realizar algumas etapas de preparação dos dados, principalmente:

- Conversão e tratamento das datas;
- Limpeza das informações;
- Transformação de colunas que armazenavam listas como texto;
- Agrupamentos e contagens para encontrar os principais cargos e habilidades.

## Tecnologias utilizadas

- **Python** — linguagem utilizada no projeto;
- **Pandas** — manipulação, limpeza e análise dos dados, incluindo `groupby`, `explode` e tabelas dinâmicas;
- **Matplotlib** — criação dos gráficos;
- **Seaborn** — criação e estilização das visualizações;
- **Hugging Face Datasets** — acesso ao dataset `data_jobs`;
- **AST** — utilização do `literal_eval` para transformar listas armazenadas como texto em estruturas de dados do Python.

## Objetivo

Este projeto faz parte dos meus estudos em **Dados e Engenharia de Dados** e foi desenvolvido como uma forma de praticar análise exploratória, manipulação de dados e visualização utilizando Python.

Mais do que apenas gerar gráficos, a ideia foi utilizar os dados para responder perguntas que poderiam surgir ao analisar o mercado de trabalho na área de tecnologia.
