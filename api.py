from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/chamados_por_departamento")
async def get_chamados_por_departamento():
    # Função para calcular os chamados por departamento
    def calcular_chamados_por_departamento():
        departamentos = {}
        with open('departamentos.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Ignorar a linha do cabeçalho
            for row in reader:
                departamentos[row[0]] = row[1]

        chamados_por_departamento = {dep: 0 for dep in departamentos.keys()}
        with open('chamados.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Ignorar a linha do cabeçalho
            for row in reader:
                chamados_por_departamento[row[4]] += 1

        result = []
        for dep_id, quantidade in chamados_por_departamento.items():
            result.append({"Departamento": departamentos[dep_id], "Quantidade de Chamados": quantidade})
        return result

    return calcular_chamados_por_departamento()

@app.get("/usuarios_por_departamento")
async def get_usuarios_por_departamento():
    departamentos = {}
    with open('departamentos.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar a linha do cabeçalho
        for row in reader:
            departamentos[row[0]] = row[1]

    usuarios_departamentos = []
    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar a linha do cabeçalho
        for row in reader:
            departamento_nome = departamentos.get(row[2], "Desconhecido")
            usuarios_departamentos.append({"Departamento": departamento_nome, "Usuário": row[1]})

    # Ordenando alfabeticamente
    usuarios_departamentos.sort(key=lambda x: x["Departamento"])

    return usuarios_departamentos

@app.get("/chamados_por_prioridade")
async def get_chamados_por_prioridade():
    prioridades = {'Baixa': [], 'Normal': [], 'Alta': []}
    with open('chamados.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar a linha do cabeçalho
        for row in reader:
            prioridades[row[2]].append(row[1])

    result = []
    for prioridade, chamados in prioridades.items():
        chamados_por_prioridade = {"Prioridade": prioridade, "Chamados": chamados}
        result.append(chamados_por_prioridade)

    return result

@app.get("/chamados_com_usuarios")
async def get_chamados_com_usuarios():
    chamados_com_usuarios = []

    # Lê os dados dos arquivos CSV
    with open('chamados.csv', 'r') as chamados_file:
        chamados_reader = csv.reader(chamados_file)
        next(chamados_reader)  # Ignora a linha do cabeçalho
        chamados = {row[0]: {"Descrição": row[1], "Prioridade": row[2], "Usuário_ID": row[3]} for row in chamados_reader}

    with open('usuarios.csv', 'r') as usuarios_file:
        usuarios_reader = csv.reader(usuarios_file)
        next(usuarios_reader)  # Ignora a linha do cabeçalho
        usuarios = {row[0]: row[1] for row in usuarios_reader}

    # Combina os dados dos chamados com os nomes dos usuários
    for chamado_id, chamado_data in chamados.items():
        usuario_nome = usuarios.get(chamado_data["Usuário_ID"], "Desconhecido")
        chamado_com_usuario = {
            "ID do Chamado": chamado_id,
            "Descrição": chamado_data["Descrição"],
            "Prioridade": chamado_data["Prioridade"],
            "Nome do Usuário": usuario_nome
        }
        chamados_com_usuarios.append(chamado_com_usuario)

    return chamados_com_usuarios

app = FastAPI()

@app.get("/chamados_por_prioridade")
async def get_chamados_por_prioridade():
    prioridades = {'Baixa': [], 'Normal': [], 'Alta': []}
    with open('chamados.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Lê o cabeçalho
        for row in reader:
            chamado = {
                "Descrição": row[1],
                "Prioridade": row[2],
                "Situação": row[5],  # Adicione a coluna "Situação"
                "Data de Abertura": row[6]  # Adicione a coluna "Data de Abertura"
            }
            prioridades[row[2]].append(chamado)

    result = []
    for prioridade, chamados in prioridades.items():
        chamados_por_prioridade = {"Prioridade": prioridade, "Chamados": chamados}
        result.append(chamados_por_prioridade)

    return result
@app.get("/ativos_inventariados")
async def get_ativos_inventariados():
    ativos_inventariados = []

    # Lê os dados do arquivo CSV de ativos inventariados
    with open('ativos_inventariados.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Lê o cabeçalho
        for row in reader:
            ativo = {
                "Nome do Ativo": row[1],
                "Departamento_ID": row[2],
                "Nome do Departamento": ""  # Adicione a coluna para o nome do departamento
            }
            ativos_inventariados.append(ativo)

    # Lê os dados do arquivo CSV de departamentos
    with open('departamentos.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Lê o cabeçalho
        departamentos = {row[0]: row[1] for row in reader}

    # Atualiza o nome do departamento para cada ativo
    for ativo in ativos_inventariados:
        departamento_id = ativo["Departamento_ID"]
        departamento_nome = departamentos.get(departamento_id, "Desconhecido")
        ativo["Nome do Departamento"] = departamento_nome

    return ativos_inventariados

