import sys
from sys import path

path.append('../')
from controllers.main_controller import MainController

class MainMenu:
    #OPTION_MENU = {
    #    '1': show_members,
    #    '2': available_slots
    #}

    @classmethod
    def default_method(cls, *args, **kwargs):
        print('HELP MENU')

    @classmethod
    def available_slots(cls, **kwargs):
        pass

    @classmethod
    def show_options(cls,  current_user):
        options = '''
1: show_members,
2: available_slots
    '''
        print(options)
        option = input()
        #method_name = cls.OPTION_MENU.get(option, MainController.__dict__)
        #method_name(**{})
        # TODO decide what you want in this dict

        if option == '1':
            users = input('User you search:> ')
            members = cls.show_members(users)
            cls._pretty_print_members(members)
        elif option == '2':
            which_doctor = input('Which doctor:> ')
            cls.available_slots()



    @classmethod
    def show_members(cls, username):
        return MainController.show_members(username)

    @classmethod
    def  _pretty_print_members(cls, members):
        if members == None:
            sys.exit(2)
        for member in members:
            print('{status} {username}'.format(
                status = getattr(member, 'status', ''),
                username = member.username
))