import csv
from datetime import datetime

arquivo = "eventos.csv"
 
def cadastrar_evento():

    print("\n==== CADRASTO DO EVENTO ====")

    nome = input("Nome do evento: ").strip()
    tipo = input("Tipo do evento: ").strip()
    local = input("Local do evento: ").strip()
    
 while True:
        data = input("Data (dd/mm/aaaa): ")

        try:
            datetime.strptime(data, "%d/%m/%Y")
            break

        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")
          while True:

        try:
            orcamento = float(input("Orçamento do evento: R$ "))

            if orcamento < 0:
                print("Digite um valor positivo.")
                continue

            break

        except ValueError:
            print("Digite um número válido.")

    with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([nome, tipo, data, local])
print("\n==== evento cadastrado com sucesso ====")
def listar_eventos():
print("\n==== EVENTTO CADASTRADOS ====")










