class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username          
        self.password = password    

    def __str__(self):
        return "User: id={}, username='{}'".format(self.id, self.username)    

    def __eq__(self, other):
        return self.id == other.id


class UserTable():
    def __init__(self):
        self.users = []

    def insert(self, user):
        self.users.append(user)

    def find_by_id(self, id):
        for user in self.users:
            if user.id == id:
                return user        
        return None

    def find_all(self):
        return self.users


# Verify implementations

bart1 = User(1, 'bart', 'EatMyShorts!')
bart2 = User(1, 'bart', '#Kig%/5gT54$§')
assert bart1 == bart2
assert "User: id=1, username='bart'" == str(bart1)

homer = User(3, 'homer', 'MoreDuff4Me!')
marge = User(7, 'marge', 'Kh7gT.9/8#gH')

table = UserTable()
table.insert(homer)
table.insert(marge)

assert 'marge' == table.find_by_id(7).username
assert 'homer' == table.find_by_id(3).username

assert 2 == len(table.find_all())
