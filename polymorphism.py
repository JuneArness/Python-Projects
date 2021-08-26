#Parent Class Usaer
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password == self.password):
             print("Welcome back,)!".format(entry_name))
        else:
            print("The password or email is incorrect.")

    class Employee(User):
        base_pay = 11.00
        department = "General"
        pin_number = "3980"

    # This is the same method in the parent class "User".
    #The difference is that, instead of using entry_password, we're using entry_pin.

        def getLoginInfo(self):
            entry_name = input("Enter your name: ")
            entry_email = input("Enter your email: ")
            entryt_pin = input("Enter your pin: ")
            if (entry_email == self.email and entry_pin == self.pin_number):
                print("Welcome back, {}!".format(entry_name))
            else:
                print("The pin or email is incorrect")

    #The following code invokes the method inside each class for User and Employee.


    customer = User()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLogininfo()
