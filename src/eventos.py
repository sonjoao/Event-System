import csv
from datetime import datetime

arquivo = "eventos.csv"
 
def cadastrar_evento():

    print("\n==== CADRASTO DO EVENTO ====")

    nome = input("Nome do evento: ").strip()
    tipo = input("Tipo do evento: ").strip()
    local = input("Local do evento: ").strip()
 with open(arquivo, "a", newline="", encoding="utf-8") as arq:

        escritor = csv.writer(arq)

        escritor.writerow([
            nome,
            tipo,
            data,
            local
        ])

    print("\nEvento cadastrado")

def listar_eventos():

    print("\nLista de Eventos")

    try:

        with open(arquivo, "r", encoding="utf-8") as arq:
         leitor=csv.reader(arq)


         vazio= true
         for i,linha in enumerate(leitor):
           vazio=false
            nome=linha[0]
            tipo=linha[1]
            data=linha[2]
            local=linha[3]


           try:
            data_evento=datetime.stirptime(data, "%d/%m/%Y")
            hoje=datetime.now()
            dias=(data_evento - hoje).days

            except:
                    dias = "erro na data"

                print(f"""
Evento {i}

Nome: {nome}
Tipo: {tipo}
Data: {data}
Local: {local}

Faltam {dias} dias
                """)
            if vazio:
             print("Nenhum evento cadastrado")

    except: 
        print("Erro ao abrir arquivo")
     return

     listar_eventos()

      try:

          indice=int(input("Digite o numero do evento")
                     if indice>= len(eventos):
                          print("Evento não encontrado")
                          return
       except:
        print("Valor invalido")
        return

print("Nova dados")
eventos[indice][0] = input("Novo nome: ")
eventos[indice][1] = input("Novo tipo: ")
eventos[indice][2] = input("Nova data: ")
eventos[indice][3] = input("Novo local: ")

with open(arquivo,"w", newline="", encoding="utf-8") as arq:
   escritor=csv.writter(arq)
    escritor.writenows(eventos)
  print("\nEvento atualizado")


def excluir_evento():

    eventos = []

     try: 
      with open(arquivo,"r", encoding="utf-8") as arq:

       leitor=csv.reader(arq)

        for linha in leitor:
         eventos.append(linha)

      except:
      print("Erro ao abrir  araquivo")
       return

      listar_eventos()


        try:
         indice=int(input("\n Numero do evento  para excluir:"))
         if indice >=len(eventos):
          print("Evento não encontrado")
          return






           

     












