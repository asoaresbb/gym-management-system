import pytest

from gym.storage.users import Users


@pytest.fixture(autouse=True)
def temporary_database(tmp_path, monkeypatch):
    # O Banco cria o banco.db na pasta atual; isolar cada teste numa pasta temporária
    monkeypatch.chdir(tmp_path)


def test_select_existing_user():
    Users(nome="Ana", telefone="910000000", email="ana@example.com", usuario="ana", senha="x").insertUser()

    user = Users()
    message = user.selectUser("1")

    assert message == "Busca feita com sucesso!"
    assert user.idusuario == 1
    assert user.nome == "Ana"


def test_insert_user_sets_new_id():
    user = Users(nome="Ana", telefone="910000000", email="ana@example.com", usuario="ana", senha="x")

    user.insertUser()

    assert user.idusuario == 1


@pytest.mark.parametrize("nome", ["", "   "])
def test_insert_user_without_name_is_rejected(nome):
    user = Users(nome=nome, telefone="910000000")

    message = user.insertUser()

    assert message == "O nome é obrigatório."
    assert user.idusuario == 0
    assert Users().selectUser("1") == "Usuário não encontrado."


def test_select_nonexistent_user():
    user = Users()
    message = user.selectUser("999")

    assert message == "Usuário não encontrado."
