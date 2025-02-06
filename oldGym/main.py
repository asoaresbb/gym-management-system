from cliente import Cliente
from ginasio import Ginasio
from pagamento import Pagamento


if __name__ == "__main__":
    ginasio = Ginasio("Ginásio Universidade Aberta")
    while True:
        print("\n[1] Adicionar Cliente")
        print("[2] Registar Pagamento")
        print("[3] Listar Clientes")
        print("[4] Listar Pagamentos de um Cliente")
        print("[5] Desativar Cliente")
        print("[6] Pesquisar Cliente")
        print("[7] Editar Dados do Cliente")
        print("[8] Listar Devedores")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Qual o nome do cliente? ")
                idade = input("Qual a sua idade? ")
                cliente = Cliente(nome, idade)
                ginasio.adicionar_cliente(cliente)
                print(f"Cliente {cliente} adicionado com sucesso.")

            elif opcao == "2":
                nome_cliente = input("Qual o nome do cliente que efetuou o pagamento? ")
                cliente = ginasio.validar_cliente_existe(nome_cliente)
                valor = input("Qual o valor do pagamento? ")
                data = input("Qual a data do pagamento? (DD/MM/AAAA) ")
                metodo = input("Qual o método de pagamento? (Cartão, Dinheiro, etc.) ")
                pagamento = Pagamento(valor, data, metodo)
                cliente.realizar_pagamento(pagamento)
                print(f"Pagamento de {valor}€ registado com sucesso para {cliente.nome}.")

            elif opcao == "3":
                print("\nClientes registados:")
                ginasio.listar_clientes()

            elif opcao == "4":
                nome_cliente = input("Qual o nome do cliente? ")
                cliente = ginasio.validar_cliente_existe(nome_cliente)
                print(f"\nPagamentos do cliente {cliente.nome}:")
                cliente.listar_pagamentos()

            elif opcao == "5":
                nome_cliente = input("Qual o nome do cliente que deseja desativar? ")
                cliente = ginasio.validar_cliente_existe(nome_cliente)
                cliente.desativar()
                print(f"Cliente '{cliente.nome}' desativado com sucesso.")

            elif opcao == "6":
                termo = input("Introduza o nome ou parte do nome do cliente: ")
                resultados = ginasio.pesquisar_clientes(termo)
                if not resultados:
                    print("Nenhum cliente encontrado.")
                else:
                    print("\nClientes encontrados:")
                    for cliente in resultados:
                        print(cliente)

            elif opcao == "7":
                nome_cliente = input("Qual o nome do cliente que deseja editar? ")
                cliente = ginasio.validar_cliente_existe(nome_cliente)
                novo_nome = input(f"Novo nome (atual: {cliente.nome}) [Enter para manter]: ")
                nova_idade = input(f"Nova idade (atual: {cliente.idade}) [Enter para manter]: ")
                cliente.editar_dados(
                    nome=novo_nome if novo_nome else None,
                    idade=nova_idade if nova_idade else None,
                )
                print("Dados do cliente atualizados com sucesso.")

            elif opcao == "8":
                ginasio.listar_devedores()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print(f"Erro: {e}")