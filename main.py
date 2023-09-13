import csv
import os
import random


# Função para criar arquivos CSV
def criar_arquivos():
    usuarios = [
        ['ID', 'Nome', 'Departamento_ID'],
        ['1', 'Alice', '1'],
        ['2', 'Bob', '2'],
        ['3', 'Charlie', '3'],
        ['4', 'David', '4'],
        ['5', 'Eva', '5'],
        ['6', 'Frank', '1'],
        ['7', 'Grace', '2'],
        ['8', 'Hannah', '3'],
        ['9', 'Ivan', '4'],
        ['10', 'Jack', '5'],
        ['11', 'Karen', '1'],
        ['12', 'Liam', '2'],
        ['13', 'Mia', '3'],
        ['14', 'Nathan', '4'],
        ['15', 'Olivia', '5'],
    ]
    departamentos = [
        ['ID', 'Nome'],
        ['1', 'RH'],
        ['2', 'TI'],
        ['3', 'Financeiro'],
        ['4', 'Operações'],
        ['5', 'Marketing'],
    ]
    chamados = [
        ['ID', 'Descrição', 'Prioridade', 'Usuário_ID', 'Departamento_ID'],
        ['1', 'Problema com e-mail', 'Baixa', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['2', 'Impressora não funciona', 'Normal', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['3', 'Falha na rede', 'Alta', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['4', 'Software não inicia', 'Baixa', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['5', 'Acesso negado ao servidor', 'Normal', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['6', 'Erro no banco de dados', 'Alta', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['7', 'Sistema lento', 'Baixa', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['8', 'Não consegue fazer login', 'Normal', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['9', 'Problema no backup', 'Alta', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))],
        ['10', 'Falha na conexão VPN', 'Normal', str(random.choice(range(1, 16))), str(random.choice(range(1, 6)))]
    ]
    # salvando arquivos csv
    with open('chamados.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(chamados)

    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(usuarios)

    with open('departamentos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(departamentos)

# relatórios do tp
def usuarios_por_departamento():
    departamentos = {}
    with open('departamentos.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            departamentos[row[0]] = row[1]

    usuarios_departamentos = []
    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            departamento_nome = departamentos.get(row[2], "Desconhecido")
            usuarios_departamentos.append((departamento_nome, row[1]))

    # Ordenando alfabeticamente
    usuarios_departamentos.sort(key=lambda x: x[0])

    for dep, nome in usuarios_departamentos:
        print(f'Departamento: {dep} - Usuário: {nome}')
def chamados_por_prioridade():
    prioridades = {'Baixa': [], 'Normal': [], 'Alta': []}
    with open('chamados.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            prioridades[row[2]].append(row[1])

    for prioridade, chamados in prioridades.items():
        print(f'Prioridade: {prioridade}')
        for chamado in chamados:
            print(f'  - {chamado}')
def usuario_com_mais_chamados():
    usuarios = {}
    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            usuarios[row[0]] = row[1]

    chamados_por_usuario = {user: 0 for user in usuarios.keys()}
    with open('chamados.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            chamados_por_usuario[row[3]] += 1

    max_chamados_usuario = max(chamados_por_usuario, key=chamados_por_usuario.get)
    print(f'O usuário {usuarios[max_chamados_usuario]} abriu mais chamados, com {chamados_por_usuario[max_chamados_usuario]} chamados.')
def chamados_por_departamento():
    departamentos = {}
    with open('departamentos.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            departamentos[row[0]] = row[1]

    chamados_por_departamento = {dep: 0 for dep in departamentos.keys()}
    with open('chamados.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Ignorar a linha do cabeçalho
        for row in reader:
            chamados_por_departamento[row[4]] += 1

    for dep_id, quantidade in chamados_por_departamento.items():
        print(f'Departamento: {departamentos[dep_id]} - Quantidade de Chamados: {quantidade}')
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    while True:
        limpar_tela()
        print("Selecione uma opção:")
        print("1. Relação de todos os usuários por departamento em ordem alfabética")
        print("2. Relação de todos os chamados por grau de prioridade de atendimento")
        print("3. Quem foi o usuário que abriu mais chamados e em que quantidade?")
        print("4. Quantidade de chamados por departamento")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            usuarios_por_departamento()
        elif escolha == '2':
            chamados_por_prioridade()
        elif escolha == '3':
            usuario_com_mais_chamados()
        elif escolha == '4':
            chamados_por_departamento()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

        input("Pressione ENTER para continuar...")

# Criar arquivos CSV ao iniciar o programa

criar_arquivos()

# Exibir o menu
menu()

