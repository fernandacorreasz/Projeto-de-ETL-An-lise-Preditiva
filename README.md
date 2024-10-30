# Projeto ETL - Análise Preditiva e Descritiva

Este projeto tem como objetivo realizar um processo de ETL (Extract, Transform, Load) para gerar dados simulados relacionados ao desmatamento e queimadas na Amazônia, e inserir esses dados em um banco de dados PostgreSQL para fins de análise preditiva e descritiva. 

## Descrição Acadêmica

Este projeto foi desenvolvido para a disciplina de **Análise Preditiva** como parte da entrega acadêmica. O conjunto de dados gerado é artificial e foi criado especificamente para atividades educacionais. A partir desses dados, podemos realizar análises preditivas para detectar padrões de desmatamento e prever tendências futuras. Além disso, análises descritivas permitem entender o estado atual das áreas desmatadas e remanescentes de floresta. 

## Pré-requisitos

- Docker
- Docker Compose


## Instruções para Execução

Siga os passos abaixo para rodar o projeto em um ambiente Dockerizado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Construir a Imagem da Aplicação

Use o comando a seguir para construir a imagem Docker da aplicação ETL:

```bash
docker build -t etl-analise-preditiva .
```

### 3. Criar a Rede Docker

Crie uma rede Docker para permitir a comunicação entre os containers:

```bash
docker network create etl-network
```

### 4. Subir o Banco de Dados PostgreSQL

```bash
docker-compose up -d
```

### 5. Executar o Processo ETL

```bash
docker run -it --rm --network etl-network etl-analise-preditiva
```

### 6. Verificar o Banco de Dados

```bash
docker exec -it postgres_container psql -U user_admin -d app-analise-preditiva
```

### 7. Parar os Containers

```bash
docker-compose down
```
