from database.connection import DAO


def listclients(clients):
    #cont=1
    for i in clients:
        data= "ID:{0}.- DNI: {1}  | First name: {2}  | Last name: {3}"
        print(data.format(i[0], i[3], i[1], i[2] ))
        #cont +=1
    print(" ")



def is_valid_client():
    while True:
        first_name= str(input('Please enter your first name: '))
        last_name=str(input('Please enter your last name: '))
        dni= str(input('Enter your DNI: ').upper())
        print(" ")
        if len(first_name) > 0 and  len(last_name) > 0 and len(dni) > 0:
            if len(dni) == 9:
                break
            else:
                 print('***The DNI field cannot have more or less than 9 alphanumeric characters.***')
                 print('Please login again\n')
        else:
            print('The first name, last name and DNI field cannot be empty.')
            print('Please login again\n')
    
    client= (first_name,last_name,dni)
    return client

    

def data_deletion(clients):
    listclients(clients)
    exists_dni=False
   
    client_to_delete= input('Enter the DNI of the customer to remove: ')
        
    for client in clients:
        if client[3] == client_to_delete:
            exists_dni=True
            break
        
    if not exists_dni:
        client_to_delete= ""

    return client_to_delete




def update_data(clients):
    dao= DAO()
    listclients(clients)
    exists_id=False
    while not (exists_id):
        client_id=int(input('Enter the ID you want to update: '))    
        for i in clients:
            if i[0] == client_id:
                print(dao.find_client(client_id))
                exists_id=True
                break 
        if not exists_id:
            print('***Id not found***')


    client_first_n= input('Enter new name: ')
    client_last_n= input('Enter new last name: ')
    while True:
        client_dni= input('Enter new DNI: ')
        print("")
        if len(client_dni) == 9:
            break
        else:
            print('***The DNI field cannot have more or less than 9 alphanumeric characters.***')
            print('Please login again\n')
        

    return dao.update_client(client_id,client_first_n,client_last_n,client_dni)



