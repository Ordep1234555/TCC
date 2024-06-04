import pandas as pd
import ast
import json

# Define a opção para exibir todas as linhas e colunas no terminal
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Carregar o CSV para um DataFrame
df = pd.read_csv('resultados.csv')

# Definindo parâmetros
criterio_mestrado = 'anos_mestrado'
criterio_doutorado = 'anos_doutorado'
grande_area_mestrado = 'grande_area_mestrado'
grande_area_doutorado = 'grande_area_doutorado'

# Converter as strings de listas para listas reais
df[criterio_mestrado] = df[criterio_mestrado].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])
df[criterio_doutorado] = df[criterio_doutorado].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])

# Explodir as listas para transformar em registros separados
df_mestrado = df.explode(criterio_mestrado)
df_doutorado = df.explode(criterio_doutorado)

# Preencher valores nulos com uma string vazia
df_mestrado[criterio_mestrado] = df_mestrado[criterio_mestrado].fillna('')
df_doutorado[criterio_doutorado] = df_doutorado[criterio_doutorado].fillna('')

# Filtrar as linhas com valores vazios ou não numéricos
df_mestrado = df_mestrado[df_mestrado[criterio_mestrado].str.isdigit()]
df_doutorado = df_doutorado[df_doutorado[criterio_doutorado].str.isdigit()]

# Converter as strings de anos para inteiros
df_mestrado[criterio_mestrado] = df_mestrado[criterio_mestrado].astype(int)
df_doutorado[criterio_doutorado] = df_doutorado[criterio_doutorado].astype(int)

# Filtrar os dados entre os anos de 1946 e 2024
df_mestrado = df_mestrado[df_mestrado[criterio_mestrado].between(1946, 2024)]
df_doutorado = df_doutorado[df_doutorado[criterio_doutorado].between(1946, 2024)]

# Contar o número de conclusões de mestrado por ano e grande área
result_mestrado = df_mestrado.groupby([criterio_mestrado, grande_area_mestrado]).size().reset_index(name='conclusoes_mestrado')

# Contar o número de conclusões de doutorado por ano e grande área
result_doutorado = df_doutorado.groupby([criterio_doutorado, grande_area_doutorado]).size().reset_index(name='conclusoes_doutorado')

# Renomear as colunas dos resultados para 'ano' e 'grande_area'
result_mestrado.rename(columns={criterio_mestrado: 'ano', grande_area_mestrado: 'grande_area'}, inplace=True)
result_doutorado.rename(columns={criterio_doutorado: 'ano', grande_area_doutorado: 'grande_area'}, inplace=True)

# Mesclar os resultados de mestrado e doutorado
result_combined = result_mestrado.merge(result_doutorado, on=['ano', 'grande_area'], how='outer').fillna(0)

# Converter para o formato de lista de dicionários para salvar como JSON
data_combined = result_combined.to_dict(orient='records')

# Salvar os resultados em um arquivo JSON
with open('dados_completos.json', 'w') as f:
    json.dump(data_combined, f, indent=2)

print("Resultados combinados salvos em JSON com sucesso!")
