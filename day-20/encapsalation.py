class Snapchat:
    def __init__(self,username,password,friends):
        self.username = username 
        self.__password = password
        self._friends = friends
    def getpassword(self):
        return self.__password
    def setpassword(self,new_passowrd):
        self.__password = new_passowrd
    @property
    def oprFriend(self):
        return self._friends
    @oprFriend.setter
    def oprFriends(self,new_friends):
        return self._friends.append(new_friends)

saaketh = Snapchat('saaketh', '1234', ['praveen','nihkil'])
print(f'Name before modifaication {saaketh.username}')
saaketh.username = 'sapnil'
print(f'naame after modification {saaketh.username}')
print(f'Passowrd before modification {saaketh.getpassword()}')
saaketh.setpassword('S@1234')
print(f'Passowrd before modification {saaketh.getpassword()}')
print(f'Your Friends {saaketh.oprFriend}')
saaketh.oprFriends = 'abhi'
print(f'updated friends {saaketh.oprFriends}')