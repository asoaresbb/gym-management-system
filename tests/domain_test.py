from datetime import date

import pytest

from fitnessGym import FitnessGym, CustomerNotFound


# Resposta 2a
def test_register_customer():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="Ana Souza", birthday=date(1985, 8, 15))

    customers = gym.get_all_customers()

    assert any(c.name == "Ana Souza" for c in customers)
    assert any(c.birthday == date(1985, 8, 15) for c in customers)


# Resposta 2a
def test_get_all_customers():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="João Silva", birthday=date(1990, 5, 20))

    customers = gym.get_all_customers()

    assert len(customers) > 0
    assert any(c.name == "João Silva" for c in customers)


# Resposta 2a
def test_search_customer_by_name():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="João Silva", birthday=date(1990, 5, 20))

    result = gym.get_customer_by_name("João Silva")

    assert len(result) > 0
    assert any(c.name == "João Silva" for c in result)


def test_search_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer("Jose Carlos", birthday=date(2000, 10, 30))

    result = gym.get_customer_by_id("0")

    assert result.id == "0"


def test_edit_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer("Bernardo", birthday=date(1976, 3, 23))

    gym.edit_customer_by_id("0", "Rogerio", birthday=date(1950, 4, 25))
    result = gym.get_customer_by_id("0")

    assert result.name == "Rogerio" and result.birthday == date(1950, 4, 25)


# Resposta 2a
def test_delete_customer():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="Maria Oliveira", birthday=date(1987, 3, 10))
    customers_before = gym.get_all_customers()
    assert any(c.name == "Maria Oliveira" for c in customers_before)
    customer_id = next(c.id for c in customers_before if c.name == "Maria Oliveira")

    gym.delete_customer_by_id(customer_id)

    assert not any(c.id == customer_id for c in gym.get_all_customers())


def test_delete_nonexistent_customer():
    gym = FitnessGym("VivaGym Academy")

    with pytest.raises(CustomerNotFound):
        gym.delete_customer_by_id("999")
