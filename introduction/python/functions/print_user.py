def user_to_string(username, password, group='user'):
    """Print username and passwort to the console."""
    return 'username:"{}" password:"{}" group:"{}"'.format(username, password, group)

def user_to_map(username, password, group='user'):
    """Collects a user's data in a map."""
    result = {'username':username, 'password':password, 'group':group}
    return result


# Positional Arguments
assert user_to_string('homer', 'Drink4DuffBeers') == 'username:"homer" password:"Drink4DuffBeers" group:"user"'

# Keyword Arguments
assert user_to_string(password='Drink4DuffBeers', username='homer') == 'username:"homer" password:"Drink4DuffBeers" group:"user"'

# (Overide default value)
assert user_to_string('homer', 'Drink4DuffBeers', 'admin') == 'username:"homer" password:"Drink4DuffBeers" group:"admin"'

# Map as return type 
result = user_to_map('homer', 'Drink4DuffBeers')
assert result['username'] == 'homer'
assert result['password'] == 'Drink4DuffBeers'
assert result['group'] == 'user'