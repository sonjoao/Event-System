

from datetime import datetime
from src.eventos import listar_eventos, buscar_evento_por_id
from src.tarefas import listar_tarefas_por_evento
from src.orcamento import calcular_gastos_evento


def _exibir_checklist(id_evento, nome_evento, dias):
    """Exibe o checklist final quando falta 1 dia ou menos para o evento."""

    print("\n" + "=" * 60)
    print("  MODO EVENTO ATIVADO  ".center(60))
    print("=" * 60)

    if dias == 1:
        print(f"\n  O evento '{nome_evento}' é HOJE!")
    else:
        print(f"\n  O evento '{nome_evento}' é AMANHÃ!")

    print("\n--- CHECKLIST FINAL ---\n")
    print("[ ] Confirmar presença dos convidados")
    print("[ ] Verificar local do evento")
    print("[ ] Conferir materiais e equipamentos")
    print("[ ] Revisar horários da programação")
    print("[ ] Verificar buffet / alimentação")
    print("[ ] Confirmar fornecedores")
    print("[ ] Últimos ajustes de decoração")
    print("[ ] Checar plano B (clima, imprevistos)")

    print("\n--- TAREFAS CADASTRADAS NO SISTEMA ---")
    listar_tarefas_por_evento(id_evento)

    print("\n  Atenção aos últimos detalhes! Boa sorte no evento! ")
    print("=" * 60)


def _contagem_regressiva(id_evento, dados):
    """Calcula e exibe os dias restantes para o evento.
    Dispara o checklist automaticamente se faltar 1 dia ou menos."""

    # índices: 0=id, 1=nome, 2=tipo, 3=data, 4=horario, 5=local, 6=orcamento, 7=convidados
    nome_evento = dados[1]
    data_evento = datetime.strptime(dados[3], "%d/%m/%Y")
    hoje = datetime.today().today()
    dias = (data_evento - hoje).days

    if dias > 1:
        print(f"\n Faltam {dias} dias para o evento '{nome_evento}'.")
    elif dias == 1:
        print(f"\n  Falta 1 dia para o evento '{nome_evento}'!")
        _exibir_checklist(id_evento, nome_evento, dias)
    elif dias == 0:
        print(f"\n  O evento '{nome_evento}' é hoje!")
        _exibir_checklist(id_evento, nome_evento, dias)
    else:
        print(f"\nℹ  O evento '{nome_evento}' já aconteceu há {abs(dias)} dias.")


def mostrar_contagem_regressiva():
    """Menu de contagem regressiva — opção [4] do menu principal."""

    print("\n=== Contagem Regressiva ===")

    listar_eventos()

    id_evento = input("\nDigite o ID do evento: ")
    evento = buscar_evento_por_id(id_evento)

    if evento is None:
        print("Evento não encontrado.")
        return

    dados = evento.split(";")
    _contagem_regressiva(id_evento, dados)


def mostrar_sugestoes():
    """Menu de sugestões personalizadas — opção [5] do menu principal."""

    print("\n=== Sugestões Personalizadas ===")

    listar_eventos()

    id_evento = input("\nDigite o ID do evento: ")
    evento = buscar_evento_por_id(id_evento)

    if evento is None:
        print("Evento não encontrado.")
        return

    dados = evento.split(";")
    # índices: 0=id, 1=nome, 2=tipo, 3=data, 4=horario, 5=local, 6=orcamento, 7=convidados

    nome      = dados[1]
    tipo      = dados[2].lower()
    data      = dados[3]
    orcamento = float(dados[6])
    convidados = int(dados[7])

    total_gasto = calcular_gastos_evento(id_evento)
    saldo = orcamento - total_gasto

    print(f"\nSugestões para o evento: {nome}")
    print("-" * 40)
    print(f"Data: {data}")

    if "aniversario" in tipo:
        print("- Pense em bolo, decoração temática, música e lista de convidados.")
    elif "casamento" in tipo:
        print("- Priorize local, buffet, fotografia e organização dos horários.")
    elif "formatura" in tipo:
        print("- Foque em convite, traje, cerimônia e registro fotográfico.")
    else:
        print("- Organize local, tarefas principais, custos e responsáveis.")

    if saldo < 0:
        print("-   O orçamento já estourou. Reveja custos ou corte tarefas menos importantes.")
    elif saldo < orcamento * 0.2:
        print("- O saldo está baixo. Evite criar novas tarefas caras.")
    else:
        print("- O orçamento está controlado. Continue acompanhando os gastos.")

    if convidados >= 100:
        print("- Como tem muitos convidados, confirme presença com antecedência.")
    elif convidados >= 30:
        print("- A quantidade de convidados é média. Uma lista organizada já ajuda muito.")
    else:
        print("- Evento menor: dá para focar mais nos detalhes e economizar.")

    
    print()
    _contagem_regressiva(id_evento, dados)
