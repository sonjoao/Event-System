import json
ARQUIVO = "dados/usuarios.jason"

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except:
        return []
