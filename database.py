# Create record
# Read record
# Update Record
# Delete record
#CRUD

#find user

import os
import validation

userDbPath = "C:/Users/Sixfingered/RAProjects/ATMproject/data/user_record/"
logFile = "C:/Users/Sixfingered/RAProjects/ATMproject/data/auth_session/"
userBalance = "C:/Users/Sixfingered/RAProjects/ATMproject/data/user_balance/"

def create(accountNumberFromUser, fname, lname, email, password, balance):
    userData = fname + ',' + lname + ',' + email + ',' + password + ',' + str(balance)
    if doesAccountNumberExist(accountNumberFromUser):
        return False

    if doesEmailExist(email):
        print('Email already exists')
        return False

    completionState = False
    try:
        f = open(userDbPath + str(accountNumberFromUser) + '.txt', 'x')
    
    except FileExistsError:
        print('User already exists')
        doesFileContainData = read(userDbPath + str(accountNumberFromUser) + '.txt')
        if not doesFileContainData:
            delete(accountNumberFromUser)
        # delte the already created file, print out error, then return false
        # check content of file before deleting
                
    else:
        f.write(str(userData))
        completionState = True
    finally:
        f.close()
        return completionState
   
    #create a file
    # name of the file would be accountNumberFromUser.txt
    # add the user details to the file
    #return true
    # if saving to file fails, then delete created file

def read(accountNumberFromUser):
    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)

    try:
        if(isValidAccountNumber):
            f = open(userDbPath + str(accountNumberFromUser) + '.txt', 'r')
        else:
            f = open(userDbPath + accountNumberFromUser, 'r')

    except FileNotFoundError:
        print('User not found')
    except FileExistsError:
        print('User does not exist')
    except TypeError:
        print('Invalid account number format')
    else:    
        return f.readline()
    
    return False
    
    # find user with account number
    # fetch the contents of the file

def update(accountNumberFromUser):
    print('Update user record')
    # find user with account number
    # fetch the contents of the file
    # update the content of the file
    # save the file

def delete(accountNumberFromUser):
    isDeleteSuccessful = False

    if os.path.exists(userDbPath + str(accountNumberFromUser) + '.txt'):
        try:
            os.remove(userDbPath + str(accountNumberFromUser) + '.txt')
            isDeleteSuccessful = True
        except FileNotFoundError:
            print('User not found')
        finally:
            return isDeleteSuccessful


    # find user with account number
    # delete the user record (file)
    # return true

def doesEmailExist(email):

    allUsers = os.listdir(userDbPath)

    for user in allUsers:
        userList = str.split(read(user), ',')
        if email in userList:
            return True
    return False
        
    
    # find user record in the data folder
    #Could be used to retreive password via email and password. 

def doesAccountNumberExist(accountNumberFromUser):

    allUsers = os.listdir(userDbPath)

    for user in allUsers:
        if user == str(accountNumberFromUser) + '.txt':
            return True
    return False

def authenticatedUser(accountNumberFromUser, password):

    if doesAccountNumberExist(accountNumberFromUser):
        
        user = str.split(read(accountNumberFromUser), ',')
        if password == user[3]:
            return user

    return False

def createLogFile(accountNumberFromUser):
# Creates a log file in auth_session

    if doesAccountNumberExist(accountNumberFromUser):
        f = open(logFile + str(accountNumberFromUser) + '.txt', 'x')
        

def deleteLogFile(userAccountNumber):
# Deletes log file in auth_session when logging out
    if os.path.exists(logFile + str(userAccountNumber) + '.txt'):
        try:
            os.remove(logFile + str(userAccountNumber) + '.txt')            
        except FileNotFoundError:
            print('No log file found')
        
        
def recordBalance(accountNumber, balance):
    balanceData = str(balance)
    # Records a users initial balance upon registering
    if doesAccountNumberExist(accountNumber):
        f = open(userBalance + str(accountNumber) + '.txt', 'x')
        f.write(str(balanceData))
        
        
def updateBalanceWithdrawl(userAccountNumber, balance, withdrawlAmt):
    # Updates a users balance when withdrawing
    balanceWithdraw = str(int(balance) - int(withdrawlAmt))

    if os.path.exists(userBalance + str(userAccountNumber) + '.txt'):
    
        f = open(userBalance + str(userAccountNumber) + '.txt', 'w')
        f.write(str(balanceWithdraw))
        f.close
        print('Your New Balance is $' + str(balanceWithdraw))            
    
def updateBalanceDeposit(userAccountNumber, balance, depositAmt):
     # Updates a users balance when depositing
    balanceDeposit = str(int(balance) + int(depositAmt))

    if os.path.exists(userBalance + str(userAccountNumber) + '.txt'):
    
        f = open(userBalance + str(userAccountNumber) + '.txt', 'w')
        f.write(str(balanceDeposit))
        f.close
        print('Your New Balance is $' + str(balanceDeposit)) 

