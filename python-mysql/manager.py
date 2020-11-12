
def listclients(clients):
    cont=1
    for i in clients:
        data= "{0}. DNI: {1}  | First name: {2}  | Last name: {3}"
        print(data.format(cont, i[3], i[1], i[2] ))
        cont +=1
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
                 print('The DNI field cannot have more or less than 9 alphanumeric characters.')
                 print('Please login again\n')
        else:
            print('The first name, last name and DNI field cannot be empty.')
            print('Please login again\n')
    
    client= (first_name,last_name,dni)
    return client

    

def data_deletion(clients):
    listclients(clients)
    exists_client=False
   
    client_to_delete= input('Enter the DNI of the customer to remove: ')
        
    for client in clients:
        #print(c[3])
        if client[3] == client_to_delete:
            exists_client=True
            break
        
    if not exists_client:
        client_to_delete= ""

    return client_to_delete



# def data_update(clients):
#     listclients(clients)
#     exists_client=False

#     client_to_update=input('Introduzca el first name del cliente que desea actualizar')

#     for u in clients:
#         if u[1] == client_to_update:
#             exists_client=True
#             break


#     if not exists_client:
#        client_to_update= ""

#     clients_f=input()


