import csv
from datetime import datetime

arquivo = "eventos.csv"
 
def cadastrar_evento():

    print("\nCadastro de Evento")

    nome = input("Nome do evento: ")
    tipo = input("Tipo do evento: ")
    data = input("Data do evento (dd/mm/aaaa): ")
    local = input("Local do evento: ")
