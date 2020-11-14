import mysql.connector
from mysql.connector import Error
from .base import get_secret


class DAO:

    def __init__(self):
        try:
            self.myconnection= mysql.connector.connect(
                port=get_secret('PORT'),
                user=get_secret('USER'),
                password=get_secret('PASSWORD'),
                database=get_secret('DATABASE'),  
                auth_plugin=get_secret('AUTH_PLUGIN')
            )
            # if self.myconnection.is_connected():
            #     print('Successful connection')

                
        except Error as ex:
            print(f'Error during connection:{ex}')


        # finally:
        #     if self.myconnection.is_connected():
        #         self.myconnection.close()
        #         print('the conexion to finalized')
    
    def list_client(self):
        if self.myconnection.is_connected():
            try:
                cursor= self.myconnection.cursor()
                cursor.execute("SELECT * FROM Customer ORDER BY id ASC")
                result=cursor.fetchall()
                return result

            except Error as ex:
                print(f'Error during connection:{ex}')

    def find_client(self,Id):
        if self.myconnection.is_connected():
            try:
                cursor= self.myconnection.cursor()
                sql="SELECT * FROM Customer WHERE id={}"
                cursor.execute(sql.format(Id))
                result=cursor.fetchone()
                return result

            except Error as ex:
                print(f'Error during connection:{ex}')


    def register_clients(self,values):
        if self.myconnection.is_connected():
            try:
                cursor= self.myconnection.cursor()
                sql= "INSERT INTO Customer (first_name,last_name,dni) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(values[0], values[1],values[2]))
                self.myconnection.commit()
                print("")
                print("Successfully added customer\n")

            except Error as ex:
                print(f'Error during connection:{ex}')  


    def update_client(self,Id,first_name,last_name,dni):
        if self.myconnection.is_connected():
            try:
                cursor= self.myconnection.cursor()
                sql= "UPDATE Customer SET first_name='{}',last_name='{}',dni='{}' WHERE id={}"
                cursor.execute(sql.format(first_name,last_name,dni,Id))
                self.myconnection.commit()
                print("Cliente actualizado\n")

            except Error as ex:
                print(f'Error durante la conexion:{ex}') 



    def delete_client(self,code_delete):
        if self.myconnection.is_connected():
            try:
    
                cursor= self.myconnection.cursor()
                sql= "DELETE FROM Customer WHERE dni= '{0}'"
                cursor.execute(sql.format(code_delete))
                self.myconnection.commit()
                print("Customer removed\n")

            except Error as ex:
                print(f'Error during connection::{ex}') 
