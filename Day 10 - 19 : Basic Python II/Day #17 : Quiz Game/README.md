##Learning how to create a class, constructor and method in python
##Creating your class - blue print 

#create a class
class User: 
    def __init__(self, user_id,username ): #must provide the parameters
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 
   # creating a method def followers(self, user):
        
#Creating a constructor or intilazation
user_1 = User("001", "Angela")
print(user_1.username)
print(user_1.id)

#creating an object from the class.. that is defines by the constructor
user_2 = User("002", "hafftamu")
print(user_2.username)



 

 
