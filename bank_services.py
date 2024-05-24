from ATM import ATM_service
customer_details = {}              
    # account number is key and class object(customer account) is value
mobile_acc_link = {}            
    # use mobile number is key and account number is value, for verification
class Bank(ATM_service): #child class of ATM because I have used ATM as database
    def new_cust(): #to create new customer
        name = input('Enter the name of customer: ')
        mobile_no = int(input('Enter the mobile number of customer: '))
        DOB = input('Enter the Date Of Birth of customer(YYYY-MM-DD): ')
        pan_no = input('Enter the Pancard number of customer: ').upper()
        initial_depo = int(input('Enter the initial deposit amount: '))
        if initial_depo <= 0:
            print('Invalid Amount')
            return
        pin = int(input('Create PIN: '))
        customer = ATM_service(name=name, DOB=DOB, mobile_no=mobile_no, pan_no=pan_no, initial_depo=initial_depo, pin=pin)
        customer_details[customer.cust_acc_num] = customer                # acct. no. stored as key and object as value
        mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked
        print('New User Created!')
        print(f'Welcome {customer.name} to Karunakar Bank of India. {customer.cust_acc_num} is your account number')
        print(customer_details.items())


    def login():
        account_no = int(input('Enter your Account Number: '))
        account_pin = int(input('Enter your Account PIN: '))
        if account_no in customer_details.keys() and account_pin == customer_details[account_no].pin :
            print(f'\n{customer_details[account_no].name} Logged in')
            customer_details[account_no].basic_details()
            print("Welcome to ATM Service Page... \n")
            while True:
                user_input = input('''
                1 = deposit,\n
                2 = withdrawl,\n
                3 = money transfer,\n
                4 = Basic Details
                5 = log out \n
                Please enter your input =''')
                if user_input == '1':
                            customer_details[account_no].deposit()
                elif user_input == '2':
                            customer_details[account_no].withdrawl()
                elif user_input == '3':
                            mobile = int(input('Enter the mobile number of recepient: '))
                            if mobile in mobile_acc_link.keys():
                                secondary = mobile_acc_link[mobile]             # use mobile no. to get acct. no.
                                customer_details[account_no].transfer(customer_details[secondary])
                            else:
                                print('The mobile number you have enter does not have an account associated with it')
                elif user_input == '4':
                            customer_details[account_no].basic_details()
                elif user_input == '5':
                            print('Logged Out')
                            return
                else:
                            print('Invalid input try again')
                print('\n#############################################################\n')
        else:
            print('Account either not exist or the pin is wrong')
            return

    
    def generate_pin():
        account_no = int(input('Enter your Account Number: '))
        mobile_no = int(input('Enter your mobile number: '))
        if  account_no in customer_details.keys() and mobile_no == customer_details[account_no].mobile_no:
            pan_no = input('Enter your Pancard number: ').upper()
            if pan_no in customer_details[account_no].pan_no:
                DOB = input('Enter your Date Of Birth: ')
                if DOB in customer_details[account_no].DOB:
                    new_pin = int(input("Enter new pin code: "))
                    customer_details[account_no].pin = new_pin
                else:
                    print("invalid information. Can't Change the pin.")
            else:
                    print("invalid information. Can't Change the pin.")
        else:
                    print("invalid information. Can't Change the pin.")

    def change_userdata():
        account_no = int(input('Enter your Account Number: '))
        mobile_no = int(input('Enter your mobile number: '))
        if  account_no in customer_details.keys() and mobile_no == customer_details[account_no].mobile_no:
            name = input('Update the name of customer: ')
            mobile_no = int(input('Update mobile number of customer: '))
            DOB = input('Update Date Of Birth of customer(YYYY-MM-DD): ')
            pan_no = input('Update Pancard number of customer: ').upper()
            customer_details[account_no].name = name
            customer_details[account_no].mobile_no = mobile_no
            customer_details[account_no].DOB = DOB
            customer_details[account_no].pan_no = pan_no
        print('New User Details Updated!')
        print(f'Welcome {customer.name} to Karunakar Bank of India. {customer.cust_acc_num} is your account number')
        print(f'name : {customer_details[account_no].name} \n mobile number : {customer_details[account_no].mobile_no} \n Date Of Birth : {customer_details[account_no].DOB} \n pancard : {customer_details[account_no].pan_no}') 


