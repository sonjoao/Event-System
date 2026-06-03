from datetime import datetime
from src.eventos import listar_eventos, buscar_evento_por_id
from src.orcamento import calcular_gastos_evento

def mostar_contagem_regressiva():
    print("\n=== Contagem Regressiva ===")

    listar_eventos()

    id_evento = input("\nDigite o ID do evento: ")
    evento = buscar_evento_por_id(id_evento)

    if evento is None:
        print(Evento não encontrado. ")
        return

      dados = evento.split(";")

      data_evento = datetime.strptime(dados[3], "%d/%m/%Y)

      hoje = datetime.now()
      dias_restantes = (data_eventos - hoje).days

      print(f"\nEventos: {dados[1]}")

      if dias_restantes > 0 :
          print("f"Faltam {dias_restantes} dias para o evento.")
      elif dias_restantes == 0:
          print("O seu evento é hoje!!)
      else:
          print("Esse evento já passou.")

def mostrar_sugestoes():
    print("\n=== Sugestões Personalizadas ==="

    listar_eventos()

    id_evento = input("\nDigite o ID do evento: ")
    evento = buscar_evento_por_id(id_evento)

    if: evento is None:
         print("Evento não encontrado.")
         return

    dados = evento.split(";)

    nome = dados[1]
    tipo = dados[2].lower()
    data = dados[3]
    orcamento = float(dados[5])
    convidados = int(dados[6])
    total_gasto = calcular_gastos_evento(id_evento)
    saldo = orcamento - total_gasto

    print("\nSugestões para o evento")
    print("-" * 40)
    print(f"Evento: {nome}")
    print(f"Data: {data}")

    
    

   
    
    


    

    
      

      

      


                                    


                                
      
