import pandas as pd
from sqlalchemy import URL, create_engine

caminho_arquivo = 'resultados.csv'

# Carregue o CSV para um DataFrame
dados = pd.read_csv(caminho_arquivo)

# Crie uma conexão com o banco de dados SQLite
engine = create_engine('sqlite:///TCC.db')
'''
engine = create_engine('mysql://localhost/test')
URL.create(
    "mysql+mysqldb",
    username="root",
    password="_aduk3n_",
    host="localhost",
    database="st",
)
'''
# Fazer conexão com o SQL
# Pensar sobre

# Insira os dados no banco de dados
dados.to_sql('pesquisadores', engine, index=False, if_exists='replace')

# Confirme a transação
engine.dispose()

print("Dados inseridos no banco de dados.")
