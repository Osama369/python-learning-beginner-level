# This application is based on python oops and mysql database V.1.0
import hashlib
import mysql.connector
import tabulate

class HashTable:
    # constructor to initailied the object

    def __init__(self) :
       try:
            self.connection=mysql.connector.connect(
              host='localhost',
              user='root',
              password='',
              database='passwordmanager'

           )
            self.cursor=self.connection.cursor()
            print("connected to database..")
       except mysql.connector.Error as errors:
           print(" error while connecting to database ", errors)               

    def is_connected(self):
        if self.connection and self.connection.is_connected():
            return True
        return False

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection to MySQL database is closed")

    def hash(self,password):
        hash_password=hashlib.sha256(password.encode()).hexdigest()
        return(hash_password[:16])      
        
    def insert(self, username, password):
        if not self.is_connected():
            print("Not connected  to database")
            return
        try:
          sql= 'INSERT INTO hashtable (username, password) VALUES (%s, %s)'
          hashed_password= self.hash(password)
          values=(username, hashed_password)
          self.cursor.execute(sql,values)
          self.connection.commit()
          print("Password inserted successfully.")
        except mysql.connector.Error as error:
            print("Error while inserting password:", error)  

    def find(self,username):
        if not self.is_connected():
            print("Not connected  to database")
            return
        try:
            sql= 'SELECT username, password FROM hashtable WHERE username = %s'
            values=(username,)
            self.cursor.execute(sql,values)
            rows = self.cursor.fetchall()
            headers = ['Username', 'Password']
            table = tabulate.tabulate(rows, headers, tablefmt='grid')
            print(table)
            
        except mysql.connector.Error as error:
            print("Error while finding password:", error)


    def find_all(self):
      try:  
        sql = 'SELECT username, password FROM hashtable'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        headers = ['Username', 'Password']
        table = tabulate.tabulate(rows, headers, tablefmt='grid')
        print(table)       
      except mysql.connector.Error as error:
            print("Error while finding password:", error)

    def auth(self,username,password):
     try:  
        hashed_password=self.hash(password)
        sql = 'SELECT * FROM hashtable WHERE username = %s AND password = %s'  
        values=(username,hashed_password)
        self.cursor.execute(sql,values)
        row=self.cursor.fetchall()
        if row:
            return True
        return False
     except mysql.connector.Error as errors:
         print(errors)         

hash_table=HashTable()
#calling functions
# hash_table.insert("fahad","fahad123")
# hash_table.find_all() 
hash_table.close()





        
       
