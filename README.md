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

docker build -t etl-analise-preditiva .


2. Construir a Imagem da Aplicação

bash
Copiar código
docker build -t etl-analise-preditiva .

3. Criar a Rede Docker
bash
Copiar código
docker network create etl-network


4. Subir o Banco de Dados PostgreSQL
bash
Copiar código
docker-compose up -d


5. Executar o Processo ETL
bash
Copiar código
docker run -it --rm --network etl-network etl-analise-preditiva


6. Verificar o Banco de Dados
bash
Copiar código
docker exec -it postgres_container psql -U user_admin -d robotics_lab_system


7. Parar os Containers
bash
Copiar código
docker-compose down
