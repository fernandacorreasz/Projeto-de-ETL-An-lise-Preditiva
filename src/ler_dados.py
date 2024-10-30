import json
import csv
import pandas as pd

def ler_e_consolidar_dados(arquivo_json, arquivo_csv, arquivo_txt):
    dados_consolidados = []

    # Ler dados do JSON
    with open(arquivo_json, 'r') as f:
        dados_json = json.load(f)
        for registro in dados_json:
            dados_consolidados.append({
                'municipio': registro['municipio'],
                'estado': registro['estado'],
                'area_km2': registro['area_km2'],
                'desmatado_2022': registro['desmatado_2022'],
                'incremento_2021_2022': registro['incremento_2021_2022'],
                'floresta_2022': registro['floresta_2022']
            })

    # Ler dados do CSV
    with open(arquivo_csv, 'r') as f:
        reader = csv.DictReader(f)
        for registro in reader:
            dados_consolidados.append({
                'municipio': registro['Municipio'],
                'estado': registro['Estado'],
                'area_km2': float(registro['Area Km2']),
                'desmatado_2022': float(registro['Desmatado 2022']),
                'incremento_2021_2022': float(registro['Incremento 2021/2022']),
                'floresta_2022': float(registro['Floresta 2022'])
            })

    # Ler dados do TXT
    with open(arquivo_txt, 'r') as f:
        for linha in f:
            municipio, estado, area_km2, desmatado_2022, incremento, floresta_2022 = linha.strip().split(';')
            dados_consolidados.append({
                'municipio': municipio,
                'estado': estado,
                'area_km2': float(area_km2),
                'desmatado_2022': float(desmatado_2022),
                'incremento_2021_2022': float(incremento),
                'floresta_2022': float(floresta_2022)
            })

    return dados_consolidados

# Exemplo de uso
arquivo_json = 'dados_desmatamento_amazonia.json'
arquivo_csv = 'dados_desmatamento_amazonia.csv'
arquivo_txt = 'dados_desmatamento_amazonia.txt'

dados = ler_e_consolidar_dados(arquivo_json, arquivo_csv, arquivo_txt)
df_consolidado = pd.DataFrame(dados)

# Exibir os primeiros registros
print(df_consolidado.head())
