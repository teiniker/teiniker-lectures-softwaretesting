class Mail():
    """Model of an email address."""

    def __init__(self, address):
        self._address = address              

    def get_address(self):
        return self._address

    def __repr__(self):
        return "Mail('{}')".format(self.get_address())

    def __str__(self):
        return 'Mail: address={}'.format(self.get_address())    

    def __eq__(self, other):
        if self._address == other._address :
            return True
        else:
            return False


class User():
    """Model of a user."""

    def __init__(self, id, username, password, mail):
        self._id = id
        self._username = username          
        self._password = password    
        self._mail = mail

    def get_id(self):
        return self._id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_mail(self):
        return self._mail

    def __repr__(self):
        return "User({}, '{}', '{}', {})".format(self.get_id(), self.get_username(), self.get_password(), repr(self.get_mail()))

    def __str__(self):
        return "User: id={}, username='{}', mail='{}'".format(self.get_id(), self.get_username(), self.get_mail().get_address())    

    def __eq__(self, other):
        if self._id == other._id:
            return True
        else:
            return False


# Verify Mail 

m = Mail('homer.simpson@springfield.com')
assert 'homer.simpson@springfield.com' == m.get_address()

assert "Mail('homer.simpson@springfield.com')" == repr(m)

assert 'Mail: address=homer.simpson@springfield.com' == str(m)

m2 = Mail('homer.simpson@springfield.com')
assert m == m2 


# Verify User

u = User(7, 'homer', ')jh%6Zgur5)r', m)
assert 7 == u.get_id()
assert 'homer' == u.get_username()
assert ')jh%6Zgur5)r' == u.get_password()
assert 'homer.simpson@springfield.com' == u.get_mail().get_address()

assert "User(7, 'homer', ')jh%6Zgur5)r', Mail('homer.simpson@springfield.com'))" == repr(u)

assert "User: id=7, username='homer', mail='homer.simpson@springfield.com'" == str(u) 
