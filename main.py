from src.eventos import *
from src.tarefas import *
from src.orcamento import *
from src.susgestoes import *

def menu():
  while True:
    print("\n========= SISTEMAS  DE EVENTOS ===========)
    print("1 - Eventos")
    print("2 - Tarefas")
    print("3 - Orçamentos")
    print("4 - Sugestões")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\nAbrindo eventos...")
        menu_eventos()
    elif opcao == "2"
        print("\nAbrindo tarefas...")
        menu_tarefas()
    elif opcao == "3"
        print("\nAbrindo orçamentos...")
        menu_orcamentos()
    elif opcao == "4"
        print("\nAbrindo susgestões...")
        menu_susgestoes()
    elif opcao == "0"
        print("\nSistema encerrado.")
        break
    
    else:
      print("\nOpção inválida!")

menu()
  
    
    
    


