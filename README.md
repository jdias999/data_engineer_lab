# Data Engineering Lab & Practice Roadmap

Repositório dedicado aos meus estudos contínuos, exercícios, scripts de teste e laboratórios práticos voltados para **Engenharia de Dados**.

Diferente dos meus repositórios de projetos completos ponta a ponta, este espaço funciona como um ambiente de rascunho e prática diária: aqui registro consultas, testes de bibliotecas, consumo de APIs, transformações isoladas e experimentos com ferramentas antes de aplicá-los em arquiteturas maiores.

---

## Sobre o Repositório

A proposta deste laboratório é documentar minha evolução técnica e manter uma base própria de consulta que possa ser revisitada ao longo do tempo.

Os códigos aqui presentes serviram de base para os projetos principais do meu portfólio, onde conecto esses conceitos em pipelines completos (como o pipeline Lakehouse na Azure com Databricks e ADF, e o pipeline ETL com dados da ANAC).

---

## Conhecimentos Praticados

Os exercícios, notebooks e scripts deste repositório cobrem a prática dos seguintes temas:

### Python para Engenharia e Análise de Dados
Estudos voltados para lógica, automação, consumo de dados externos e manipulação tabular:
- Estruturas de dados, funções modulares e organização de código;
- Leitura e escrita de arquivos em diferentes formatos (`CSV`, `JSON` e `Parquet`);
- Consumo de APIs REST com requisições HTTP, paginação e tratamento de respostas em JSON;
- Limpeza de dados, tratamento de valores ausentes e remoção de duplicidades;
- Manipulação, filtragem e agregação de dados com **Pandas**;
- Visualização exploratória de dados com **Seaborn** e **Matplotlib**.

### SQL e Modelagem de Dados
Consultas analíticas, transformação e estruturação de dados em bancos relacionais (**PostgreSQL**, **DuckDB** e **Spark SQL**):
- Consultas estruturadas (`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`);
- Relacionamentos e cruzamentos entre tabelas (`INNER`, `LEFT`, `CROSS` e `ANTI JOIN`);
- Comandos `DDL` e `DML`;
- Subqueries, `CASE WHEN` e Common Table Expressions (`CTEs`);
- Funções de janela (*Window Functions* como `ROW_NUMBER`, rankings e análises temporais);
- Rotinas idempotentes de atualização com `MERGE INTO` / `UPSERT`;
- Modelagem dimensional (tabelas Fato, Dimensão e views analíticas).

### Processamento Distribuído e Lakehouse (Spark & Databricks)
Práticas voltadas para processamento de dados em escala e organização em camadas:
- Manipulação de DataFrames e transformações distribuídas com **PySpark**;
- Leitura, escrita e versionamento de tabelas em formato **Delta Lake**;
- Aplicação da **Arquitetura Medallion** (Landing, Bronze, Silver e Gold);
- Ingestão incremental de arquivos com **Databricks Auto Loader** e controle de **Watermark**;
- Organização de catálogos, schemas, tabelas e volumes no **Unity Catalog**.

### Cloud, Infraestrutura Local e Versionamento
- **Microsoft Azure:** Práticas de integração entre **Azure Data Lake Storage Gen2 (ADLS Gen2)**, **Azure Databricks** e orquestração de notebooks com **Azure Data Factory (ADF)**;
- **Docker:** Criação e uso de containers com `Docker` e `Docker Compose` para subir bancos de dados e ambientes locais isolados;
- **Git e GitHub:** Versionamento de código, organização de repositórios e documentação técnica.

---

## Roadmap e Próximos Estudos

Este repositório continua recebendo novos testes conforme avanço nos estudos. Os tópicos abaixo representam as frentes que estou aprofundando atualmente ou planejo explorar nos próximos módulos:

### Orquestração de Pipelines — Apache Airflow
- Construção e agendamento de DAGs locais via Docker;
- Gerenciamento de dependências entre tarefas, *retries* e monitoramento de falhas;
- Integração de scripts Python e bancos de dados dentro de fluxos orquestrados.

### Otimização, Qualidade de Dados e DataOps
- Aprofundamento em performance no Apache Spark (particionamento, *caching*, *broadcast joins* e organização física no Delta Lake);
- Automação de testes de qualidade de dados (*Data Quality checks*) e contratos de dados;
- Transformação modular com **dbt**;
- Conceitos de CI/CD aplicados a repositórios de dados.

### Expansão Multi-Cloud — AWS
- Exploração dos serviços equivalentes no ecossistema AWS para ampliar a base em nuvem (como **Amazon S3**, permissões no **IAM**, **AWS Glue / Lambda** e consultas serverless com **Amazon Athena**).

---

## Projetos Completos

Para ver a aplicação prática desses conceitos integrados em pipelines ponta a ponta, acesse os repositórios principais no meu perfil:

- **Global Data Center Infrastructure, Energy & Environmental Impact — Lakehouse:** Pipeline incremental na nuvem Azure (ADLS Gen2, Databricks, PySpark, Spark SQL, Delta Lake, Unity Catalog e Azure Data Factory).
- **SAC ANAC — Pipeline ETL & Análise:** Processamento e modelagem local de mais de 100 mil registros públicos utilizando Python, Pandas, SQL e DuckDB.
