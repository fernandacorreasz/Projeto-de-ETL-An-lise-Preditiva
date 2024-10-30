import json
import random
from faker import Faker
import csv

# Função para gerar dados em formato JSON
def gerar_dados_json(num_registros, arquivo_json):
    municipios = [
        "Manaus", "Parintins", "Itacoatiara", "Manacapuru", "Coari", "Tabatinga", 
        "Maués", "Tefé", "Humaitá", "São Gabriel da Cachoeira", "Benjamin Constant", 
        "Eirunepé", "Lábrea", "Presidente Figueiredo", "Boca do Acre", "Iranduba", 
        "Manicoré", "Autazes", "Borba", "Novo Aripuanã"
    ]
    
    dados = []

    for _ in range(num_registros):
        municipio = random.choice(municipios)
        estado = "AM"
        area_km2 = round(random.uniform(1000, 60000), 2)
        desmatado_2022 = round(random.uniform(500, area_km2 * 0.6), 2)
        incremento = round(random.uniform(10, 200), 2)
        floresta_2022 = round(area_km2 - desmatado_2022, 2)

        registro = {
            'municipio': municipio,
            'estado': estado,
            'area_km2': area_km2,
            'desmatado_2022': desmatado_2022,
            'incremento_2021_2022': incremento,
            'floresta_2022': floresta_2022
        }
        dados.append(registro)

    # Gravar os dados em arquivo JSON
    with open(arquivo_json, 'w') as f:
        json.dump(dados, f, indent=4)

# Função para gerar dados em formato CSV
def gerar_dados_csv(num_registros, arquivo_csv):
    municipios = [
        "Manaus", "Parintins", "Itacoatiara", "Manacapuru", "Coari", "Tabatinga", 
        "Maués", "Tefé", "Humaitá", "São Gabriel da Cachoeira", "Benjamin Constant", 
        "Eirunepé", "Lábrea", "Presidente Figueiredo", "Boca do Acre", "Iranduba", 
        "Manicoré", "Autazes", "Borba", "Novo Aripuanã"
    ]

    with open(arquivo_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        # Escreve o cabeçalho
        writer.writerow(['Municipio', 'Estado', 'Area Km2', 'Desmatado 2022', 'Incremento 2021/2022', 'Floresta 2022'])

        for _ in range(num_registros):
            municipio = random.choice(municipios)
            estado = "AM"
            area_km2 = round(random.uniform(1000, 60000), 2)
            desmatado_2022 = round(random.uniform(500, area_km2 * 0.6), 2)
            incremento = round(random.uniform(10, 200), 2)
            floresta_2022 = round(area_km2 - desmatado_2022, 2)

            writer.writerow([municipio, estado, area_km2, desmatado_2022, incremento, floresta_2022])

# Função para gerar dados em formato TXT
def gerar_dados_txt(num_registros, arquivo_txt):
    municipios = [
        "Manaus", "Parintins", "Itacoatiara", "Manacapuru", "Coari", "Tabatinga", 
        "Maués", "Tefé", "Humaitá", "São Gabriel da Cachoeira", "Benjamin Constant", 
        "Eirunepé", "Lábrea", "Presidente Figueiredo", "Boca do Acre", "Iranduba", 
        "Manicoré", "Autazes", "Borba", "Novo Aripuanã"
    ]

    with open(arquivo_txt, 'w') as f:
        for _ in range(num_registros):
            municipio = random.choice(municipios)
            estado = "AM"
            area_km2 = round(random.uniform(1000, 60000), 2)
            desmatado_2022 = round(random.uniform(500, area_km2 * 0.6), 2)
            incremento = round(random.uniform(10, 200), 2)
            floresta_2022 = round(area_km2 - desmatado_2022, 2)

            f.write(f"{municipio};{estado};{area_km2};{desmatado_2022};{incremento};{floresta_2022}\n")

# Exemplos de uso
gerar_dados_json(20, 'dados_desmatamento_amazonia.json')
gerar_dados_csv(20, 'dados_desmatamento_amazonia.csv')
gerar_dados_txt(20, 'dados_desmatamento_amazonia.txt')
