from abc import ABC, abstractmethod
from datetime import date

from customer import Customer


class Gym(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def register_customer(self, name: str, phoneNumber: str, email: str, user: str, password: str):
        pass

    @abstractmethod
    def get_all_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def get_customer_by_name(self, name: str) -> list[Customer]:
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
