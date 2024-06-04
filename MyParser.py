import os
import csv
import xml.etree.ElementTree as ET
import zipfile
import time

pasta_base = (r'D:\Dowloads\mestres-e-doutores-completo')
saida_csv = 'resultados.csv'

# Função para obter o ano de conclusão do mestrado ou doutorado
def obter_ano_conclusao(formacao):
    if formacao is not None and formacao.attrib['STATUS-DO-CURSO'] == 'CONCLUIDO':
        ano_conclusao = formacao.get("ANO-DE-CONCLUSAO")
        return ano_conclusao
    return ''

# Função para obter o codigo do curso do mestrado ou doutorado
def obter_codigo_curso(formacao):
    if formacao is not None and formacao.attrib['STATUS-DO-CURSO'] == 'CONCLUIDO':
        codigo_curso = formacao.get("CODIGO-CURSO")
        return codigo_curso
    return ''

# Função para obter a grande area do mestrado ou doutorado em areas-do-conhecimento
def obter_grande_area_0(formacao):
    if formacao.find('AREAS-DO-CONHECIMENTO') is not None and formacao.attrib['STATUS-DO-CURSO'] == 'CONCLUIDO':
        for area_conhecimento in formacao.find('AREAS-DO-CONHECIMENTO'):
            grande_area = area_conhecimento.get("NOME-GRANDE-AREA-DO-CONHECIMENTO")
            return grande_area
    return ''

# Função para obter a area do mestrado ou doutorado em areas-do-conhecimento
def obter_area_conhecimento_0(formacao):
    if formacao.find('AREAS-DO-CONHECIMENTO') is not None and formacao.attrib['STATUS-DO-CURSO'] == 'CONCLUIDO':
        for area_conhecimento in formacao.find('AREAS-DO-CONHECIMENTO'):
            area_do_conhecimento = area_conhecimento.get("NOME-DA-AREA-DO-CONHECIMENTO")
            return area_do_conhecimento
    return ''

# Função para obter a grande area do mestrado ou doutorado em dados-complementares atraves do codigo curso
def obter_grande_area_1(formacao, codigo_curso):
    codigo_curso_atual = formacao.get("CODIGO-CURSO")
    if codigo_curso_atual in codigo_curso:
        grande_area = formacao.get("NOME-GRANDE-AREA-DO-CONHECIMENTO")
        return grande_area
    return ''

# Função para obter a area do mestrado ou doutorado em dados-complementares atraves do codigo curso
def obter_area_conhecimento_1(formacao, codigo_curso):
    codigo_curso_atual = formacao.get("CODIGO-CURSO")
    if codigo_curso_atual in codigo_curso:
        area_conhecimento = formacao.get("NOME-DA-AREA-DO-CONHECIMENTO")
        return area_conhecimento
    return ''

# Formatando os dados
def convert(s):
    return [element for element in s if element]
                         
# Registra o tempo de início
tempo_inicio = time.time()

# Lista para armazenar os resultados
resultados = []

# Iterar sobre as pastas 00, 01, 02, etc.
for subpasta in os.listdir(pasta_base):
    subpasta_caminho = os.path.join(pasta_base, subpasta)

    # Verificar se é uma subpasta
    if os.path.isdir(subpasta_caminho):
        
        # Iterar sobre os arquivos zip na subpasta
        for arquivo_zip in os.listdir(subpasta_caminho):
            if arquivo_zip.endswith(".zip"):
                caminho_zip = os.path.join(subpasta_caminho, arquivo_zip)

                # Extrair o conteúdo do arquivo zip
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    zip_ref.extractall(subpasta_caminho)

                # Iterar sobre os arquivos XML extraídos
                for arquivo_xml in os.listdir(subpasta_caminho):
                    if arquivo_xml.endswith(".xml"):
                        caminho_arquivo = os.path.join(subpasta_caminho, arquivo_xml)

                        try: 
                            # Parse do XML
                            tree = ET.parse(caminho_arquivo)
                            root = tree.getroot()

                            # Encontrar todos os elementos 'MESTRADO' e 'DOUTORADO'
                            mestrados = root.findall(".//MESTRADO") or root.findall(".//MESTRADO-PROFISSIONALIZANTE")
                            doutorados = root.findall(".//DOUTORADO")
                            areas = root.findall(".//INFORMACAO-ADICIONAL-CURSO")

                            # Extraindo os dados das conclusões mestrado
                            anos_mestrado = set([obter_ano_conclusao(m) for m in mestrados])
                            codigo_curso_mestrado = set([obter_codigo_curso(m) for m in mestrados])
                            grande_area_mestrado_0 = set([obter_grande_area_0(m) for m in mestrados])
                            area_conhecimento_mestrado_0 = set([obter_area_conhecimento_0(m) for m in mestrados])
                            grande_area_mestrado_1 = set([obter_grande_area_1(a, codigo_curso_mestrado) for a in areas])
                            area_conhecimento_mestrado_1 = set([obter_area_conhecimento_1(a, codigo_curso_mestrado) for a in areas])
                            
                            # Extraindo os dados das conclusões doutorado
                            anos_doutorado = set([obter_ano_conclusao(d) for d in doutorados])
                            codigo_curso_doutorado = set([obter_codigo_curso(d) for d in doutorados])
                            grande_area_doutorado_0 = set([obter_grande_area_0(d) for d in doutorados])
                            area_conhecimento_doutorado_0 = set([obter_area_conhecimento_0(d) for d in doutorados])
                            grande_area_doutorado_1 = set([obter_grande_area_1(a, codigo_curso_doutorado) for a in areas])
                            area_conhecimento_doutorado_1 = set([obter_area_conhecimento_1(a, codigo_curso_doutorado) for a in areas])

                            # Juntando os dois jeitos de pegar areas
                            if grande_area_mestrado_1 == {''} or ((grande_area_mestrado_1 == {'', 'OUTROS'} or grande_area_mestrado_1 == {'OUTROS'}) and grande_area_mestrado_0 != {''}):
                                grande_area_mestrado = grande_area_mestrado_0
                            else:
                                grande_area_mestrado = grande_area_mestrado_1
                            if area_conhecimento_mestrado_1 == {''}:
                                area_conhecimento_mestrado = area_conhecimento_mestrado_0
                            else:
                                area_conhecimento_mestrado = area_conhecimento_mestrado_1
                            if grande_area_doutorado_1 == {''} or ((grande_area_doutorado_1 == {'', 'OUTROS'} or grande_area_doutorado_1 == {'OUTROS'}) and grande_area_doutorado_0 != {''}):
                                grande_area_doutorado = grande_area_doutorado_0
                            else:
                                grande_area_doutorado = grande_area_doutorado_1
                            if area_conhecimento_doutorado_1 == {''}:
                                area_conhecimento_doutorado =   area_conhecimento_doutorado_0
                            else:
                                area_conhecimento_doutorado = area_conhecimento_doutorado_1

                            # Adicionar os resultados à lista
                            resultados.append({
                                'arquivo': arquivo_xml,
                                'anos_mestrado': convert(anos_mestrado),
                                'grande_area_mestrado': convert(grande_area_mestrado),
                                'area_conhecimento_mestrado': convert(area_conhecimento_mestrado),
                                'anos_doutorado': convert(anos_doutorado),
                                'grande_area_doutorado': convert(grande_area_doutorado),
                                'area_conhecimento_doutorado': convert(area_conhecimento_doutorado)
                            })

                            # Remover o arquivo XML após processar (opcional)
                            os.remove(caminho_arquivo)
                        
                        except ET.ParseError as e:
                            print(f"Erro ao analisar o arquivo XML: {e}")

# Escrever os resultados em um arquivo CSV
with open(saida_csv, 'w', newline='', encoding='utf-8') as csv_file:
    campos = ['arquivo', 'anos_mestrado', 'grande_area_mestrado', 'area_conhecimento_mestrado', 'anos_doutorado', 'grande_area_doutorado', 'area_conhecimento_doutorado']
    writer = csv.DictWriter(csv_file, fieldnames=campos)

    # Escrever o cabeçalho
    writer.writeheader()

    # Escrever os dados
    writer.writerows(resultados)

# Registra o tempo de término
tempo_fim = time.time()

# Calcula o tempo de execução
tempo_execucao = tempo_fim - tempo_inicio

print(f"Tempo de execução: {tempo_execucao} segundos")
print(f'Os resultados foram salvos em {saida_csv}')