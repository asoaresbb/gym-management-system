from dataclasses import dataclass
from datetime import date

@dataclass
class Customer:
    name: str
    birthday: date
    id: str