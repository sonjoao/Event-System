import json
ARQUIVO = "dados/usuarios.jason"

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

    print("\n___ CADRASTO ___")

    usuario = input("Crie um usuário: ")
    senha = input("Crie uma senha: ")

    usuario.append({
        "usuario": usuario
        "senha": senha
    })

    salvar_usuarios(usuarios)

    print(\nCadastro realizado com sucesso!)
    
def login()

