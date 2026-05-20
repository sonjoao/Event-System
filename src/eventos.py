import csv
from datetime import datetime

arquivo = "eventos.csv"

def cadastrar_evento():

    print("\nCadastro de Evento")

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    data = input("Data (dd/mm/aaaa): ")
    local = input("Local: ")

    with open(arquivo, "a", newline="", encoding="utf-8") as arq:

        escritor = csv.writer(arq)

        escritor.writerow([
            nome,
            tipo,
            data,
            local
        ])

    print("\nEvento cadastrado")

def listar_eventos():

    print("\nLista de Eventos")

    try:

        with open(arquivo, "r", encoding="utf-8") as arq:

            leitor = csv.reader(arq)

            vazio = True

            for i, linha in enumerate(leitor):

                vazio = False

                nome = linha[0]
                tipo = linha[1]
                data = linha[2]
                local = linha[3]

                try:

                    data_evento = datetime.strptime(data, "%d/%m/%Y")

                    hoje = datetime.now()

                    dias = (data_evento - hoje).days

                except ValueError:
                    dias = "erro na data"

                print(f"""
Evento {i}

Nome: {nome}
Tipo: {tipo}
Data: {data}
Local: {local}

Faltam {dias} dias
                """)

            if vazio:
                print("Nenhum evento cadastrado")

    except FileNotFoundError:
        print("Arquivo não encontrado")

def editar_evento():

    eventos = []

    try:

        with open(arquivo, "r", encoding="utf-8") as arq:

            leitor = csv.reader(arq)

            for linha in leitor:
                eventos.append(linha)

    except FileNotFoundError:
        print("Erro ao abrir arquivo")
        return

    listar_eventos()

    try:

        indice = int(input("\nDigite o número do evento: "))

        if indice < 0 or indice >= len(eventos):
            print("Evento não encontrado")
            return

    except ValueError:
        print("Valor inválido")
        return

    print("\nNovos dados")

    eventos[indice][0] = input("Novo nome: ")
    eventos[indice][1] = input("Novo tipo: ")
    eventos[indice][2] = input("Nova data: ")
    eventos[indice][3] = input("Novo local: ")

    with open(arquivo, "w", newline="", encoding="utf-8") as arq:

        escritor = csv.writer(arq)

        escritor.writerows(eventos)

    print("\nEvento atualizado")

def excluir_evento():

    eventos = []

    try:

        with open(arquivo, "r", encoding="utf-8") as arq:

            leitor = csv.reader(arq)

            for linha in leitor:
                eventos.append(linha)

    except FileNotFoundError:
        print("Erro ao abrir arquivo")
        return

    listar_eventos()

    try:

        indice = int(input("\nNúmero do evento para excluir: "))

        if indice < 0 or indice >= len(eventos):
            print("Evento não encontrado")
            return

    except ValueError:
        print("Valor inválido")
        return

    eventos.pop(indice)

    with open(arquivo, "w", newline="", encoding="utf-8") as arq:

        escritor = csv.writer(arq)

        escritor.writerows(eventos)

    print("\nEvento removido")
