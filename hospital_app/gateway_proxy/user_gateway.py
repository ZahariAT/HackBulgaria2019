from sys import path

path.append('../')
from hospital.user import User
from hospital.doctor import Doctor
from hospital.patient import Patient
from gateway_proxy.gateway import Gateway
from utils.hospital_errors import *

class UserGateway(Gateway): #Singelton
    #create db, log, 
    def create_new_user(self, username, password, **kwargs): # self so it can have only one UserGateway like it has 1 object only
        try:
            if not self.find_existing_user(username):
                if kwargs['status'] == 'doctor':
                    self.db.add(Doctor(user_id=self.db.query(User.id).filter(User.username == username), title=kwargs['title']))
                elif kwargs['status'] == 'patient':
                    self.db.add(Patient(user_id=self.db.query(User.id).filter(User.username == username), illness=kwargs['illness']))
                #self.log.info(f'New user was created - {username}')
                else:
                    raise NotCorrectStatusError(kwargs['status'])
                self.db.add(User(username=username, password=password, status=kwargs['status']))
            else:
                raise UserAlreadyExistsError(username)
        except DatabaseConnectionError:
            sys.exit(1)
        self.db.commit()
        return True

    def find_existing_user(self, username):
        q = self.db.query(User).filter(User.username == username).all()
        return q

    def find_all(self):
        return self.db.find_all(User)

    def delete(self, username):
        try:
            if self.find_existing_user(username):
                stat = self.db.query(User.status).filter(User.username == username).one()[0]
                if stat == 'doctor':
                    self.db.query(Doctor).filter(Doctor.user_id == self.db.query(User.id).\
                        filter(User.username == username).one()[0]).delete()
                else:
                    self.db.query(Patient).filter(Patient.user_id == self.db.query(User.id).\
                        filter(User.username == username).one()[0]).delete()
                self.db.query(User).filter(User.username == username).delete()
            else:
                raise UserDoesNotExistsError(username)
        except DatabaseConnectionError:
            sys.exit(1)
        self.db.commit()
        return True

    def find(self, username, password):
        user = self.db.query(User).filter_by(username=username, password=password).one_or_none() #returns None if no user was found while just one() returns sqlalchemy.orm.exc.NoResultFound: No row was found for one()
        return user

#update('Pand', email='panda@aaa.com')
    def update(self, username, **params): 
    #TODO update also Doctor/Patient
        try:
            if not self.find_existing_user(username):
                self.db.query(User).filter(User.username == username).\
                    update(params, synchronize_session=False)
            else:
                raise UserDoesNotExistsError(username)
        except dataIntegrityError:
            self.log.exception(exp)  #we don't print in a project, we signal that we have detected some error but don't want to stop the hole project
        self.db.commit()
        return True

        #createsession.query(MyClass).filter_by(name = 'some name')
        #find
        #delete
        #update(table_name, (username, email), ('roza', 'ra@abv.bg')))

if __name__ == '__main__':
    pass
    #UserGateway().create_new_user(username='zaha', password='12334aaa', status='doctor', title='ochen')
    #UserGateway().delete('zaha')
    #UserGateway().find('zaha', '12334aa')
    #UserGateway().create_new_user(username='graha', password='12334bbb', status='patient', illness='ochen')