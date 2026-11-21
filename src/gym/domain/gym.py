from abc import ABC, abstractmethod
from datetime import date

from gym.domain.customer import Customer


class Gym(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def register_customer(self, name: str, phone_number: str, email: str, user: str, password: str):
        pass

    @abstractmethod
    def list_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def list_customers_by_name(self, name: str) -> list[Customer]:
        pass

    @abstractmethod
    def get_customer_by_id(self, id: str) -> Customer:
        pass

    @abstractmethod
    def edit_customer_by_id(self, id: str, name: str, birthday: date):
        pass

    @abstractmethod
    def delete_customer_by_id(self, id: str):
        pass
