import requests
import re
import pandas as pd
import os

# URL do site a ser raspado
url = "https://pastebin.com/raw/xjCDscZk"

# Fazer a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Verificar se a requisição foi bem-sucedida

# Conteúdo do texto
data = response.text

# Expressão regular para extrair os dados
pattern = re.compile(r"(.+?) - CNPJ: (.+?) - Telefone: (.+?) - Ramo: (.+)")

# Inicializar listas para armazenar os dados
empresas = []
cnpjs = []
telefones = []
ramos = []
statuses = []  # Nova lista para status

# Encontrar todas as correspondências no texto
for match in pattern.findall(data):
    empresas.append(match[0].strip())
    cnpjs.append(match[1].strip())
    telefones.append(match[2].strip())
    ramos.append(match[3].strip())
    statuses.append("Ativo") 

# Criar um DataFrame com os dados raspados
df = pd.DataFrame({
    'EMPRESA': empresas,
    'CNPJ': cnpjs,
    'TELEFONE': telefones,
    'RAMO': ramos,
    'STATUS': statuses  # Adicionar coluna de status
})

# Nome do arquivo Excel
file_name = 'dados_empresas.xlsx'

# Salvar o DataFrame em um arquivo Excel, substituindo se o arquivo já existir
df.to_excel(file_name, index=False)

print(f"Dados raspados e salvos em '{file_name}'")
