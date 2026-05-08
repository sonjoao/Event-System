import csv
from datetime import datetime

arquivo = "eventos.csv"
 
def cadastrar_evento():

    print("\nCadastro de Evento")

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    data = input("Data (dd/mm/aaaa): ")
    local = input("Local: ")
