# eventos.py
# Esse arquivo cuida do CRUD de eventos.
# CRUD significa: criar, listar, editar e excluir.

from datetime import datetime
import src.arquivos

# Caminho onde os eventos serão salvos.
ARQUIVO_EVENTOS = "dados/eventos.txt"


def gerar_id_evento():
    # Lemos todos os eventos que já existem.
    eventos = src.arquivos.ler_arquivo(ARQUIVO_EVENTOS)

    # Se não tiver nenhum evento, o primeiro id será 1.
    if len(eventos) == 0:
        return 1

    # Pegamos o último evento da lista.
    ultimo_evento = eventos[-1]

    # O id fica antes do primeiro ponto e vírgula.
    ultimo_id = int(ultimo_evento.split(";")[0])

    # O próximo id é o último id + 1.
    return ultimo_id + 1


def data_valida(data):
    try:
        # Tentamos transformar a data digitada em uma data real.
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        # Se não conseguir, significa que a data está errada.
        return False


def criar_evento():
    print("\n=== Cadastro de Evento ===")

    # O id é gerado automaticamente para evitar repetição.
    id_evento = gerar_id_evento()

    # Pedimos as informações principais do evento.
    nome = input("Nome do evento: ")
    tipo = input("Tipo do evento: ")

    # Usamos repetição para obrigar o usuário a digitar uma data válida.
    while True:
        data = input("Data (dd/mm/aaaa): ")

        if data_valida(data):
            break
        else:
            print("Data inválida! Use o formato dd/mm/aaaa.")

    local = input("Local: ")

    # Tratamos orçamento para evitar erro caso o usuário digite texto.
    while True:
        try:
            orcamento = float(input("Orçamento disponível: R$ "))
            break
        except ValueError:
            print("Digite apenas números no orçamento.")

    # Tratamos convidados para garantir que seja um número inteiro.
    while True:
        try:
            convidados = int(input("Quantidade de convidados: "))
            break
        except ValueError:
            print("Digite apenas números inteiros em convidados.")

    # Juntamos tudo em uma linha, separado por ponto e vírgula.
    linha = f"{id_evento};{nome};{tipo};{data};{local};{orcamento};{convidados}"

    # Salvamos essa linha no arquivo de eventos.
    src.arquivos.adicionar_linha(ARQUIVO_EVENTOS, linha)

    print("\nEvento cadastrado com sucesso!")


def listar_eventos():
    print("\n=== Lista de Eventos ===")

    # Lemos os eventos salvos no arquivo.
    eventos = src.arquivos.ler_arquivo(ARQUIVO_EVENTOS)

    # Se não tiver evento, mostramos uma mensagem simples.
    if len(eventos) == 0:
        print("Nenhum evento cadastrado ainda.")
        return

    # Passamos por todos os eventos para mostrar de forma organizada.
    for evento in eventos:
        dados = evento.split(";")

        print("-" * 40)
        print(f"ID: {dados[0]}")
        print(f"Nome: {dados[1]}")
        print(f"Tipo: {dados[2]}")
        print(f"Data: {dados[3]}")
        print(f"Local: {dados[4]}")
        print(f"Orçamento: R$ {float(dados[5]):.2f}")
        print(f"Convidados: {dados[6]}")


def buscar_evento_por_id(id_procurado):
    # Lemos todos os eventos.
    eventos = src.arquivos.ler_arquivo(ARQUIVO_EVENTOS)

    # Procuramos um evento com o id informado.
    for evento in eventos:
        dados = evento.split(";")

        if dados[0] == str(id_procurado):
            return evento

    # Se não encontrar, retornamos None.
    return None


def editar_evento():
    print("\n=== Editar Evento ===")

    listar_eventos()

    id_editar = input("\nDigite o ID do evento que deseja editar: ")

    eventos = src.arquivos.ler_arquivo(ARQUIVO_EVENTOS)
    novos_eventos = []
    encontrado = False

    for evento in eventos:
        dados = evento.split(";")

        if dados[0] == id_editar:
            encontrado = True

            print("\nDeixe em branco para manter o valor atual.")

            novo_nome = input(f"Novo nome ({dados[1]}): ")
            novo_tipo = input(f"Novo tipo ({dados[2]}): ")
            nova_data = input(f"Nova data ({dados[3]}): ")
            novo_local = input(f"Novo local ({dados[4]}): ")
            novo_orcamento = input(f"Novo orçamento ({dados[5]}): ")
            novos_convidados = input(f"Novos convidados ({dados[6]}): ")

            # Se o usuário não digitar nada, o valor antigo continua.
            if novo_nome == "":
                novo_nome = dados[1]
            if novo_tipo == "":
                novo_tipo = dados[2]
            if nova_data == "":
                nova_data = dados[3]
            if novo_local == "":
                novo_local = dados[4]
            if novo_orcamento == "":
                novo_orcamento = dados[5]
            if novos_convidados == "":
                novos_convidados = dados[6]

            # Montamos a linha atualizada.
            evento_atualizado = f"{dados[0]};{novo_nome};{novo_tipo};{nova_data};{novo_local};{novo_orcamento};{novos_convidados}"
            novos_eventos.append(evento_atualizado)
        else:
            # Eventos que não foram editados continuam iguais.
            novos_eventos.append(evento)

    # Salvamos a lista atualizada no arquivo.
    src.arquivos.salvar_arquivo(ARQUIVO_EVENTOS, novos_eventos)

    if encontrado:
        print("\nEvento editado com sucesso!")
    else:
        print("\nEvento não encontrado.")


def excluir_evento():
    print("\n=== Excluir Evento ===")

    listar_eventos()

    id_excluir = input("\nDigite o ID do evento que deseja excluir: ")

    eventos = src.arquivos.ler_arquivo(ARQUIVO_EVENTOS)
    novos_eventos = []
    encontrado = False

    for evento in eventos:
        dados = evento.split(";")

        if dados[0] == id_excluir:
            encontrado = True
        else:
            novos_eventos.append(evento)

    src.arquivos.salvar_arquivo(ARQUIVO_EVENTOS, novos_eventos)

    if encontrado:
        print("\nEvento excluído com sucesso!")
    else:
        print("\nEvento não encontrado.")
