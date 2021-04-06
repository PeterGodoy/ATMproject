import datetime
import random
now = datetime.datetime.now()

database = {} #database

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
    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('Please enter your password \n')

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation()
    else:
        print('Account number or password incorrect. Please try again')
        login()
    
#Register if user does not have an account
def register():    
    print('******REGISTER*******')    
    email = input('What is your email address? \n')
    fname = input('What is your first name? \n')
    lname = input('What is your last name? \n')
    password = input('create a password for yourself \n')

    accountNumber = generateAccountNumber()
    database[accountNumber] = [ fname, lname, email, password ]

    print('Thank you ' + fname + 'Your Account Has been created')
    print('Your account number is: %d' % accountNumber)
    print('Please write it down and keep it safe')
    print('*****************************')

    login()

#Withdrawl Option
def withdrawl():
    withdrawlAmt = input('How much would you like to withdraw?')
    print('Take your cash.')
    bankOperation()

#Deposit Option, also show balance after deposit
def deposit():
    depositAmt = int(input('How much would you like to deposit?'))
    print('Your new balance is $' + str(depositAmt))
    bankOperation()

#User can file a complaint
def complaint():
    complaint = input('What issue would you like to report?')
    print('Thank you for contacting us.')
    bankOperation()

#Banking options
def bankOperation():
    print('*********MAIN MENU***********')
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))
    if(selectedOption == 1):
        print('You selected %s' % selectedOption + ': Withdrawl')
        withdrawl()
    
    elif(selectedOption == 2):
        print('You selected %s' % selectedOption + ': Deposit')
        deposit()
    
    elif(selectedOption == 3):
        print('You selected %s' % selectedOption + ': Complaint')
        complaint()

    elif(selectedOption == 4):
        print('You selected Exit, Goodbye!')
        exit()
    
    else:
        print('Invalid Option Selected, please try again.')
        bankOperation()

#Random account number generator
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)        

init()

