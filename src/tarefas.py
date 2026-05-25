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
