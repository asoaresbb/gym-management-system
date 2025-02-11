from dataclasses import dataclass

@dataclass
class Customer:
    id: str
    name: str
    phoneNumber: str
    email: str
    user: str
    password: str

    # Resposta 1c.
    # Metodo polifórmico que é subscrito pelas subclasses
    def get_discount(self) -> float:
        raise NotImplementedError


# Subclasse para clientes regulares
# Clientes normais não têm desconto # Resposta 1c.
class RegularCustomer(Customer):
    def get_discount(self) -> float:
        return 0.0


# Subclasse para clientes VIP
# Clientes VIP têm 10% de desconto # Resposta 1c.
class VIPCustomer(Customer):
    def get_discount(self) -> float:
        return 10.0
