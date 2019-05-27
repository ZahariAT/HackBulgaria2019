import sys
from sys import path

path.append('../')
from controllers.main_controller import MainController
from interface.main_menu import MainMenu
from utils.hospital_errors import *


class StartMenu:
    # sing in & sign up
    # redirect to Main menu
    @classmethod
    def run(cls):
        print("Welcome to Hospital Hack Bulgaria!")
        options = """
Do you want to sign in or sign up?
Options:
1 - sign in
2 - sign up
3 - exit
        """
        print(options)
        start_option = input()
        if start_option == '3':
            return
        # TODO check if the option number is correct
        username = input('Username:> ')
        password = input('Password:> ')
        if start_option == '1':

            # TODO hide password
            current_user = MainController.sign_in(username, password)
            if current_user:
                MainMenu.show_options(current_user)
            else:
                print("Wrong username or password!")
                sys.exit(1)
        elif start_option == '2':
            # TODO hide password
            second_password = input('Confirm Password:>')
            status = input('You are doctor or patient:> ' )
            if status == 'doctor':
                title = input('Title:> ')
                try:
                    current_user = MainController.sign_up(
                        username, password, second_password, status=status, title=title)
                except UserAlreadyExistsError:
                    print('Sign up failed! User already exists!')
                    sys.exit(1)
                except DatabaseConnectionError:
                    print('Sign up failed! Server error! Try again')
                    sys.exit(1)
                except PasswordsDontMatchError:
                    print('Sign up failed! Password don\'t match! Try again')
                    sys.exit(1)
                else:
                    MainMenu.show_options(current_user)
            elif status == 'patient':
                illness = input('Illness:> ')
                try:
                    current_user = MainController.sign_up(
                        username, password, second_password, status=status, illness=illness)
                except UserAlreadyExistsError:
                    print('Sign up failed! User already exists!')
                    sys.exit(1)
                except DatabaseConnectionError:
                    print('Sign up failed! Server error! Try again')
                    sys.exit(1)
                except PasswordsDontMatchError:
                    print('Sign up failed! Password don\'t match! Try again')
                    sys.exit(1)
                else:
                    MainMenu.show_options(current_user)
            else:
                print('-----In ELse------')
        else:
            sys.exit(1)

if __name__ == '__main__':
    print(MainController.sign_in('maha', '12334aaa'))