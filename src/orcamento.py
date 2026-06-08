# orcamento.py
# Esse arquivo calcula o orçamento do evento.
# Ele soma o custo das tarefas e compara com o orçamento disponível.

from src.arquivos import ler_arquivo
from src.eventos import listar_eventos, buscar_evento_por_id

ARQUIVO_TAREFAS = "dados/tarefas.txt"


def calcular_gastos_evento(id_evento):
    # Lemos todas as tarefas cadastradas.
    tarefas = ler_arquivo(ARQUIVO_TAREFAS)

    # Essa variável começa em zero e vai acumulando os custos.
    total_gasto = 0

    for tarefa in tarefas:
        dados = tarefa.split(";")

        # Se a tarefa pertence ao evento informado, somamos seu custo.
        if dados[1] == str(id_evento):
            total_gasto += float(dados[3])

    return total_gasto


def mostrar_orcamento():
    print("\n=== Controle de Orçamento ===")

    listar_eventos()

    id_evento = input("\nDigite o ID do evento: ")
    evento = buscar_evento_por_id(id_evento)

    if evento is None:
        print("Evento não encontrado.")
        return

    dados = evento.split(";")

    # O orçamento do evento fica na posição 5 da linha salva.
    orcamento = float(dados[5])

    # Calculamos o total de gastos das tarefas desse evento.
    total_gasto = calcular_gastos_evento(id_evento)

    # O saldo é o que sobrou do orçamento.
    saldo = orcamento - total_gasto

    print("\nResumo do orçamento")
    print("-" * 40)
    print(f"Evento: {dados[1]}")
    print(f"Orçamento disponível: R$ {orcamento:.2f}")
    print(f"Total gasto em tarefas: R$ {total_gasto:.2f}")
    print(f"Saldo restante: R$ {saldo:.2f}")

    # Mensagens simples para ajudar o usuário a entender a situação.
    if saldo < 0:
        print("Atenção: o evento passou do orçamento.")
    elif saldo == 0:
        print("O orçamento foi usado exatamente.")
    else:
        print("Ainda existe dinheiro disponível no orçamento.")
