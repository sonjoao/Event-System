from src.auth import tela_inicial

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
  # usei esse def para criar uma função, quando der o printe vai ficar entre linhas, para ficar mais bonito
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





  
