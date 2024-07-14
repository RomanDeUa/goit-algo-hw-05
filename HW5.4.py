# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Incorrect command format"
    return inner

# Функції для обробки команд бота
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            try:
                args = input("Enter the name and phone number: ").split()
                if len(args) != 2:
                    raise ValueError
                print(add_contact(args, contacts))
            except ValueError:
                print("Give me name and phone please")
        elif command == "phone":
            try:
                args = input("Enter the name: ").split()
                if len(args) != 1:
                    raise ValueError
                print(get_phone(args, contacts))
            except ValueError:
                print("Enter user name")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
