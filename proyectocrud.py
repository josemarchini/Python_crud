
clients = "pablo,ricardo."

def _add_comma():
    global clients

    clients += ","

def create_client(client_name):
    global clients

    clients += client_name
    _add_comma()

def list_clients():
    global clients

    print(clients)


def _print_welcome():
    print("WELCOME TO OTTO CLIENTS")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[D]elete client")

if __name__=="__main__":
    _print_welcome()

    command = input()

    if command == "C":
        client_name = input("What is the client name: ")
        
        create_client(client_name)
        list_clients()
    
    elif command == "D":
        pass
    else:
        print("Invalid command")

    

