import json

ARQUIVO = "dados/usuarios.json"

# mesmo esquema de função de texto, para deixar tudo padrão
def linha():
    print("=" * 60)
    
def titulo(texto):
    linha()
    print(texto.center(60))
    linha()

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except:
        return []
        
def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def cadastrar():
    usuarios = carregar_usuarios()

    titulo("CADASTRO")

    usuario = input("Crie um usuário: ")
    senha = input("Crie uma senha: ")

    usuarios.append({
        "usuario": usuario,
        "senha": senha
    })

    salvar_usuarios(usuarios)

    print("\nCadastro realizado com sucesso!")

def login():
    usuarios = carregar_usuarios()

    titulo("LOGIN")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            print("\nLogin realizado com sucesso!")
            return True

    print("\nUsuário ou senha incorretos!")
    return False

def tela_inicial():
    titulo("SISTEMA DE EVENTOS")

    resposta = input("Possui cadastro? (s/n): ").lower()

    if resposta == "n":
        cadastrar()

    return login()
