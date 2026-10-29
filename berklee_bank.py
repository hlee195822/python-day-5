bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

'''
Name: print_welcome
Task: prints the welcome message to the terminal
Input: None
Side Effects (print/display)
Return: None
'''

def print_welcome():
    print("==== welcome")

'''
Name: get_username
Task: Prompt the user for their name
Input: None
Side Effects (print/display): Promt "what is your name"
Return: reture the username
'''

def get_username():
    name = input("what is your name?")
    return 

'''
Name: get_pin
Task: Prompt the user for thier pin
Input: None
Side Effects (print/display) "what is your pin"
Return: reture the pin
'''

def get_pin():
    pin = inpit("what is your pin? ")
    return pin

'''
Name: verify_idenitly
Task: Take the name and pin and see if there's a valid user in the system. If so, get their data. If not, fail
Input: username, pin
Side Effects (print/display): If they don't exist, it says "Access Denied"
Return: Trun if user exists, False if not
'''
def verify_identity(usename, pin):
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        if pin == users_values.get("pin"):
            return True
        print("Access Denied for ", username, "with pin", pin)
        return False


'''
Name: Print_meau
Task: Print the functionality of the bank (the commands they can do) to the terminal
Input: None
Side Effects (print/display): do you wanna deposit, withdraw, get balance, quite (they type their answer)
Return: the string the user typed in
'''
def get_meau_choice():
    choice = input("Do you want to... deposit withdraw balance quit")
    return choice

'''
Name: get_balance
Task: gets the balance and prints it
Input: 
Side Effects (print/display): the balance 
Return: None
'''

def get_balance(username)
    if bank_dict.get(username):
        user_values = bank_dict.get(username)
        balance == users_values.get("balance"):
        print("Your balance is: ", balance)

return None

'''
Name: deposit_money
Task: Ask the user how much they want to deposit then add that to the balance
Input: username
Side Effects (print/display): prompting the user for the amount to deposit
Return: None
'''

def deposit_money(username)
    deposit amount = inout("How much would you like to deposit? ")
     if bank_dict.get(username):
            user_values = bank_dict.get(username)
            previous_bal =user_values.get("balance")
            new_bal =previous_bal + deposit-amount 
            user_valuse.update("balance": new_bal)

    return None
'''
Name: withdraw_money
Task: Ask the user how much they want to withdraw. If they have enough, 
Input: username
Side Effects (print/display): Asking the user the amount they want to withdraw
Return: None
'''
def withdraw_money(username):
    withdraw_amount = in(input("How much would you like to withdraw?"))
    if bank_dict.get(username):
            user_values = bank_dict.get(username)
            previous_bal =user_values.get("balance")
            new_bal =previous_bal - deposit-amount 
            if new_bal < 0:
                print("Insufficient funds...")
            else: # if the new balance is not less than 0, update the dictionary
                user_values.update({"balance": new_bal})


def run_tests():
    withdraw_money("priya") # Asks for amount, if 200 fail
    withdraw_money("priya") # Asks for amount, if 100 should succeed

    deposit_money("priya") # Asks for the amount, if 100 should succeed

    get_balance("priya") # Print $100 

    #verify_identity("priya", 4821)





    def main():
        print_welcome()
        name =get_username()
        pin =get_pin()
        valid + verfiy_identity(name, pin)
        if not valid:
            return
        while True:
            users_choice = get_meau_choice()
            if users_choice == "balance":
                get_balance(name)

            elif users_choice == "withdraw": 
                withdraw_money(name)

            elif users_choice == "deposit": 
                 deposit_money(name)

            elif users_choice == "quit": 
                break

            elif print("You can't choose that...")

            
         



