import json

ARQUIVO = "dados/usuarios.json"


def linha():
    print("=" * 60)
    
def titulo(texto):
    linha()
    print(texto.center(60))
    linha()

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as arquivo: # "r" (Read): Modo de leitura estrita. Apenas lê os dados existentes.
            return json.load(arquivo)
    except:
        return []
  
def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as arquivo: # "w" (Write): Modo de escrita destrutiva. Limpa o arquivo e sobrescreve do zero.
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
   while True:
        titulo("SISTEMA DE EVENTOS")
        resposta = input("Possui cadastro? (s/n): ").lower().strip()

        if resposta == "n":
            cadastrar()
            return login()
        elif resposta == "s":
            return login()  
        else:
            print("\nOpção inválida! Digite apenas 's' para sim ou 'n' para não.")
            input("\nPressione ENTER para tentar novamente...")
            os.system("cls") 
