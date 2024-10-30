# Usando a imagem oficial do Python como base
FROM python:3.10

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do projeto para o diretório de trabalho do container
COPY . /app

# Instalando as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar o seu script main.py
CMD ["python", "src/main.py"]
