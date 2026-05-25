arquivo_tarefas = "dados/tarefas.txt"

def gerar_id_tarefa():
  tarefas = ler_arquivo(arquivo_tarefas) # Ler todas as tarefas ja cadastradas
  if len(tarefas) == 0:
    return 1
    ultima_tarefa = tarefas[-1] # pegar ultima tarefa pra descobrir o ultimo id usado
    ultimo_id = int(ultima_tarefa.split(";")[0])
    return ultimo_id + 1

def criar_tarefa():
  print("\n--- CADASTRO DE TAREFA ---") #objetivo: listar todos os eventos para o user saber qual evento colocar a tarefa
  listar_eventos()
  id_evento = input("\nDigite o id do evento dessa tarefa: ")
  if buscar_evento_por_id(id_evento) is None: #variavel pra ver se o evento existe antes de cadastrar a tarefa 
    print("Evento não encontrado. Cadastre um evento válido.")
    return
id_tarefa = gerar_id_tarefa()
nome_tarefa = input("Nome da tarefa: ")

while True: # Custo precisa ser obrigatoriamente numeros
  try:
    custo = float(input("Custo da tarefa: R$ "))
    break
  except ValueError:
    print("Digite apenas números no custo.")
status = "pendente" # marca todas as tarefas como pendente 

linha = f"{id_tarefa};{id_evento};{nome_tarefa};{custo};{status}" #salva todos na lista

print("\nTarefa Cadastrada com Sucesso!")

def listar_tarefas():
  print("\n Lista de Tarefas")
  tarefas = ler_arquivo(arquivo_tarefas)
  if len(tarefas) == 0:
    print("Nenhuma Tarefa cadastrada ainda")
    return
  for tarefa in tarefas:
    dados = tarefa.split(";")
    print("-" * 40) # tecnica para replicar qualquer tipo de texto sem precisar printar varias vezes 
    print(f"ID da tarefa: {dados[0]}")
    print(f"ID da Evento: {dados[1]}")
    print(f"Tarefa: {dados[2]}")
    print(f"Custo em R$: {(dados[3]):.2f}")
    print(f"Status: {dados[4]}")

def listar_tarefas_por_evento(id_evento): # lista apenas as tarefas de um evento especifico, por isso a variavel se chama assim
  tarefas = ler_arquivo(arquivo_tarefas)
  encontrou = False 
  print("\nTarefas do Evento")
  for tarefa in tarefas:
    dados = tarefa.split(";") # dividindo em substrings retornando dentro da lista 
    if dados[1] == str(id_evento):
      encontrou = True
      print(f"Id da tarefa: {dados[0]}")
      print(f"Tarefa: {dados[2]}")
      print(f"Custo em R$: {float(dados[3]):.2f}")
      print(f"Status: {dados[4]}")
  if not encontrou:
    print("Esse evento ainda não possui Tarefas.")

def concluir_tarefas():
  print("\nConcluir Tarefa")
  listar_tarefas()
  id_concluir = input("\nDigite o ID da Tarefa Concluída: ")
  tarefas = ler_arquivo(arquivo_tarefas)
  novas_tarefas = []
  encontrado = False
  for tarefa in tarefas:
    dados = tarefa.split(";")
    if dados[0] == id_concluir:
      encontrado = True # Isso mantem os dados alterando apenas o status
      tarefa_atualizada = f"{dados[0]};{dados[1]};{dados[2]};{dados[3]};concluída"
      novas_tarefas.append(tarefa_atualizada)
    else:novas_tarefas.append(tarefa)
  salvar_arquivo(arquivo_tarefas, novas_tarefas)
  if encontrado:
    print("\nTarefa marcada como Concluída!")
  else:
    print("\nTarefa Não Encontrada ou Não concluída!")
