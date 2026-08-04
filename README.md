#  Data Engineering Lab & Practice Roadmap

Repositório dedicado aos meus estudos, exercícios e laboratórios práticos voltados para **Engenharia de Dados**.

Este espaço reúne a construção da minha base técnica em Python e SQL e acompanhará minha evolução em temas como ingestão de dados, APIs, processamento distribuído, computação em nuvem, containerização e orquestração de pipelines.

---

##  Sobre o repositório

Este repositório funciona como um laboratório contínuo de aprendizado.

Aqui organizo exercícios, testes, consultas, scripts e pequenas implementações desenvolvidas durante meus estudos. A ideia não é apresentar todos os conteúdos como projetos completos de portfólio, mas documentar minha evolução técnica, registrar os conceitos praticados e criar uma base que possa ser revisitada e aprimorada ao longo do tempo.

Atualmente, o foco principal está na consolidação dos fundamentos de:

- Python aplicado a Dados;
- SQL e bancos de dados relacionais;
- manipulação e transformação de dados;
- modelagem e consultas analíticas;
- organização e versionamento de código.

À medida que novos conhecimentos forem consolidados, o repositório receberá novos módulos relacionados a APIs, formatos de dados, Spark, Databricks, AWS, Docker e Airflow.

> **Sobre o uso de Inteligência Artificial:** ferramentas de IA podem ser utilizadas como apoio durante os estudos para esclarecer dúvidas, sugerir abordagens, ajudar na interpretação de erros e auxiliar na evolução de alguns exercícios. O objetivo, porém, é compreender a lógica implementada, testar diferentes soluções e consolidar os conceitos na prática, e não apenas reproduzir códigos prontos.

---

##  Estrutura atual

Atualmente, o repositório está organizado em duas frentes principais: **Python para Dados** e **SQL para Engenharia de Dados**.

```text
data_engineering_lab/
│
├── Python_DE/
│   │
│   ├── Basic/
│   │   └── Exercícios de lógica, estruturas de dados,
│   │       Pandas e Matplotlib
│   │
│   └── Intermediary/
│       └── Tratamento, transformação e limpeza
│           de dados com Pandas
│
└── SQL_DE/
    │
    ├── Funcionalidades/
    │   └── DDL, DML, CASE, Subqueries,
    │       CTEs e operadores de conjunto
    │
    ├── Functions/
    │   └── Funções de texto e data,
    │       funções aninhadas e Window Functions
    │
    └── Merge/
        └── Rotinas de UPSERT, MERGE
            e criação de snapshots

```
A estrutura poderá ser modificada conforme novos conteúdos forem adicionados e os estudos evoluírem.

---

##  Conhecimentos praticados

Os exercícios e laboratórios presentes atualmente têm como foco a aplicação prática dos seguintes conceitos.

##  Python para Dados

Estudos voltados para lógica de programação, manipulação de dados e automação de tarefas.

Principais temas praticados:

*estruturas de dados;
*condicionais e estruturas de repetição;
*funções e organização de código;
*leitura e manipulação de arquivos;
*filtragem e transformação de dados;
*tratamento de valores ausentes;
*identificação e remoção de duplicidades;
*agregações e agrupamentos;
*manipulação de DataFrames com Pandas;
*criação de visualizações com Matplotlib.

##  SQL para Engenharia de Dados

Exercícios voltados para consultas, transformação de dados e construção de soluções analíticas utilizando bancos de dados relacionais.

Principais temas praticados:


*SELECT, WHERE, ORDER BY e GROUP BY;
*JOINs e relacionamentos entre tabelas;
*DDL e DML;
*CASE WHEN;
*subqueries;
*Common Table Expressions (CTEs);
*operadores de conjunto;
*funções de texto e data;
*funções aninhadas;
*Window Functions;
*rankings e análises temporais;
*rotinas de MERGE e UPSERT;
*criação e comparação de snapshots.


##  Git e GitHub

Utilização do Git e GitHub para:

* Controle de versão;
* Organização dos estudos;
* Acompanhamento da evolução do código;
* Registro das alterações realizadas;
* Documentação dos exercícios e laboratórios.

---

## Roadmap de Desenvolvimento

Este repositório continuará sendo expandido conforme novos conhecimentos forem estudados e praticados.

Os tópicos abaixo representam os próximos passos planejados. Eles ainda estão em processo de aprendizado e **não devem ser interpretados como tecnologias já dominadas**.

## Integração e Coleta de Dados — APIs e Formatos

Estudos sobre:

* Consumo de APIs REST com Python;
* Requisições HTTP;
* Leitura e tratamento de respostas em JSON;
* Paginação e coleta de dados;
* Tratamento de erros;
* Armazenamento de dados brutos;
* Manipulação de formatos como CSV, JSON, Parquet e XML.

##  Processamento Distribuído — Spark e Databricks

Introdução aos conceitos de processamento distribuído e transformação de dados em maior escala.

**Temas planejados:**

* Fundamentos do Apache Spark;
* DataFrames com PySpark;
* Transformações e agregações;
* Leitura e escrita de dados;
* Particionamento;
* Formato Parquet;
* Arquitetura Medallion;
* Utilização do Databricks como ambiente de desenvolvimento e processamento.

## Computação em Nuvem — AWS

Estudos introdutórios sobre serviços de nuvem e sua utilização em pipelines de dados.

**Possíveis temas:**

* Amazon S3 para armazenamento de dados;
* Organização de arquivos em buckets;
* Permissões e conceitos básicos de IAM;
* Integração entre armazenamento e processamento;
* AWS Lambda e computação serverless;
* Amazon Athena para consultas sobre dados armazenados;
* Conceitos de Data Warehouse e serviços relacionados.

## Containerização — Docker

Estudos sobre criação e execução de ambientes isolados para aplicações e pipelines.

**Temas planejados:**

* Imagens e containers;
* Criação de Dockerfile;
* Volumes e portas;
* Gerenciamento de dependências;
* Utilização do Docker Compose;
* Execução de aplicações em ambientes reproduzíveis.

##  Orquestração de Pipelines — Apache Airflow

Estudos sobre organização, agendamento e monitoramento de fluxos de dados.

**Temas planejados:**

* Fundamentos de orquestração;
* Criação de DAGs;
* Tarefas e dependências;
* Agendamento de pipelines;
* Monitoramento de execuções;
* Tratamento básico de falhas;
* Integração entre etapas de ingestão e transformação.


O foco é aprender cada etapa de forma progressiva, entendendo o papel das ferramentas e evitando utilizar tecnologias apenas como palavras-chave.

---

##  Próximos Objetivos

Os próximos passos são:

* Aprofundar os conhecimentos em APIs, JSON e ingestão de dados;
* Estudar os fundamentos do Apache Spark e praticar com PySpark;
* Explorar o Databricks como ambiente de processamento;
* Aprender os conceitos essenciais de computação em nuvem com AWS;
* Estudar Docker e criação de ambientes reproduzíveis;
* Aprender os fundamentos de orquestração com Apache Airflow;
* Utilizar os conhecimentos consolidados em um projeto autoral de pipeline de dados End-to-End.
