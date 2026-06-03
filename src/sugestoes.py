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
      

      

      


                                    


                                
      
