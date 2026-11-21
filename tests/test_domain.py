import pytest

from gym.domain.fitness_gym import FitnessGym, CustomerNotFound


def test_get_all_customers():
    gym = FitnessGym("VivaGym Academy")
    id1 = gym.register_customer(
        name="João Silva", phone_number="932930094", email="j_silva@yahoo.com", user="JSilva", password="1234"
    )
    id2 = gym.register_customer(
        name="Ana Souza", phone_number="917331324", email="ana_souza@gmail.com", user="ASouza", password="1234",
    )

    customers = gym.list_customers()

    assert len(customers) == 2
    joao = next(c for c in customers if c.id == id1)
    assert joao.name == "João Silva"
    assert joao.phone_number == "932930094"
    assert joao.email == "j_silva@yahoo.com"
    assert joao.user == "JSilva"
    assert joao.password == "1234"
    ana = next(c for c in customers if c.id == id2)
    assert ana.name == "Ana Souza"
    assert ana.phone_number == "917331324"
    assert ana.email == "ana_souza@gmail.com"
    assert ana.user == "ASouza"
    assert ana.password == "1234"


def test_search_customer_by_name():
    gym = FitnessGym("VivaGym Academy")
    gym.register_customer(
        name="João Silva", phone_number="932930094", email="j_silva@yahoo.com", user="JSilva", password="1234",
    )

    result = gym.list_customers_by_name("João Silva")

    assert len(result) == 1
    assert result[0].name == "João Silva"


def test_search_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    id = gym.register_customer(
        name="Carlos Lopes", phone_number="914252253", email="c_lopes@yahoo.com", user="CLopes", password="1234",
    )

    result = gym.get_customer_by_id(id)

    assert result.id == id
    assert result.name == "Carlos Lopes"
    assert result.phone_number == "914252253"
    assert result.email == "c_lopes@yahoo.com"
    assert result.user == "CLopes"
    assert result.password == "1234"


def test_edit_customer_by_id():
    gym = FitnessGym("VivaGym Academy")
    id = gym.register_customer(
        name="Rogerio", phone_number="913214223", email="r_samp@hotmail.com", user="Rogi99", password="1234",
    )

    gym.edit_customer_by_id(
        id=id, name="Rogerio", phone_number="969757724", email="rr_99@hotmail.com", user="RR99", password="1234",
    )

    result = gym.get_customer_by_id(id)
    assert result.name == "Rogerio"
    assert result.phone_number == "969757724"
    assert result.email == "rr_99@hotmail.com"
    assert result.user == "RR99"
    assert result.password == "1234"


def test_edit_nonexistent_customer():
    gym = FitnessGym("VivaGym Academy")

    with pytest.raises(CustomerNotFound):
        gym.edit_customer_by_id("999")


# Resposta 2a
def test_delete_customer():
    gym = FitnessGym("VivaGym Academy")
    customer_id = gym.register_customer(
        name="Maria Oliveira", phone_number="935332524", email="mmoliv@yahoo.com", user="MOliv", password="1234",
    )
    customers_before = gym.list_customers()
    assert any(c.name == "Maria Oliveira" for c in customers_before)

    gym.delete_customer_by_id(customer_id)

    assert not any(c.id == customer_id for c in gym.list_customers())


def test_delete_nonexistent_customer():
    gym = FitnessGym("VivaGym Academy")

    with pytest.raises(CustomerNotFound):
        gym.delete_customer_by_id("999")
