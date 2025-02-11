from customer import Customer
from fitnessGym import CustomerNotFound, FitnessGym


def start_app():
    vivaGym = FitnessGym("VivaGym Academy")

    while True:
        print("\n1. Register new client")
        print("2. Show all clients")
        print("3. Search client")
        print("4. Edit client info")
        print("5. Delete client")
        print("6. Exit\n")
        option = input("Choose an option: ")

        if option == "1":
            _handle_register_customer(vivaGym)

        elif option == "2":
            _handle_show_all_customers(vivaGym)

        elif option == "3":
            _handle_search_customer(vivaGym)

        elif option == "4":
            _handle_edit_customer_by_id(vivaGym)

        elif option == "5":
            _handle_delete_customer_by_id(vivaGym)

        elif option == "6":
            print("See you later!")
            break

        else:
            print("Invalid option! Choose between 1 and 6.")


def _handle_register_customer(vivaGym: FitnessGym):
    name = input("What's client name: ")
    phoneNumber = input("What's client number: ")
    email = input("What's client e-mail: ")
    user = input("What's client username: ")
    password = input("What's client password: ")

    customer = Customer(id="", name=name, phoneNumber=phoneNumber, email=email, user=user, password=password)
    vivaGym.register_customer(customer)

    print(f"{name} registered with success!")


def _print_customers(customers: list[Customer]):
    for customer in customers:
        print(
            f"{customer.id} {customer.name:<20} {customer.phoneNumber:<12} {customer.email:<20} {customer.user:<8} {customer.password:<12}")


def _handle_show_all_customers(vivaGym: FitnessGym):
    print("Registered clients: ")
    customers = vivaGym.get_all_customers()
    if customers:
        _print_customers(customers)
    else:
        print("There is no registered clients.")


def _handle_search_customer(vivaGym: FitnessGym):
    name = input("Which client are you trying to find? ")
    customers = vivaGym.get_customer_by_name(name)
    if customers:
        _print_customers(customers)
    else:
        print(f"Client '{name}' not found.")


def _handle_edit_customer_by_id(vivaGym: FitnessGym):
    customers = vivaGym.get_all_customers()
    _print_customers(customers)
    id = input("Which is the Id of the client you want to edit? ")
    try:
        vivaGym.get_customer_by_id(id)
        name = input("What's the new name?")
        phoneNumber = input("What's client new number: ")
        email = input("What's client new e-mail: ")
        user = input("What's client new username: ")
        password = input("What's client new password: ")
        vivaGym.edit_customer_by_id(id, name, phoneNumber, email, user, password)
    except CustomerNotFound:
        print(f"Client with Id {id} not found.")


def _handle_delete_customer_by_id(vivaGym: FitnessGym):
    customers = vivaGym.get_all_customers()
    _print_customers(customers)
    id = input("Which is the Id of the client you want to delete? ")
    try:
        vivaGym.delete_customer_by_id(id)
    except CustomerNotFound:
        print(f"Client with Id {id} not found.")


if __name__ == "__main__":
    start_app()
