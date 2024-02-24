from Car import Car
import pandas as pd


class User_Interface():
    @staticmethod
    def welcome_message():
        print('\n Welcome to Car Rental System \n')

    @staticmethod
    def print_main_menu_options():
        print('->Enter 1 to display the available cars')
        print('->Enter 2 to rent a Car')
        print('->Enter 3 to exit\n')

    @staticmethod
    def print_available_cars():
        file = pd.read_csv('Datasets/CarRentalDataV1.csv')
        make = file["vehicle.make"]
        model = file["vehicle.model"]
        print(file.columns)
        file['vehicle.make_model'] = make + ' ' + model
        print(sorted(file['vehicle.make_model'].unique()))

    def main_menu():
        User_Interface.print_main_menu_options()
        user_choice = int(input())

        if user_choice == 1:
            User_Interface.print_available_cars()
            User_Interface.main_menu()
