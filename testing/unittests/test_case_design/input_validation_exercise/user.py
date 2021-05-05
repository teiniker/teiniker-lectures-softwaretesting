class ValidationError(Exception):
   pass    

class User:
    def __init__(self, id, username, password):
        if not isinstance(id, int):
                raise TypeError('Invalid id: wrong type!')
        if id < 0:
            raise ValueError('Invalid id: should be a positive number!')
        if len(username) < 5:
            raise ValueError('Invalid username: too short!')
        if len(password) < 12:
            raise ValidationError('Invalid password: too short!')

        self.id = id
        self.username = username
        self.password = password
