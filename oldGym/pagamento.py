class Pagamento:
    def __init__(self, valor, data, metodo):
        self.valor = self.validar_valor(valor)
        self.data = data
        self.metodo = metodo

    @staticmethod
    def validar_valor(valor):
        if not str(valor).replace(".", "").isdigit():
            raise ValueError("O valor deve ser numérico.")
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        return valor

    def __str__(self):
        return f"Valor: {self.valor}€, Data: {self.data}, Método: {self.metodo}"