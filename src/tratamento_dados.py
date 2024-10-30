import pandas as pd

def tratar_dados_json(df):
    # Exemplo: Converter colunas de desmatamento e área para float
    df['area_km2'] = pd.to_numeric(df['area_km2'], errors='coerce').fillna(0).astype('float64')
    df['desmatado_2022'] = pd.to_numeric(df['desmatado_2022'], errors='coerce').fillna(0).astype('float64')
    df['incremento_2021_2022'] = pd.to_numeric(df['incremento_2021_2022'], errors='coerce').fillna(0).astype('float64')
    df['floresta_2022'] = pd.to_numeric(df['floresta_2022'], errors='coerce').fillna(0).astype('float64')
    
    return df

def tratar_dados_csv(df):
    # Exemplo: Tratar colunas do CSV
    df['Area Km2'] = pd.to_numeric(df['Area Km2'], errors='coerce').fillna(0).astype('float64')
    df['Desmatado 2022'] = pd.to_numeric(df['Desmatado 2022'], errors='coerce').fillna(0).astype('float64')
    df['Incremento 2021/2022'] = pd.to_numeric(df['Incremento 2021/2022'], errors='coerce').fillna(0).astype('float64')
    df['Floresta 2022'] = pd.to_numeric(df['Floresta 2022'], errors='coerce').fillna(0).astype('float64')
    
    return df

def tratar_dados_txt(df):
    # Exemplo: Tratar colunas do TXT
    df['area_km2'] = pd.to_numeric(df['area_km2'], errors='coerce').fillna(0).astype('float64')
    df['desmatado_2022'] = pd.to_numeric(df['desmatado_2022'], errors='coerce').fillna(0).astype('float64')
    df['incremento_2021_2022'] = pd.to_numeric(df['incremento_2021_2022'], errors='coerce').fillna(0).astype('float64')
    df['floresta_2022'] = pd.to_numeric(df['floresta_2022'], errors='coerce').fillna(0).astype('float64')
    
    return df
