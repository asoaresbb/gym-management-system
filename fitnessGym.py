from customer import Customer
from gym import Gym


class FitnessGym(Gym):
    def __init__(self, name: str):
        super().__init__(name)
        self._customers: list[Customer] = []

    def register_customer(self, name: str, phone_number: str, email: str, user: str, password: str):
        customer = Customer(id=str(len(self._customers)), name=name, phone_number=phone_number, email=email, user=user,
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

    def edit_customer_by_id(self, id: str, name: str = "", phone_number: str = "", email: str = "", user: str = "",
                            password: str = ""):
        customer_to_edit: Customer = self.get_customer_by_id(id)

        if name:
            customer_to_edit.name = name
        if phone_number:
            customer_to_edit.phone_number = phone_number
        if email:
            customer_to_edit.email = email
        if user:
            customer_to_edit.user = user
        if password:
            customer_to_edit.password = password

    def delete_customer_by_id(self, id: str):
        customer_to_delete: Customer = self.get_customer_by_id(id)
        self._customers.remove(customer_to_delete)


class CustomerNotFound(Exception):
    pass
