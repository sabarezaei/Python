class User :
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user) :
        self.following +=1     # we follow a user so our following account goes up by one
        user.followers +=1     # and that user that we are following, their followers acount goes up by one
        
 
 
        
user1 = User(12,"Saba")
user2 = User (11, "Amine")


user1.follow(user2)


print(user1.following)