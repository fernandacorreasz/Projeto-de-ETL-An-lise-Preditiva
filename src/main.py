import os
import random
import logging
from time import sleep
from gerador_dados import gerar_dados_csv, gerar_dados_json, gerar_dados_txt
from gravar_dados import gravar_dados  # Função consolidada que faz a inserção no banco

# Configuração básica de logging
logging.basicConfig(
    filename='etl_process.log',
    filemode='a',  # 'a' para adicionar ao arquivo existente
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Diretório base do projeto (o diretório "analises")
diretorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Diretório onde os arquivos serão salvos, dentro de "analises"
diretorio_dados = os.path.join(diretorio_base, 'analises', 'data')

# Função principal para gerar e processar os dados
def main():
    try:
        # Garante que a pasta de saída 'analises/data' existe dentro da aplicação
        os.makedirs(diretorio_dados, exist_ok=True)
        logging.info(f'Diretório de dados garantido em: {diretorio_dados}')
    except Exception as e:
        logging.error(f'Erro ao criar diretório {diretorio_dados}: {e}')
        return  # Saia se não conseguir criar o diretório

    while True:
        try:
            logging.info("Iniciando processo ETL...")

            # Definir caminhos para os arquivos de dados dentro da pasta 'analises/data'
            arquivo_json = os.path.join(diretorio_dados, 'dados_desmatamento_amazonia.json')
            arquivo_csv = os.path.join(diretorio_dados, 'dados_desmatamento_amazonia.csv')
            arquivo_txt = os.path.join(diretorio_dados, 'dados_desmatamento_amazonia.txt')

            # Geração de dados
            logging.info(f'Gerando arquivo JSON em: {arquivo_json}')
            gerar_dados_json(random.randrange(1, 150), arquivo_json)

            logging.info(f'Gerando arquivo CSV em: {arquivo_csv}')
            gerar_dados_csv(random.randrange(1, 150), arquivo_csv)

            logging.info(f'Gerando arquivo TXT em: {arquivo_txt}')
            gerar_dados_txt(random.randrange(1, 150), arquivo_txt)

            # Inserção dos dados no banco
            logging.info(f'Inserindo dados do arquivo JSON ({arquivo_json}) no banco de dados.')
            gravar_dados(arquivo_json, 'json')

            logging.info(f'Inserindo dados do arquivo CSV ({arquivo_csv}) no banco de dados.')
            gravar_dados(arquivo_csv, 'csv')

            logging.info(f'Inserindo dados do arquivo TXT ({arquivo_txt}) no banco de dados.')
            gravar_dados(arquivo_txt, 'txt')

            logging.info("Processo ETL finalizado. Aguardando 1 minuto...")
            sleep(60)

        except Exception as e:
            logging.error(f'Ocorreu um erro durante o processo ETL: {e}')
            sleep(60)  # Aguarde um minuto antes de tentar novamente

if __name__ == "__main__":
    main()
