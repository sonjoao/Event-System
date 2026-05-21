arquivo_tarefas = "dados/tarefas.txt"

def gerar_id_tarefa():
  tarefas = ler_arquivo(arquivo_tarefas) # Ler todas as tarefas ja cadastradas
  if len(tarefas) == 0:
    return 1
    ultima_tarefa = tarefas[-1] # pegar ultima tarefa pra descobrir o ultimo id usado
    ultimo_id = int(ultima_tarefa.split(";")[0])
    return ultimo_id + 1
