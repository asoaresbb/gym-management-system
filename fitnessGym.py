from datetime import date

from customer import Customer
from gym import Gym


class FitnessGym(Gym):
    def __init__(self, name: str):
        super().__init__(name)
        self._customers: list[Customer] = []

    def register_customer(self, name: str, birthday: date):
        customer = Customer(name, birthday, id=str(len(self._customers)))
        self._customers.append(customer)

    def get_all_customers(self) -> list[Customer]:
        return self._customers

    def search_customer(self, name: str) -> list[Customer]:
        return [customer for customer in self._customers if name.lower() in customer.name.lower()]

    def search_customer_by_id(self, id: str):
        for customer in self._customers:
            if customer.id == id:
                return customer
        raise CustomerNotFound()

    def edit_customer_by_id(self, id: str, name: str, birthday: str):
        customer_to_edit: Customer = self.search_customer_by_id(id)
        customer_to_edit.name = name
        customer_to_edit.birthday = birthday

    def delete_customer_by_id(self, id: str):
        customer_to_delete: str = []
        for customer in self._customers:
            if customer.id == id:
                customer_to_delete = customer
                break
        if customer_to_delete:
            self._customers.remove(customer_to_delete[0])
        else:
            raise CustomerNotFound()


class CustomerNotFound(Exception):
    ...
