import hashlib

class PasswordHashTable:
    # print("hello world")
    def __init__(self,size):
       self.size=size
       self.table=[[] for _ in range(size)]  # table list 
      # hash function will create hash code
       
    def _hash_function(self, password):
        hashed_password= hashlib.sha256(password.encode()).hexdigest()
        return int(hashed_password[:16], 16) % self.size


    def insert(self,username,password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()[:16]
        index = self._hash_function(username)
        self.table[index].append((username, hashed_password))
        # adding to table
        # self.table[index].append((username,hashed_password))
        print("password saved..")
        print(self.table)


    def find(self,username):
        # hash_password= self._hash_function(password)
        index = self._hash_function(username)
        for pairs in self.table[index]:
            stored_username, stored_password= pairs
            if stored_username == username:
                print("password found")
                return stored_password
            

        return None    


password_table=PasswordHashTable(size=100)
# call the function 
password_table.insert("usama","password123")

print("\n")
# find password with username as key
value=password_table.find("usama")
print(value)


