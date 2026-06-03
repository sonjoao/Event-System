def ler_arquivo(caminho):
  linhas = []

  try:
    with open(caminho, "r", encondig="utf-8") as arquivo:
      for linha in arquivo:
          linha = linha.strip()

        if linha != "":
         linhas.append(linha)

  except FileNotFoundError:
    return []
 return linhas

def salvar_arquivo(caminho, linhas):
  with open(caminho, "w", encoding="utf-8") as arquivo:
    for linha in linhas:
      arquivo.write(linha + "\n")

def adicionar_linha(caminho, linha):
  with open(caminho, "a", encondig="utf-8) as arquivo:
            arquivo.write(linha + "\n")







