import logging
import json
import pandas as pd
from sqlalchemy import create_engine

# Configurar logs
logging.basicConfig(level=logging.INFO)

def obter_conexao():
    logging.info("Conectando ao banco de dados PostgreSQL...")
    # Alterando 'localhost' para 'postgres_container'
    engine = create_engine('postgresql://user_admin:admin123**@172.21.0.2:5432/app-analise-preditiva')
    return engine

def gravar_dados(arquivo, tipo):
    try:
        engine = obter_conexao()

        if tipo == 'json':
            with open(arquivo, 'r') as f:
                dados_json = json.load(f)
            df = pd.DataFrame(dados_json)
            logging.info(f"Dados JSON:\n{df.head()}")
            df.to_sql('tabela_json', engine, if_exists='append', index=False)
            logging.info("Dados JSON inseridos com sucesso!")

        elif tipo == 'csv':
            df = pd.read_csv(arquivo, encoding='utf-8')
            logging.info(f"Dados CSV:\n{df.head()}")
            df.to_sql('tabela_csv', engine, if_exists='append', index=False)
            logging.info("Dados CSV inseridos com sucesso!")

        elif tipo == 'txt':
            dados = []
            with open(arquivo, 'r') as f:
                for linha in f:
                    municipio, estado, area_km2, desmatado_2022, incremento, floresta_2022 = linha.strip().split(';')
                    dados.append({
                        'municipio': municipio,
                        'estado': estado,
                        'area_km2': float(area_km2),
                        'desmatado_2022': float(desmatado_2022),
                        'incremento_2021_2022': float(incremento),
                        'floresta_2022': float(floresta_2022)
                    })
            df = pd.DataFrame(dados)
            logging.info(f"Dados TXT:\n{df.head()}")
            df.to_sql('tabela_txt', engine, if_exists='append', index=False)
            logging.info("Dados TXT inseridos com sucesso!")

        else:
            logging.error("Tipo de arquivo não suportado!")
    except Exception as e:
        logging.error(f"Erro ao gravar os dados: {e}")

# Exemplo de execução
if __name__ == "__main__":
    logging.info("Iniciando o processo de gravação de dados...")
    gravar_dados('dados_desmatamento_amazonia.json', 'json')
    gravar_dados('dados_desmatamento_amazonia.csv', 'csv')
    gravar_dados('dados_desmatamento_amazonia.txt', 'txt')
    logging.info("Processo de gravação concluído.")
