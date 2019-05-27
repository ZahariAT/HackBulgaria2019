import hashlib
from sys import path

path.append('../')
from utils.hospital_errors import *
from gateway_proxy.user_gateway import UserGateway

class MainController:
    @classmethod
    def sign_in(cls, username, password):
        cls._validate_password(password)
        password = cls._hash_password(username, password)
        current_user = UserGateway().find(username, password)
        return current_user

    @classmethod
    def sign_up(cls, username, password, second_password, **params):
        cls._validate_password(password)
        cls._validate_password(second_password)

        hashed_pass1 = cls._hash_password(username, password)
        hassed_pass2 = cls._hash_password(username, second_password)
        cls._do_passwords_match(hashed_pass1, hassed_pass2)

        if UserGateway().find(username, password):
            raise UserAlreadyExistsError

        return UserGateway().create_new_user(username, hashed_pass1, **params)

    @classmethod
    def show_members(cls, current_user): #TODO return list with more than one memeber
        if cls.is_doctor(current_user):
            return cls.show_patients(current_user)
            #  [Patient('Roza'), Patient('Mimi')]
        else:
            return cls.show_doctors(current_user)

    @classmethod
    def _validate_password(cls, password):
        if len(password) < 8 or password.isdigit():
            raise InvalidPasswordError


    @classmethod
    def _hash_password(cls, username, password):
        #salt = username + database_decoder + user_decoder  ## database_decoder is secret and it's not in database
        dk = hashlib.pbkdf2_hmac('sha256', password.encode(), f'{username} more salt'.encode(), 10000).hex()
        return dk

    @classmethod
    def _do_passwords_match(cls, password, second_password):
        return password == second_password
    
    @classmethod                      #TODO make it part of gateway, not controller and to be object method
    def is_doctor(cls, current_user):
        return True

    @classmethod
    def delete_profile(cls, current_user, password):
        hashed_pass = cls._hash_password(password)
        if not UserGateway().find(current_user, hashed_pass):
            raise UserDoesNotExistsError(username)
        UserGateway().delete(current_user)

    @classmethod
    def show_doctors(cls, current_user):
        pass

    @classmethod
    def show_patients(cls, current_user):
        pass

    @classmethod
    def available_slots(cls, **kwargs):
        pass

if __name__ == '__main__':
    #print(MainController.sign_up('maha', '12334aaa', '12334aaa', status='patient', illness='Disco'))
    print(MainController.sign_in('maha', '12334aaa'))