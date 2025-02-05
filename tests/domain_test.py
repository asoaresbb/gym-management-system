from datetime import date

import pytest

from gym import Gym, CustomerNotFound


def test_register_customer():
    gym = Gym("Academia da Rebeca")
    gym.register_customer(name="Ana Souza", birthday=date(1985, 8, 15))

    customers = gym.get_all_customers()

    assert any(c.name == "Ana Souza" for c in customers)
    assert any(c.birthday == date(1985, 8, 15) for c in customers)


def test_get_all_customers():
    gym = Gym("Academia da Rebeca")
    gym.register_customer(name="João Silva", birthday=date(1990, 5, 20))

    customers = gym.get_all_customers()

    assert len(customers) > 0
    assert any(c.name == "João Silva" for c in customers)


def test_search_customer():
    gym = Gym("Academia da Rebeca")
    gym.register_customer(name="João Silva", birthday=date(1990, 5, 20))

    result = gym.search_customer("João Silva")

    assert len(result) > 0
    assert any(c.name == "João Silva" for c in result)


def test_delete_customer():
    gym = Gym("Academia da Rebeca")
    gym.register_customer(name="Maria Oliveira", birthday=date(1987, 3, 10))
    customers_before = gym.get_all_customers()
    assert any(c.name == "Maria Oliveira" for c in customers_before)
    customer_id = next(c.id for c in customers_before if c.name == "Maria Oliveira")

    gym.delete_customer_by_id(customer_id)

    assert not any(c.id == customer_id for c in (gym.get_all_customers()))


def test_delete_nonexistent_customer():
    gym = Gym("Academia da Rebeca")

    with pytest.raises(CustomerNotFound):
        gym.delete_customer_by_id("999")
