import datetime
import random
import validation
import database
from getpass import getpass
now = datetime.datetime.now()

#Initial prompt for user. 
def init():
    print('Welcome to PWG Bank, current date and time is:')
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    haveAccount = int(input('Do you have an account with us?: 1 (Yes) 2 (No) \n'))

    if(haveAccount == 1):        
        login()
    elif(haveAccount ==2):        
        register()
    else:        
        print('You have selected an invalid option')
        init()

#User login
def login():
    print('*****You can now Login*****')
    accountNumberFromUser = input('What is your account number? \n')
    global userAccountNumber
    userAccountNumber = accountNumberFromUser
    
    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)

    if isValidAccountNumber:
        password = getpass('Please enter your password \n')

        user = database.authenticatedUser(accountNumberFromUser, password)
    
        if user:
            logFile = database.createLogFile(accountNumberFromUser)            
            bankOperation(user)

        print('Account number or password incorrect. Please try again')
        login()

    else:
        print('Invalid Account Number: Must have 10 digits and be an integer')
        init()
    
#Register if user does not have an account
def register():
    print('******REGISTER*******')    
    email = input('What is your email address? \n')
    fname = input('What is your first name? \n')
    lname = input('What is your last name? \n')
    password = getpass('Create a password for yourself \n')

    accountNumber = generateAccountNumber()    
    
    global balance
    balance = setBalance()
    isUserCreated = database.create(accountNumber, fname, lname, email, password, balance)

    if isUserCreated:
        print('Thank you ' + fname + ' Your Account Has been created')
        print('Your account number is: %d' % accountNumber)
        print('Please write it down and keep it safe')
        print('*****************************')
        recordBalance = database.recordBalance(accountNumber, balance)
        login()
    else:
        print('Something went wrong, please try again')
        register()

#Withdrawl Option
def withdrawl(user):
    withdrawlAmt = input('How much would you like to withdraw?')
    print('Take your cash.')
    newBalance = database.updateBalanceWithdrawl(userAccountNumber, balance, withdrawlAmt)
    bankOperation(user)

#Deposit Option, also show balance after deposit
def deposit(user):
    depositAmt = int(input('How much would you like to deposit?'))
    newBalance = database.updateBalanceDeposit(userAccountNumber, balance, depositAmt)
    bankOperation(user)

#User can file a complaint
def complaint(user):
    complaint = input('What issue would you like to report?')
    print('Thank you for contacting us.')
    bankOperation(user)

#Banking options
def bankOperation(user):
    print('*********MAIN MENU***********')
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))
    if(selectedOption == 1):
        print('You selected %s' % selectedOption + ': Withdrawl')
        withdrawl(user)
    
    elif(selectedOption == 2):
        print('You selected %s' % selectedOption + ': Deposit')
        deposit(user)
    
    elif(selectedOption == 3):
        print('You selected %s' % selectedOption + ': Complaint')
        complaint(user)

    elif(selectedOption == 4):
        print('You selected Exit, Goodbye!')
        deleteLogFile = database.deleteLogFile(userAccountNumber)
        exit()
            
    else:
        print('Invalid Option Selected, please try again.')
        bankOperation(user)

#Random account number generator
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)  

def setBalance():
    return random.randrange(0,1000)      

init()

