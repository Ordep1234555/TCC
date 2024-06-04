import pandas as pd
import ast

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv('resultados.csv')

# Criar dicionário para armazenar as áreas de conhecimento para cada grande área
areas_por_grande_area = {}

# Iterar sobre as linhas do DataFrame
for index, row in df.iterrows():
    grande_area_mestrado = ast.literal_eval(row['grande_area_mestrado'])
    area_conhecimento_mestrado = ast.literal_eval(row['area_conhecimento_mestrado'])
    grande_area_doutorado = ast.literal_eval(row['grande_area_doutorado'])
    area_conhecimento_doutorado = ast.literal_eval(row['area_conhecimento_doutorado'])
    
    # Verificar se há apenas uma grande área e uma área de conhecimento associada para mestrado
    if len(grande_area_mestrado) == 1 and len(area_conhecimento_mestrado) == 1:
        if grande_area_mestrado[0] not in areas_por_grande_area:
            areas_por_grande_area[grande_area_mestrado[0]] = {}
        if area_conhecimento_mestrado[0] not in areas_por_grande_area[grande_area_mestrado[0]]:
            areas_por_grande_area[grande_area_mestrado[0]][area_conhecimento_mestrado[0]] = 0
        areas_por_grande_area[grande_area_mestrado[0]][area_conhecimento_mestrado[0]] += 1
    
    # Verificar se há apenas uma grande área e uma área de conhecimento associada para doutorado
    if len(grande_area_doutorado) == 1 and len(area_conhecimento_doutorado) == 1:
        if grande_area_doutorado[0] not in areas_por_grande_area:
            areas_por_grande_area[grande_area_doutorado[0]] = {}
        if area_conhecimento_doutorado[0] not in areas_por_grande_area[grande_area_doutorado[0]]:
            areas_por_grande_area[grande_area_doutorado[0]][area_conhecimento_doutorado[0]] = 0
        areas_por_grande_area[grande_area_doutorado[0]][area_conhecimento_doutorado[0]] += 1

# Filtrar as áreas que ocorrem pelo menos 5 vezes com uma grande área específica
filtered_areas_por_grande_area = {}
for grande_area, areas_conhecimento in areas_por_grande_area.items():
    filtered_areas_por_grande_area[grande_area] = [area for area, count in areas_conhecimento.items() if count >= 5]

# Salvar as áreas de conhecimento filtradas para cada grande área em um arquivo de texto
with open('areas_por_grande_area_filtradas.txt', 'w') as file:
    for grande_area, areas_conhecimento in filtered_areas_por_grande_area.items():
        file.write(f"Grande Área: {grande_area}\n")
        file.write(f"Áreas de Conhecimento: {', '.join(areas_conhecimento)}\n\n")
