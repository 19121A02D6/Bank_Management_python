from bank_services import Bank
from ATM import ATM_service
class user():
        def use_bank():
                print("Welcome to Karunakar Bank Service Page... \n")
                while True:
                    user_input = input('''
            Press 1 for creating a new customer:
            Press 2 for logging in as an existing customer:
            Press 3 for displaying number of customers:
            Press 4 for changing pin:
            Press 5 for edit user details:
            Press 6 for exit\n
            Please enter your input =''')

                    if user_input == '1':
                        print('Create user')
                        Bank.new_cust()
                    elif user_input == '2':
                        Bank.login()
                    elif user_input == '3':
                        print('There currently', ATM_service.no_of_cust,'customers in Corporate bank.')
                    elif user_input == '4':
                        Bank.generate_pin()
                    elif user_input == '5':
                        Bank.change_userdata()
                    elif user_input == '6':
                        print('Exited')
                        break
                    else:
                        print('Invalid input try again')
                    print('\n*************************************************************\n')


if __name__ == '__main__':

    print("start \n")
    while True:
        user_input = input(''' 1 = for bank services, 2 = code writter details \n 0 = Exit page \n Please enter your input= ''')
        if user_input == '1':
                user.use_bank()
        elif  user_input == '2':
                print("Patike Karunakar Rao, Mobile Number = 8886109431, \n Please feel free to give feedback... Thank you for your interest.
        elif user_input == '0':
                break
        else:
                print("Invalid input... \n please try again \n \n")
