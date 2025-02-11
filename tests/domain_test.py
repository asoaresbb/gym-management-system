
import pytest

from fitnessGym import FitnessGym, CustomerNotFound


def test_get_all_customers():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="João Silva", phone_number="932930094", email="j_silva@yahoo.com", user="JSilva",
                          password="1234")
    gym.register_customer(name="Ana Souza", phone_number="917331324", email="ana_souza@gmail.com", user="ASouza",
                          password="1234")

    customers = gym.get_all_customers()

    assert len(customers) > 0
    assert any(c.name == "João Silva" for c in customers)
    assert any(c.phoneNumber == "932930094" for c in customers)
    assert any(c.email == "j_silva@yahoo.com" for c in customers)
    assert any(c.user == "JSilva" for c in customers)
    assert any(c.password == "1234" for c in customers)
    assert any(c.name == "Ana Souza" for c in customers)
    assert any(c.phoneNumber == "917331324" for c in customers)
    assert any(c.email == "ana_souza@gmail.com" for c in customers)
    assert any(c.user == "ASouza" for c in customers)
    assert any(c.password == "1234" for c in customers)

def test_search_customer_by_name():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="João Silva", phone_number="932930094", email="j_silva@yahoo.com", user="JSilva",
                          password="1234")

    result = gym.get_customer_by_name("João Silva")

    assert len(result) > 0
    assert any(c.name == "João Silva" for c in result)


def test_search_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="Carlos Lopes", phone_number="914252253", email="c_lopes@yahoo.com", user="CLopes",
                          password="1234")

    result = gym.get_customer_by_id("0")

    assert result.id == "0"
    assert result.name == "Carlos Lopes"
    assert result.phoneNumber == "914252253"
    assert result.email == "c_lopes@yahoo.com"
    assert result.user == "CLopes"
    assert result.password == "1234"


def test_edit_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="Rogerio", phone_number="913214223", email="r_samp@hotmail.com", user="Rogi99",
                          password="1234")

    gym.edit_customer_by_id("0", "Rogerio", phoneNumber="969757724", email="rr_99@hotmail.com", user="RR99",
                            password="1234")
    result = gym.get_customer_by_id("0")

    assert result.name == "Rogerio"


# Resposta 2a
def test_delete_customer():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(name="Maria Oliveira", phone_number="935332524", email="mmoliv@yahoo.com", user="MOliv",
                          password="1234")
    customers_before = gym.get_all_customers()
    assert any(c.name == "Maria Oliveira" for c in customers_before)
    customer_id = next(c.id for c in customers_before if c.name == "Maria Oliveira")

    gym.delete_customer_by_id(customer_id)

    assert not any(c.id == customer_id for c in gym.get_all_customers())


def test_delete_nonexistent_customer():
    gym = FitnessGym("VivaGym Academy")

    with pytest.raises(CustomerNotFound):
        gym.delete_customer_by_id("999")
