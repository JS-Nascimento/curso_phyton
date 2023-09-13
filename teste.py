import csv
import random
import os

# Lista de palavras-chave para criar nomes de ativos mais realistas
palavras_chave = ['Desktop', 'Laptop', 'Servidor', 'HD', 'SSD', 'Memória', 'Monitor', 'Mouse', 'Teclado', 'Impressora',
                  'Scanner', 'Roteador', 'Switch', 'Projetor']


# Função para criar registros aleatórios de ativos
def criar_registros_de_ativos():
    departamentos = {
        '1': 'RH',
        '2': 'TI',
        '3': 'Financeiro',
        '4': 'Operações',
        '5': 'Marketing',
    }

    ativos_inventariados = [['ID', 'Nome do Ativo', 'Departamento_ID', 'Ativo']]

    for i in range(1, 21):  # Criar pelo menos 20 registros
        ativo_id = str(i)
        nome_ativo = f'{random.choice(palavras_chave)} {i}'
        departamento_id = str(random.choice(list(departamentos.keys())))
        esta_ativo = random.choice(['Sim', 'Não'])  # Adiciona se o ativo está ativo ou não

        ativos_inventariados.append([ativo_id, nome_ativo, departamento_id, esta_ativo])

    with open('ativos_inventariados.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(ativos_inventariados)


# Chame a função para criar os registros de ativos
criar_registros_de_ativos()
