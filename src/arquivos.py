

def ler_arquivo(caminho):
    linhas = []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            
            for linha in arquivo:
                linha = linha.strip()

                
                if linha != "":
                    linhas.append(linha)

    except FileNotFoundError:
        # Isso evita o programa quebrar no primeiro uso.
        return []

    return linhas


def salvar_arquivo(caminho, linhas):
   # w = abrir o arquivo no modo escrita na ultima linha
    
    with open(caminho, "w", encoding="utf-8") as arquivo:
        # Passamos por cada linha da lista recebida.
        for linha in linhas:
            # Escrevemos a linha e pulamos para a próxima.
            arquivo.write(linha + "\n")


def adicionar_linha(caminho, linha):
    # O modo "a" adiciona no final sem apagar o que já existe.
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(linha + "\n")
