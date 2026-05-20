def orçamento():
    print(" ==== controle de orçamento ====  ")
    
    listar_eventos()

    # 1. TRATAMENTO DE ERRO: O usuário pode digitar um ID que não existe ou letras
    try:
        id_evento = input("Digite o ID do evento:")
        evento = buscar_evento_por_id(id_evento)

        if evento is None:
            print(" Erro: Evento não encontrado, verifique o ID")
            return
        # Converte a linha do texto do arquivo em uma lista
        dados = evento.split(";")
        
        #  Transforma texto em número decimal utilizando o float
        #  O orçamento está na posição [5] no banco de dados
        orcamento_limite = float(dados[5])
        
        # Busca o somatório de custos vinculados a este ID
        total_gasto = calcular_gastos_evento(id_evento)
        
        #Subtrai as depesas acumuladas
        saldo = orcamento_limite - total_gasto
        
        # Painel de resumo financeiro
        print("="*30)
        print(f"RESUMO: {dados[1].upper()}") 
        print(f"Verba Total:  R$ {orcamento_limite:.2f}")
        print(f"Gasto Atual:  R$ {total_gasto:.2f}")
        print(f"Saldo Livre:  R$ {saldo:.2f}")
        print("="*30)

        # Verificação do status financeiro
        if saldo < 0:
            print("Alerta : orçamento estourou!")
        elif saldo < (orcamento_limite * 0.1): # Se sobrar menos de 10%
            print("Cuidado: O saldo está quase acabando.")
        else:
            print("Orçamento dentro do limite.") 
            
    #Captura erros de conversão, Letras no lugar de números
    except ValueError:
        print(" Erro: Digite apenas números para valores e IDs.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
