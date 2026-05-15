def mostrar_orcamento():
    print("\n=== Controle de Orçamento ===")
    
    listar_eventos()

    # 1. TRATAMENTO DE ERRO: O usuário pode digitar um ID que não existe ou letras
    try:
        id_evento = input("\nDigite o ID do evento: ")
        evento = buscar_evento_por_id(id_evento)

        if evento is None:
            print("⚠️ Erro: Evento não encontrado. Verifique o ID.")
            return

        dados = evento.split(";")
        
        # 2. CONVERSÃO SEGURA: Transformando texto em número decimal (float)
        # O orçamento está na posição 5 da lista 'dados'
        orcamento_limite = float(dados[5])
        
        # Chamamos a função que soma os gastos (que já explicamos antes)
        total_gasto = calcular_gastos_evento(id_evento)
        
        saldo = orcamento_limite - total_gasto

        print("\n" + "="*30)
        print(f"RESUMO: {dados[1].upper()}") # Nome do evento em maiúsculo
        print(f"Verba Total:  R$ {orcamento_limite:.2f}")
        print(f"Gasto Atual:  R$ {total_gasto:.2f}")
        print(f"Saldo Livre:  R$ {saldo:.2f}")
        print("="*30)

        # 3. LÓGICA DE NEGÓCIO 
        if saldo < 0:
            print("🚨 ALERTA: O orçamento estourou!")
        elif saldo < (orcamento_limite * 0.1): # Se sobrar menos de 10%
            print("⚠️ Cuidado: O saldo está quase acabando.")
        else:
            print("✅ Orçamento dentro do limite.")

    except ValueError:
        print("❌ Erro: Digite apenas números para valores e IDs.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")
