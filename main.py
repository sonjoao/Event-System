from src.eventos import criar_evento, listar_eventos, editar_evento, excluir_evento
from src.tarefas import criar_tarefa, listar_tarefas, listar_tarefas_por_evento, concluir_tarefa, excluir_tarefa
from src.orcamento import mostrar_orcamento
from src.sugestoes import mostrar_contagem_regressiva, mostrar_sugestoes

def menu_eventos
  while True:
    print("\n ========= MENU DE EVENTOS =========)
    print("1 - Cadastrar evento")
    print("2 - Listar evento")
    print("3 - Editar evento")
    print("4 - Excluir evento")
    print("0" - Voltar")

    opcao = input("Escolha uma opção: ")
         
      if opcao == "1":
         criar_eventos()
      elif opcao == "2":
         listar_eventos()
      elif opcao == "3":
         editar_eventos()
      elif opcao == "4":
         excluir_evento()
      elif opcao == "0":
         break
          
    else:
      print("\nOpção inválida! Tente novamente.")

def menu_tarefas():
  while True:
     print("\n========= MENU DE TAREFAS =========")
     print("1 - Cadastrar tarefa")
     print("2 - Listar todas as tarefas")
     print("3 - Listar tarefas de um evento")
     print("4 - Marcar tarefa como conclúida")
     print("5 - Excluir tarefa")
     print("0 - Voltar")

def menu_principal():
  while True:
         print("\n=============================")
         print(" SISTEMAS DE ORGANIZAÇÃO DE EVENTOS")
         print("\n=============================")
         print("1 - Eventos")
         print("2 - Tarefas")
         print("3 - Controle de orçamentos")
         print("4 - Contagem regressiva")
         print("5 - Susgestões personalizada")
         print("0 - Sair")

         opcao = input("Escolha uma opcão: ")
              if opcao == "1":
                menu_eventos()
              elif opcao == "2":
                menu_tarefas()
              elif opcao == "3":
                mostra_orcamento()
              elif opcao == "4":
                mostra_contagem_regressiva()
              elif opcao == "5":
                exluir_tarefa()
              elif opcao == "0":
                 break
              else:
                 print("Opção inválida. Tente novamente.")

      
                
              
              

         
        
    
  
    
    
    


