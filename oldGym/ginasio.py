from cliente import Cliente

class Ginasio:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise ValueError("Cliente inválido.")
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("Não há clientes registados.")
        else:
            for cliente in self.clientes:
                print(cliente)

    def listar_devedores(self):
        devedores = [cliente for cliente in self.clientes if cliente.esta_em_divida()]
        if not devedores:
            print("Nenhum cliente em dívida.")
        else:
            print("\nClientes em dívida:")
            for cliente in devedores:
                print(cliente)

    def obter_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower():
                return cliente
        raise ValueError(f"Cliente '{nome}' não encontrado.")

    def validar_cliente_existe(self, nome):
        try:
            return self.obter_cliente(nome)
        except ValueError:
            raise ValueError(f"Cliente '{nome}' não encontrado.")

    def pesquisar_clientes(self, termo):
        resultados = [
            cliente for cliente in self.clientes 
                if termo.lower() in cliente.nome.lower()
        ]
        return resultados