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

def cadastrar():  # função para cadastrar um novo usuário, onde o usuário digita um nome de usuário e senha, e essas informações são salvas em um arquivo JSON para serem usadas posteriormente no login
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

def login():  # função para fazer login, onde o usuário digita seu nome de usuário e senha, e o sistema verifica se as credenciais estão corretas, permitindo ou negando o acesso ao sistema de eventos
    usuarios = carregar_usuarios()

    titulo("LOGIN")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    for u in usuarios: # usamos u para percorrer a lista de usuários, verificando se o usuário e senha correspondem a algum cadastro existente


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
