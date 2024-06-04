import pandas as pd

# Carregar o CSV para um DataFrame do pandas
df = pd.read_csv('resultados.csv')

# Remover colchetes e aspas simples das strings nas colunas
df = df.apply(lambda x: x.str.strip("[]'") if x.dtype == "object" else x)

# Agrupar pelos campos 'grande_area_mestrado' e 'area_conhecimento_mestrado' e contar as ocorrências
contagem_mestrado = df.groupby(['grande_area_mestrado', 'area_conhecimento_mestrado']).size().reset_index(name='contagem_mestrado')

# Agrupar pelos campos 'grande_area_doutorado' e 'area_conhecimento_doutorado' e contar as ocorrências
contagem_doutorado = df.groupby(['grande_area_doutorado', 'area_conhecimento_doutorado']).size().reset_index(name='contagem_doutorado')

print("Contagem para Mestrado:")
print(contagem_mestrado)

#print("\nContagem para Doutorado:")
#print(contagem_doutorado)

'''
# Preencher valores nulos com uma string vazia
df_mestrado[criterio_mestrado] = df_mestrado[criterio_mestrado].fillna('')
df_doutorado[criterio_doutorado] = df_doutorado[criterio_doutorado].fillna('')

# Filtrar as linhas com valores vazios ou não numéricos
df_mestrado = df_mestrado[df_mestrado[criterio_mestrado].str.isdigit()]
df_doutorado = df_doutorado[df_doutorado[criterio_doutorado].str.isdigit()]

# Converter as strings de anos para inteiros
df_mestrado[criterio_mestrado] = df_mestrado[criterio_mestrado].astype(int)
df_doutorado[criterio_doutorado] = df_doutorado[criterio_doutorado].astype(int)

# Filtrar os dados entre os anos de 1942 e 2024
df_mestrado = df_mestrado[df_mestrado[criterio_mestrado].between(1942, 2024)]
df_doutorado = df_doutorado[df_doutorado[criterio_doutorado].between(1942, 2024)]

# Agrupar por ano e calcular a soma
result_mestrado = df_mestrado.groupby(criterio_mestrado).agg({'mestrado': 'sum'}).reset_index()
result_doutorado = df_doutorado.groupby(criterio_doutorado).agg({'doutorado': 'sum'}).reset_index()

# Combinar os resultados de mestrado e doutorado em um único DataFrame
result_combined = result_mestrado.merge(result_doutorado, left_on=criterio_mestrado, right_on=criterio_doutorado, how='outer')
result_combined['ano'] = result_combined[criterio_mestrado].fillna(result_combined[criterio_doutorado])
result_combined.drop([criterio_mestrado, criterio_doutorado], axis=1, inplace=True)
result_combined.fillna(0, inplace=True)

# Converter para o formato de lista de dicionários para salvar como JSON
data_combined = result_combined.to_dict(orient='records')

# Remover as aspas duplas em torno dos valores do ano
for entry in data_combined:
    if entry['ano']:
        entry['ano'] = int(entry['ano'])
    
# Salvar os resultados em um arquivo JSON
with open('dados_completos.json', 'w') as f:
    json.dump(data_combined, f, indent=2)

print("Resultados combinados salvos em JSON com sucesso!")
'''