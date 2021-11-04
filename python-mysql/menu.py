import helper
from database.connection import DAO
import manager

def main_menu():
    while True:
        helper.clear() # With this we can clean the terminal of windows, linux or MAC
        print('======================')
        print(" WELCOME TO THE MENU ")
        print('======================')
        print('[1] List clients')
        print('[2] Find clients')
        print('[3] Add clients') 
        print('[4] Modify clients')
        print('[5] Delete clients')
        print('[6] Exit')
        print('======================')
        
        option= input('Select an option > ')
        helper.clear()

        if option < '1' or option > '6':
            print('Wrong option, enter again')
        elif option == '6':
            print('Exiting the system...\n')
            break
        else:
            advanced_options(option)

        input('\nPress ENTER to continue...')
        
def advanced_options(option):
    dao = DAO()
    if option == '1':
        try:
            print('Listing clients: \n')
            client = dao.list_client()
            if len(client) > 0:
                manager.listclients(client)
            else:
                print('The requested data was not found')
        except:
            print('An error occurred')

    if option == '2':
        print('Find customer:\n')
        # Logic

    if option == '3':
        print('Adding client:\n')
        clients = manager.is_valid_client()
        try:
            if len(clients) > 0:
                dao.register_clients(clients)
            else:
                print('The requested data was not found')
        except:
            print('An error occurred')

    if option == '4':
        try:
            client = dao.list_client()
            print('List all: \n')
            if len(client) > 0:
                manager.update_data(client)
            else:
                print('The requested data was not found')
        except:
            print('An error occurred')
        
    if option == '5':
        try:
            client = dao.list_client()
            print('List all: \n')
            if len(client) > 0:
                remove_client= manager.data_deletion(client)
                if not (remove_client == ""):
                    dao.delete_client(remove_client)    
                else:
                    print('Client not found')
            else:
                print('The requested data was not found')
        except:
            print('An error occurred')
