from customer import Customer
from gym import Gym


class FitnessGym(Gym):
    def __init__(self, name: str):
        super().__init__(name)
        self._customers: list[Customer] = []

    def register_customer(self, name: str, phoneNumber: str, email: str, user: str, password: str):
        customer = Customer(id=str(len(self._customers)), name=name, phoneNumber=phoneNumber, email=email, user=user,
                            password=password)
        self._customers.append(customer)

    def get_all_customers(self) -> list[Customer]:
        return self._customers

    def get_customer_by_name(self, name: str) -> list[Customer]:
        return [customer for customer in self._customers if name.lower() in customer.name.lower()]

    def get_customer_by_id(self, id: str) -> Customer:
        try:
            return next(customer for customer in self._customers if customer.id == id)
        except StopIteration:
            raise CustomerNotFound()

    def edit_customer_by_id(self, id: str, name: str, phoneNumber: str, email: str, user: str, password: str):
        customer_to_edit: Customer = self.get_customer_by_id(id)
        customer_to_edit.name = name
        customer_to_edit.phoneNumber = phoneNumber
        customer_to_edit.email = email
        customer_to_edit.user = user
        customer_to_edit.password = password

    def delete_customer_by_id(self, id: str):
        customer_to_delete: Customer = self.get_customer_by_id(id)
        self._customers.remove(customer_to_delete)


class CustomerNotFound(Exception):
    pass
