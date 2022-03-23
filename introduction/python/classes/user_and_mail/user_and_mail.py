class Mail():
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f"Mail('{self.address}')"

    def __str__(self):
        return f"Mail: address='{self.address}'"

    def __eq__(self, other):
        return self.address == other.address


class User():
    """Model of a user having only one mail addresse."""

    def __init__(self, id, username, password, mail):
        self.id = id
        self.username = username
        self.password = password
        self.mail = mail

    def __repr__(self):
        return f"User({self.id}, '{self.username}', '{self.password}', {repr(self.mail)})"

    def __str__(self):
        return f"User: id={self.id}, username='{self.username}', mail='{self.mail.address}'"

    def __eq__(self, other):
        return self.id == other.id


# Verify Mail

m1 = Mail('homer.simpson@springfield.com')
assert 'homer.simpson@springfield.com' == m1.address
assert "Mail('homer.simpson@springfield.com')" == repr(m1)
assert "Mail: address='homer.simpson@springfield.com'" == str(m1)

m2 = Mail('homer.simpson@springfield.com')
assert m1 == m2


# Verify User

u = User(7, 'homer', ')jh%6Zgur5)r', m1)
assert 7 == u.id
assert 'homer' == u.username
assert ')jh%6Zgur5)r' == u.password
assert 'homer.simpson@springfield.com' == u.mail.address

assert "User(7, 'homer', ')jh%6Zgur5)r', Mail('homer.simpson@springfield.com'))" == repr(u)

assert "User: id=7, username='homer', mail='homer.simpson@springfield.com'" == str(u)
