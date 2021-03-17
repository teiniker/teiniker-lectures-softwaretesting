class Mail():
    def __init__(self, address):
        self.address = address              

    def __repr__(self):
        return "Mail('{}')".format(self.address)

    def __str__(self):
        return 'Mail: address={}'.format(self.address)    

    def __eq__(self, other):
        if self.address == other.address :
            return True
        else:
            return False


class User():
    def __init__(self, id, username, password, mail):
        self.id = id
        self.username = username          
        self.password = password    
        self.mail = mail

    def __repr__(self):
        return "User({}, '{}', '{}', {})".format(self.id, self.username, self.password, repr(self.mail))

    def __str__(self):
        return "User: id={}, username='{}', mail='{}'".format(self.id, self.username, self.mail.address)    

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False


# Verify Mail 

m = Mail('homer.simpson@springfield.com')
assert 'homer.simpson@springfield.com' == m.address

assert "Mail('homer.simpson@springfield.com')" == repr(m)

assert 'Mail: address=homer.simpson@springfield.com' == str(m)

m2 = Mail('homer.simpson@springfield.com')
assert m == m2 


# Verify User

u = User(7, 'homer', ')jh%6Zgur5)r', m)
assert 7 == u.id
assert 'homer' == u.username
assert ')jh%6Zgur5)r' == u.password
assert 'homer.simpson@springfield.com' == u.mail.address

assert "User(7, 'homer', ')jh%6Zgur5)r', Mail('homer.simpson@springfield.com'))" == repr(u)

assert "User: id=7, username='homer', mail='homer.simpson@springfield.com'" == str(u) 
