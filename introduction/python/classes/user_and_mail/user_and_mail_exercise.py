# Exercises: Classes, Dunder Methods
# 
# A) Implement the class Mail which holds an email address.
# B) Implement the class User which stores: id, username, password 
#    and a Mail instance.

class Mail():
    """Model of an email address."""
    pass
    

class User():
    """Model of a user."""
    pass


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
