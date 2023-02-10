import translators as ts
import translators.server as tss
import json

# Inicialize o tradutor
from_language, to_language = 'en', 'pt'

# Dicionário para armazenar as traduções
translated_values = {}

# Função para carregar um arquivo JSON
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Função para salvar o dicionário como um arquivo JSON
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Carregue o arquivo JSON
json_data = load_json('en.json')

# Loop para traduzir cada value do JSON
count = 1
total = len(json_data)
for key, value in json_data.items():
    translated_value = tss.google(value, from_language, to_language)
    translated_values[key] = translated_value
    print(f'{count} of {total} entries translated')
    count += 1

# Salve o dicionário como um arquivo JSON
save_json('translated.json', translated_values)
