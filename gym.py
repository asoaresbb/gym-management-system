from customer import Customer
from datetime import date

class Gym:
    def __init__(self, name: str):
        self._name = name
        self._customers: list[Customer] = []

    def register_customer(self, name: str, birthday: date):
        customer = Customer(name, birthday, id=str(len(self._customers)))
        self._customers.append(customer)

    def get_all_customers(self) -> list[Customer] :
        return self._customers

    def search_customer(self, name: str) -> list[Customer]:
        return [customer for customer in self._customers if name.lower() in customer.name.lower()]

    def delete_customer_by_id(self, id: str):
        customer_to_delete: list[Customer] = []
        for customer in self._customers:
            if customer.id == id :
                customer_to_delete.append(customer)
                break
        if customer_to_delete:
            self._customers.remove(customer_to_delete[0])
        else:
            raise CustomerNotFound()

class CustomerNotFound(Exception):
    ...