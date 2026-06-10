

from src.arquivos import ler_arquivo
from src.eventos import listar_eventos, buscar_evento_por_id

ARQUIVO_TAREFAS = "dados/tarefas.txt"


def calcular_gastos_evento(id_evento):
    
    tarefas = ler_arquivo(ARQUIVO_TAREFAS)

    total_gasto = 0

    for tarefa in tarefas:
        dados = tarefa.split(";")

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

    # índices: 0=id, 1=nome, 2=tipo, 3=data, 4=horario, 5=local, 6=orcamento, 7=convidados
    orcamento = float(dados[6])

    
    total_gasto = calcular_gastos_evento(id_evento)

    saldo = orcamento - total_gasto

    print("\nResumo do orçamento")
    print("-" * 40)
    print(f"Evento: {dados[1]}")
    print(f"Orçamento disponível: R$ {orcamento:.2f}")
    print(f"Total gasto em tarefas: R$ {total_gasto:.2f}")
    print(f"Saldo restante: R$ {saldo:.2f}")

    if saldo < 0:
        print("Atenção: o evento passou do orçamento.")
    elif saldo == 0:
        print("O orçamento foi usado exatamente.")
    else:
        print("Ainda existe dinheiro disponível no orçamento.")
