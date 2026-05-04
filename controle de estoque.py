produtos = []

while True:
    print("==================================")
    print("CONTROLE DE ESTOQUE DO SALÃO")
    print("1 - Cadastrar produto")
    print("2 - Ver estoque")
    print("3 - Registrar venda")
    print("4 - Registrar uso")
    print("5 - Repor estoque")
    print("6 - Remover produto")
    print("7 - Salvar")
    print("8 - Carregar dados")
    print("9 - Sair")
    print("==================================")

    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        nome = input("Nome do produto: ").lower()
        categoria = input("Categoria do produto: ").lower()
        quantidade = int(input("Quantidade do produto: "))
        preco = float(input("Preço do produto: "))

        produto_novo = [nome, categoria, quantidade, preco]
        produtos.append(produto_novo)

        print("Produto cadastrado com sucesso!")

    elif opcao == 2:
        print("\nESTOQUE:")
        for produto in produtos:
            print(produto)

    elif opcao == 3:
        nome = input("Nome do produto: ").lower()
        qnt = int(input("Quantidade vendida: "))

        for produto in produtos:
            if produto[0] == nome:
                if produto[2] >= qnt:
                    produto[2] -= qnt
                    print("Venda registrada!")
                else:
                    print("Estoque insuficiente!")
                break

    elif opcao == 4:
        nome = input("Nome do produto usado: ").lower()
        qnt = int(input("Quantidade usada: "))

        for produto in produtos:
            if produto[0] == nome:
                if produto[2] >= qnt:
                    produto[2] -= qnt
                    print("Uso registrado!")
                else:
                    print("Estoque insuficiente!")
                break

    elif opcao == 5:
        nome = input("Produto para repor: ").lower()
        qnt = int(input("Quantidade adicionada: "))

        for produto in produtos:
            if produto[0] == nome:
                produto[2] += qnt
                print("Estoque atualizado!")
                break

    elif opcao == 6:
        nome = input("Produto para remover: ").lower()

        for produto in produtos:
            if produto[0] == nome:
                produtos.remove(produto)
                print("Produto removido!")
                break

    elif opcao == 7:
        arquivo = open("estoque.txt", "w")

        for produto in produtos:
            linha = f"{produto[0]};{produto[1]};{produto[2]};{produto[3]}\n"
            arquivo.write(linha)

        arquivo.close()
        print("Dados salvos!")

    elif opcao == 8:
        try:
            arquivo = open("estoque.txt", "r")

            produtos = []

            for linha in arquivo:
                dados = linha.strip().split(";")
                nome = dados[0]
                categoria = dados[1]
                quantidade = int(dados[2])
                preco = float(dados[3])

                produtos.append([nome, categoria, quantidade, preco])

            arquivo.close()
            print("Dados carregados!")

        except:
            print("Nenhum arquivo encontrado.")

    elif opcao == 9:
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")