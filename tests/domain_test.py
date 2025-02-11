
import pytest

from customer import Customer
from fitnessGym import FitnessGym, CustomerNotFound


def test_register_customer():
    gym = FitnessGym("VivaGym Academy")
    customer = Customer(id="", name="Ana Souza", phoneNumber="917331324", email="ana_souza@gmail.com",
                        user="ASouza", password="1234")

    gym.register_customer(customer)
    customers = gym.get_all_customers()

    assert customer in customers
    assert customer.id == "0"


def test_get_all_customers():
    gym = FitnessGym("VivaGym Academy")
    customer1 = Customer(id="", name="João Silva", phoneNumber="932930094", email="j_silva@yahoo.com", user="JSilva",
                         password="1234")
    customer2 = Customer(id="", name="Ana Souza", phoneNumber="917331324", email="ana_souza@gmail.com", user="ASouza",
                         password="1234")
    gym.register_customer(customer1)
    gym.register_customer(customer2)

    customers = gym.get_all_customers()

    assert len(customers) == 2
    assert customer1 in customers
    assert customer1.id == "0"
    assert customer2 in customers
    assert customer2.id == "1"


def test_search_customer_by_name():
    gym = FitnessGym("VivaGym Academy")
    customer = Customer(id="", name="João Silva", phoneNumber="932930094", email="j_silva@yahoo.com", user="JSilva",
                          password="1234")
    gym.register_customer(customer)

    result = gym.get_customer_by_name("João Silva")

    assert customer.id == "0"
    assert len(result) > 0
    assert customer in result


def test_search_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    customer = Customer(id="", name="Carlos Lopes", phoneNumber="914252253", email="c_lopes@yahoo.com", user="CLopes",
                          password="1234")

    gym.register_customer(customer)

    result = gym.get_customer_by_id("0")

    assert customer.id == "0"
    assert customer == result


def test_edit_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    customer = Customer(id="", name="Rogerio", phoneNumber="913214223", email="r_samp@hotmail.com", user="Rogi99",
                          password="1234")
    gym.register_customer(customer)

    gym.edit_customer_by_id("0", "Rogerio", phoneNumber="969757724", email="rr_99@hotmail.com", user="RR99",
                            password="1234")

    result = gym.get_customer_by_id("0")

    assert customer.id == "0"
    assert customer == result


# Resposta 2a
def test_delete_customer():
    gym = FitnessGym("VivaGym Academy")
    customer = Customer(id="", name="Maria Oliveira", phoneNumber="935332524", email="mmoliv@yahoo.com", user="MOliv",
                          password="1234")
    gym.register_customer(customer)

    customers_before = gym.get_all_customers()

    assert customer.id == "0"
    assert len(customers_before) > 0
    assert customer in customers_before

    gym.delete_customer_by_id("0")

    assert not customer in customers_before


def test_delete_nonexistent_customer():
    gym = FitnessGym("VivaGym Academy")

    with pytest.raises(CustomerNotFound):
        gym.delete_customer_by_id("999")
