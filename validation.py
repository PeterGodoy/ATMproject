def accountNumberValidation(accountNumberFromUser):
    
    if accountNumberFromUser:

        try:
            int(accountNumberFromUser)

            if len(str(accountNumberFromUser)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False
           
    return False 