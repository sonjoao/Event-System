from datetime import datetime
def verificar_dia_evento(data_evento):
  hoje=datetime.today()
  data=datetime.strptime(
      data_evento,
      "%d/%m/%Y"
  )
  dias=(data-hoje).days
  return dias
def modo_evento(data_evento):
  dias=verificar_dia_evento(data_evento)

  if dias >1:

     print(
           f"\nAinda faltam {dias} dias para o evento."
     )
     return  
    
    print("\nMODO EVENTO ATIVADO\n")

    print("✓ Verificar buffet")
    print("✓ Verificar decoração")
    print("✓ Conferir lista de convidados")
    print("✓ Conferir equipamentos")

    print("Atenção aos ultimos detalhes!")


  
  
  
