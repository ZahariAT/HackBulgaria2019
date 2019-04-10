import unittest
import decorators
import os
import tempfile
import time
import datetime

class testDecorators(unittest.TestCase):

    '''accepts decorator takes types 
    and checks if the types of the func arguments coincides with decorators arguments'''

    def test_say_hello_with_string_argv_with_accepts_decorator_taking_str(self):
        actual_result = decorators.say_hello('Pesho')
        expected_result = 'Hello, I am Pesho'
        self.assertEqual(actual_result, expected_result)

    def test_say_hello_with_not_string_argv_with_accepts_decorator_taking_str(self):
        with self.assertRaises(TypeError): #or self.assertRaises(Exception, lambda:func())
            decorators.say_hello(1)

    def test_deposit_with_name_type_str_and_money_type_int_given_in_accepts_return_True(self):
        self.assertEqual(decorators.deposit('Az', 0), True)

    def test_deposit_with_name_and_money_types_incorrect_and_decorator_accepts_raises_TypeError(self):
         with self.assertRaises(TypeError): #or self.assertRaises(Exception, lambda:func())
            decorators.deposit(1, 2)

    '''encrypt is a decorator which takes key and then you decorate functions which are returning string 
    by encrypting them in Caesar Cipher with the key the passes in encrypt'''

    def test_if_encrypt_decoretor_works_with_key_2(self):
        @decorators.encrypt(2)
        def return_hello():
            return 'Hello'
        self.assertEqual(return_hello(), 'Jgnnq')

    '''
    performance and log decorators are similar for testing. Only if I knew how to test them
    '''
    def test_log_which_takes_file_and_writes_in_it(self): #it fails couse of few seconds
        @decorators.log('log.txt')
        def get_low():
            return 'Get get get low'
        get_low()
        with open('log.txt') as f:
            lines = f.readlines()
        self.assertEqual(lines[-1], 'get_low was called at {}'.format(datetime.datetime.now()))

    def test_performance_which_takes_file_and_decorates_func_by_writing_in_the_file_func_name_and_the_date_it_was_called(self):
        'no idea how but tried'
        @decorators.performance('log.txt')
        def something_heavy():
            time.sleep(2)
            return 'I am done!'

       # something_heavy()
       # with open('log.txt') as f:
       #     lines = f.readlines()
        

    def test_if_something_heavy_returns_the_string_I_am_done(self):
        self.assertEqual('I am done!', decorators.something_heavy())



'''
import os
import tempfile

fd, path = tempfile.mkstemp()
try:
    with os.fdopen(fd, 'w') as tmp:
        # do stuff with temp file
        tmp.write('stuff')
finally:
    os.remove(path)

with tempfile.TemporaryFile() as fp:
    fp.write('Hello world!')
    fp.seek(0)
    fp.read()'''

if __name__=='__main__':
    unittest.main()