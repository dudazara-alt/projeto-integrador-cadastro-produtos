def cadastrar_produto(lista):
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("O nome do produto não pode ficar vazio.\n")
        return

    try:
        preco = float(input("Preço: R$ ").replace(",", "."))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Digite um preço e uma quantidade válidos.\n")
        return

    if preco < 0 or quantidade < 0:
        print("Preço e quantidade não podem ser negativos.\n")
        return

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    lista.append(produto)
    print("Produto cadastrado com sucesso!\n")


def listar_produtos(lista):
    if not lista:
        print("Nenhum produto cadastrado.\n")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")
    for produto in lista:
        print(
            f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )
    print()


def pesquisar_produto(lista):
    nome = input("Digite o nome do produto: ").strip().lower()

    for produto in lista:
        if produto["nome"].lower() == nome:
            print(
                f"Produto encontrado: {produto['nome']} | "
                f"Preço: R$ {produto['preco']:.2f} | "
                f"Quantidade: {produto['quantidade']}\n"
            )
            return

    print("Produto não encontrado.\n")


def atualizar_produto(lista):
    nome = input("Nome do produto que deseja atualizar: ").strip().lower()

    for produto in lista:
        if produto["nome"].lower() == nome:
            try:
                novo_preco = float(input("Novo preço: R$ ").replace(",", "."))
                nova_quantidade = int(input("Nova quantidade: "))
            except ValueError:
                print("Digite valores válidos.\n")
                return

            if novo_preco < 0 or nova_quantidade < 0:
                print("Preço e quantidade não podem ser negativos.\n")
                return

            produto["preco"] = novo_preco
            produto["quantidade"] = nova_quantidade
            print("Produto atualizado com sucesso!\n")
            return

    print("Produto não encontrado.\n")


def remover_produto(lista):
    nome = input("Nome do produto que deseja remover: ").strip().lower()

    for produto in lista:
        if produto["nome"].lower() == nome:
            lista.remove(produto)
            print("Produto removido com sucesso!\n")
            return

    print("Produto não encontrado.\n")


def menu():
    lista_produtos = []

    while True:
        print("====== SISTEMA DE CADASTRO DE PRODUTOS ======")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(lista_produtos)
        elif opcao == "2":
            listar_produtos(lista_produtos)
        elif opcao == "3":
            pesquisar_produto(lista_produtos)
        elif opcao == "4":
            atualizar_produto(lista_produtos)
        elif opcao == "5":
            remover_produto(lista_produtos)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
