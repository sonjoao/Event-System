from datetime import datetime
def verificar_dia_evento(data_evento):
  hoje=datetime.today()
  data=datetime.strptime(
      data_evento,
      "%d/%m/%Y"
  )
  dias=(data-hoje).days
  return dias
  
  
