from Cars import Cars

class User_Interface():
    @staticmethod
    def welcome_message():
        print('\n Welcome to Car Rental System \n')

    @staticmethod
    def print_main_menu_options():
        print('->Enter 1 to display the available cars')
        print('->Enter 2 to rent a Car')
        print('->Enter 3 to exit\n')

    def main_menu():
        User_Interface.print_main_menu_options()
        user_choice = int(input())

        if user_choice == 1:
            print(sorted(Cars.available_cars))
            print('\nDone!')
            print()
            User_Interface.main_menu()
