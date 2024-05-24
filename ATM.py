class ATM_service():

    no_of_cust = 0
    acc_num = 121200
    def __init__(self, name, DOB, mobile_no, pan_no, initial_depo, pin):
        
        self.name                 = name
        self.cust_acc_num         = ATM_service.acc_num
        self.mobile_no            = mobile_no
        self.acc_balance          = initial_depo
        self.pin                  = pin
        self.DOB                  = DOB
        self.pan_no               = pan_no
        
        ATM_service.acc_num       = ATM_service.acc_num + 1
        ATM_service.no_of_cust    = ATM_service.no_of_cust + 1

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ₹{self.acc_balance}')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance      = self.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def transfer(self, other):
        amount = int(input('Enter the Transaction amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            other.acc_balance     = other.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')
    
