from datetime import date

from customer import Customer


class Gym:
    def __init__(self, name: str):
        self._name = name

    # Resposta 1a
    def register_customer(self, name: str, birthday: date):
        raise NotImplementedError

    # Resposta 1a
    def get_all_customers(self) -> list[Customer]:
        raise NotImplementedError

    # Resposta 1a
    def get_customer_by_name(self, name: str) -> list[Customer]:
        raise NotImplementedError

    def get_customer_by_id(self, id: str) -> list[Customer]:
        raise NotImplementedError

    def edit_customer_by_id(self, id: str, name: str, birthday: str):
        raise NotImplementedError

    # Resposta 1a
    def delete_customer_by_id(self, iD: str):
        raise NotImplementedError
