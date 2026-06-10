from src.auth import tela_inicial

from src.eventos import ( #importei as funções de eventos  para usar no menu
    criar_evento,
    listar_eventos,
    editar_evento,
    excluir_evento
)

from src.tarefas import ( #importei as funções de tarefas  
    criar_tarefa,
    listar_tarefas,
    listar_tarefas_por_evento,
    concluir_tarefa,
    excluir_tarefa
)

from src.orcamento import mostrar_orcamento #importei a função de orçamento 
from src.sugestoes import mostrar_contagem_regressiva, mostrar_sugestoes #importei as funções de sugestões 

import os


def limpar_tela():
    os.system("cls")


def linha():      
    print("_" * 60)


def titulo(texto):
    linha()
    print(texto.center(60))
    linha()


def pausar():
    input("\nPressione ENTER para continuar...") #função simples para pausar a tela e esperar o usuário pressionar enter


def menu_eventos():     #função para mostrar o menu de eventos, onde o usuário pode escolher entre criar, listar, editar ou excluir eventos
    opcoes = {
        "1": criar_evento,
        "2": listar_eventos,
        "3": editar_evento,
        "4": excluir_evento
    }

    while True:  #loop para mostrar o menu de eventos até o usuário escolher voltar
        limpar_tela()
        titulo("MENU DE EVENTOS")

        print("\n[1] Cadastrar evento")
        print("[2] Listar eventos")
        print("[3] Editar evento")
        print("[4] Excluir evento")
        print("[0] Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            break

        if opcao in opcoes:
            limpar_tela()
            opcoes[opcao]()
            pausar()
        else:
            print("Opção inválida.")
            pausar()


def menu_tarefas(): 
    while True:
        limpar_tela()
        titulo("MENU DE TAREFAS")

        print("\n[1] Cadastrar tarefa")
        print("[2] Listar tarefas")
        print("[3] Listar tarefas por evento")
        print("[4] Concluir tarefa")
        print("[5] Excluir tarefa")
        print("[0] Voltar")

        opcao = input("\nEscolha uma opção: ") 

        if opcao == "1":
            criar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            id_evento = input("ID do evento: ")
            listar_tarefas_por_evento(id_evento)

        elif opcao == "4":
            concluir_tarefa()

        elif opcao == "5":
            excluir_tarefa()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        pausar()


def menu_principal(): 
    while True:
        limpar_tela() 

        titulo("SISTEMA DE ORGANIZAÇÃO DE EVENTOS")

        print("\n[1] Eventos")
        print("[2] Tarefas")
        print("[3] Controle de orçamento")
        print("[4] Contagem regressiva")
        print("[5] Sugestões")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_eventos()

        elif opcao == "2":
            menu_tarefas()

        elif opcao == "3":
            mostrar_orcamento()
            pausar()

        elif opcao == "4":
            mostrar_contagem_regressiva()
            pausar()

        elif opcao == "5":
            mostrar_sugestoes()
            pausar()

        elif opcao == "0":
            print("\nEncerrando sistema...")
            break

        else:
            print("Opção inválida.")
            pausar()


if __name__ == "__main__": # Inicialização do sistema: valida o acesso do usuário antes de abrir o menu principal
    if tela_inicial():
       menu_principal()
