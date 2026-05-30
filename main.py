from src.auth import tela_inicial
# primeiro, importei as outras parte do src, feita pela equipe
from src.eventos import (
  criar_evento
  listar_eventos
  editar_evento,
  excluir_evento
)

from src.tarefas import (
  criar_tarefa,
  listar_tarefa,
  listar_tarefas_por_evento,
  concluir_tarefa,
  excluir_tarefa
)

from src.orcamento import mostrar_orcamento
from src.susgestoes import mostrar_contagem_regressiva, mostrar_sugestoes

import os

def limpar_tela():
  os.system("cls")
  
def linha()
  print("_" * 60)
  # usei esse def para criar uma função, quando der o print vai ficar entre linhas, para ficar mais bonito
def titulo(texto):
  linha()
  print(texto.center(60))
  linha(60)

def pausar():
  input("\nPressione ENTER para continuar...")

def menu_eventos():
  opcoes = {
    "1" : criar_eventos,
    "2" : istar_eventos,
    "3" : editar_evento,
    "4" : excluir_evento
  }

while True:
  limpar_tela()
  titulo("MENU DE EVENTOS")

  print("\n[1] Cadastrar evento")
  print("[2] Listar eventos")
  print("[3] Editar evento")
  print("[4] Excluir evento")
  print("[0] Voltar")

  opcao = input("\nEscolha uma opção: ")

  if opcao == "0"
    break
  
  if opcao in opcoes:
    limpar_tela()
    opcoes[opcao]()
    pausar()
  else:
      print("Opção inválida")
      pausar()

  def menu_tarefas
    while True:
      limpar_tela()
      titulo("MENU DE TAREFAS")
      
      print("\n[1] Cadastrar tarefa")
      print("[2] Listar tarefas")
      print("[3] Editar tarefas")
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

      elif opcao == "4"
          concluir_tarefa()

      elif opcao == "5"
          excluir_tarefas()

      elif opcao == "0":
          break
      else:
          print("Opção inválida")

      pausar()
  
          

      
          
    





  
