class UserAlreadyExistsError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass

class PasswordsDontMatchError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class UserDoesNotExistsError(Exception):
    pass

class NotCorrectStatusError(Exception):
    pass