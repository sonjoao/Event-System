# arquivo.py
# Esse arquivo cuida apenas de ler e salvar informações nos arquivos .txt.
# Assim, o resto do projeto não precisa repetir código de abrir arquivo toda hora.


def ler_arquivo(caminho):
    # Criamos uma lista vazia para guardar as linhas do arquivo.
    linhas = []

    try:
        # Abrimos o arquivo no modo leitura, usando utf-8 para aceitar acentos.
        with open(caminho, "r", encoding="utf-8") as arquivo:
            # Lemos todas as linhas do arquivo.
            for linha in arquivo:
                # strip() remove espaços e quebras de linha do começo/fim.
                linha = linha.strip()

                # Se a linha não estiver vazia, ela entra na lista.
                if linha != "":
                    linhas.append(linha)

    except FileNotFoundError:
        # Caso o arquivo ainda não exista, retornamos uma lista vazia.
        # Isso evita o programa quebrar no primeiro uso.
        return []

    # Retornamos as linhas encontradas.
    return linhas


def salvar_arquivo(caminho, linhas):
    # Abrimos o arquivo no modo escrita.
    # O modo "w" apaga o conteúdo antigo e escreve tudo novamente.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        # Passamos por cada linha da lista recebida.
        for linha in linhas:
            # Escrevemos a linha e pulamos para a próxima.
            arquivo.write(linha + "\n")


def adicionar_linha(caminho, linha):
    # Abrimos o arquivo no modo acrescentar.
    # O modo "a" adiciona no final sem apagar o que já existe.
    with open(caminho, "a", encoding="utf-8") as arquivo:
        # Escrevemos a nova linha no final do arquivo.
        arquivo.write(linha + "\n")

        
