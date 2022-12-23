class BasePasswordManager:
    old_passwords=['testing']

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self,password):
        return self.get_password==password

class PasswordManagr(BasePasswordManager):
    
    def set_password(self,new_password):
        if len(new_password)<6:
            return "Password can't be set as it less than 6 characters"
        if self.get_level(self.get_password())<self.get_level(new_password):
            self.old_passwords.append(new_password)
            return "Password has been updated sucessfully with security level ",self.get_level()
        
    def get_level(self,password=None):
        print(password)
        if password==None:
            password=self.get_password()
        if password.isalpha() or password.isnumeric():
            return 1
        elif password.isalnum():
            return 2
        else:
            return 3

a=BasePasswordManager()
new_password=input('Enter the Password:  ')
if new_password==a.get_password():
    print('Previous password is same')
else:
    b=PasswordManagr()
    print(b.set_password(new_password))
