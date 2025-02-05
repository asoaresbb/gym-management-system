from datetime import datetime
from gym import CustomerNotFound, Gym
from customer import Customer


def start_app():
    gym = Gym("Academia da Rebeca")

    while True:
        print("\n1. Registar novo cliente")
        print("2. Mostrar todos os clientes")
        print("3. Pesquisar cliente")
        print("4. Editar dados de cliente")
        print("5. Apagar cliente")
        print("6. Sair\n")
        option = input("Escolhe uma opção: ")

        if option == "1":
            _handle_register_customer(gym)

        elif option == "2":
            _handle_show_all_customers(gym)

        elif option == "3":
            _handle_search_customer(gym)

        elif option == "4":
            print("")

        elif option == "5":
            _handle_delete_customer_by_id(gym)

        elif option == "6":
            print("Até à próxima!")
            break

        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")


def _handle_delete_customer_by_id(gym: Gym):
    customers = gym.get_all_customers()
    _print_customers(customers)
    id = input("Qual é o id do cliente que deseja apagar? ")
    try:
        gym.delete_customer_by_id(id)
    except CustomerNotFound:
        print(f"Cliente com {id} nao encontrado.")


def _handle_search_customer(gym: Gym):
    name = input("Qual é o nome do cliente que deseja pesquisar? ")
    customers = gym.search_customer(name)
    if customers:
        _print_customers(customers)
    else:
        print(f"Cliente '{name}' não encontrado.")


def _print_customers(customers: list[Customer]):
    for customer in customers:
        print(f"{customer.id} {customer.name:<20} {customer.birthday}")


def _handle_register_customer(gym: Gym):
    name = input("Qual é o nome do cliente: ")
    date_str = input("Qual a data de nascimento do cliente (DD-MM-YYYY)? ")
    gym.register_customer(
        name=name,
        birthday=datetime.strptime(date_str, "%d-%m-%Y").date(),
    ),
    print(f"{name} registado com sucesso!")


def _handle_show_all_customers(gym: Gym):
    print("Clientes registados: ")
    customers = gym.get_all_customers()
    if customers:
        _print_customers(customers)
    else:
        print("Não há clientes registados.")


if __name__ == "__main__":
    start_app()
