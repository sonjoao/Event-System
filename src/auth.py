import hashlib
import json
import os

ARQUIVO_USUARIOS = "dados/usuarios.json"
#tive que recorrer a claude para me ensinar como fazer

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if not os.path.exists(ARQUIVOS_USUARIOS):
      return []
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8) as f:
