from pagamento import Pagamento

class Cliente:
    def __init__(self, nome, idade):
        self.nome = self.validar_nome(nome)
        self.idade = self.validar_idade(idade)
        self.pagamentos = []
        self.ativo = True

    def realizar_pagamento(self, pagamento):
        if not isinstance(pagamento, Pagamento):
            raise ValueError("Pagamento inválido.")
        self.pagamentos.append(pagamento)

    def listar_pagamentos(self):
        if not self.pagamentos:
            print("Nenhum pagamento efetuado.")
        else:
            for pagamento in self.pagamentos:
                print(pagamento)

    def desativar(self):
        self.ativo = False

    def editar_dados(self, nome=None, idade=None):
        if nome:
            self.nome = self.validar_nome(nome)
        if idade:
            self.idade = self.validar_idade(idade)

    def esta_em_divida(self):
        return len(self.pagamentos) == 0

    @staticmethod
    def validar_nome(nome):
        if not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        return nome.strip()

    @staticmethod
    def validar_idade(idade):
        if not str(idade).isdigit():
            raise ValueError("A idade deve ser um número inteiro.")
        idade = int(idade)
        if idade <= 0:
            raise ValueError("A idade deve ser maior que zero.")
        return idade

    def __str__(self):
        status = "Ativo" if self.ativo else "Desativado"
        return f"Nome: {self.nome}, Idade: {self.idade}, Status: {status}"