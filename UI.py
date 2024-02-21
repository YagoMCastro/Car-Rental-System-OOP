class User_Interface():
    @staticmethod
    def welcome_message():
        print('\n Welcome to Car Rental System \n')

    def main_menu():
        User_Interface.welcome_message()
        print('->Enter 1 to display the available cars')
        print('->Enter 2 to rent a Car')
        print('->Enter 3 to exit\n')
