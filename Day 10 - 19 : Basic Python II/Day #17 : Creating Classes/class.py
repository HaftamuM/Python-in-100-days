#Creating your class - blue print 

#create a class
class User: 
    def __init__(self, user_id,username ): #must provide the parameters
        self.id = user_id
        self.username = username
    #initalise attribute 

#Creating a constructor or intilazation
user_1 = User("001", "Angela")
print(user_1.username)
print(user_1.id)

#creating an object from the class.. that is defines by the constructor
user_2 = User("002", "ahaftamu")
print(user_2.username)

#Creat an object 
#user_1 = User("001")
#Create an attribute 
#user_1.id = "00Stud1"
#user_1.username = "mola"

#print the attribute 
#print(user_1.id, user_1.user)

 

 
