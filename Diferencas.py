import pandas as pd

# Carregar os arquivos CSV para dataframes
df1 = pd.read_csv('resultados copy.csv')
df2 = pd.read_csv('resultados.csv')

# Encontrar as diferenças entre os dataframes
diferencas = pd.concat([df1, df2]).drop_duplicates(keep=False)

# Salvar as diferenças em um novo arquivo CSV
diferencas.to_csv('diferencas.csv', index=False)
