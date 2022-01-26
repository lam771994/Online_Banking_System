#LAM YING XIAN
#TP063038

##Admin Page##

#Create new account for customer
def create_newaccount():
    print('\n\t*****Create New Account for Customer*****\n\t')  
    customer_login=open('customerlogin.txt','a')
    customer_details=open('customerdetails.txt','a')
    data = int(input("\n\tPlease key in the number of customer's record that you want to keep: "))
    for x in range(data):
        loginid = input("Please create customer's login ID: ")
        customer_password = input("Please create customer's password: ")
        customer_name = str(input("Please enter customer's name: "))
        customer_ID = input("Please enter customer's identification no.: ")
        customer_login.write(loginid+"\t"+customer_password+"\n")
        customer_details.write(loginid+"\t\t"+customer_name+"\t\t"+customer_ID+"\n")
    customer_login.close()
    customer_details.close()
    print('\n\t***Account successfully created***\n\t')
    
    
    
#View all customer accounts
def view_allprofiles():
    print("\n\t*****All Customers' Profiles*****\n\t")
    myfile = open("customerdetails.txt","r")
    print("\n\nCustomer ID:\tCustomer Name:\tCustomer Identification No:")
    print(myfile.read())
    myfile.close()
   
    
#Search for specific customer account
def search_customer():
    print("\n\t*****Search for Specific Customer's Profile*****\n\t")  
    detail=input("Enter any customer detail:")
    myfile=open("customerdetails.txt","r")
    print("\n\nCustomer ID:\tCustomer Name:\tCustomer Identification No:")
    for line in myfile:
        line=line.rstrip()
        if detail in line:
            print(line)
    myfile.close()
    

def search_transaction():
    print("\n\t*****View Transaction*****\n\t")  
    detail=input("Enter the customer ID:")
    myfile=open("customeraccount.txt","r")
    print("\n\nCustomer ID:\tCustomer Name:\tDeposit Amount:\tWithdrawal Amount:\tBalance:")
    for line in myfile:
        line=line.rstrip()
        if detail in line:
            print(line)
    myfile.close()

###Customer Page###   

#Check customer authentication

def check_auth(x,y):
    customer_login=open("customerlogin.txt","r")
    auth = x+"\t"+y
    condition = False
    for line in customer_login:
        line = line.rstrip()
        if auth == line:
            condition = True
    customer_login.close()
    return condition

#function for customer's deposit and withdrawal
transaction_system = True
def deposit_withdrawal():
    print("\n\t*****Deposit or Withdraw Money*****\n\t")
    customer_account=open("customeraccount.txt","a")
    customer_balance = 0
    customer_deposit = 0
    customer_withdraw = 0
    loginid = input("Please enter your login ID: ")
    customer_name=input("Please enter your name: ")
    print("Customer ID:\tCustomer Name:\tBalance:")
    print(loginid+"\t\t"+customer_name+"\t\t"+str(customer_balance))
    while (transaction_system == True):
        print('\n\tPlease select the below option:\n\t')
        print('\n\t[A] Deposit money\n\t')
        print('\n\t[B] Withdraw money\n\t')
        print('\n\t[C] Exit\n\t')
        transaction = input("Please enter the option above: ")
        
        if transaction == 'A': 
            deposit = input("Please enter the amount that you would like to deposit: ")
            customer_deposit = float(deposit)
            customer_withdraw = 0.00
            customer_balance += float(deposit)
            print("\n\nCustomer ID:\tCustomer Name:\tDeposit Amount:\tWithdrawal Amount:\tBalance:")
            print(loginid+"\t\t"+customer_name+"\t\t"+str(customer_deposit)+"\t\t"+str(customer_withdraw)+"\t\t"+str(customer_balance)+"\n")
            customer_account.write(loginid+"\t\t"+customer_name+"\t\t"+str(customer_deposit)+"\t\t"+str(customer_withdraw)+"\t\t"+str(customer_balance)+"\n")
        elif transaction == 'B':
            withdraw = input("Please enter the amount that you would like to withdraw: ")
            if float(customer_withdraw) <= float(customer_balance):
                customer_withdraw = float(withdraw)
                customer_balance -= float(withdraw)
                print("\n\nCustomer ID:\tCustomer Name:\tDeposit Amount:\tWithdrawal Amount:\tBalance:")
                print(loginid+"\t\t"+customer_name+"\t\t"+str(customer_deposit)+"\t\t"+str(customer_withdraw)+"\t\t"+str(customer_balance)+"\n")
                customer_account.write(loginid+"\t"+customer_name+"\t"+str(customer_deposit)+"\t"+str(customer_withdraw)+"\t"+str(customer_balance)+"\n")
            else: 
                print("You have insufficient amount. The transaction cannot be done.")
        elif transaction == 'C':
            customer_account.close()
            break
        else:
            print("Incorrect option code. Please try again.")

#function for customer to view transaction
def view_transaction():
    print("\n\t*****View Transaction*****\n\t")  
    detail=input("Enter your customer ID:")
    myfile=open("customeraccount.txt","r")
    print("\n\nCustomer ID:\tCustomer Name:\tDeposit Amount:\tWithdrawal Amount:\tBalance:")
    for line in myfile:
        line=line.rstrip()
        if detail in line:
            print(line)
    myfile.close()

#loop function for the main page
system_activated = True
while(system_activated == True):
    print('\n\t*****Welcome to APU Online Banking Main Page*****\n\t')
    print('\n\tPlease key in the page code:\n\t')
    print('\n\t[1] Admin Page\n\t')
    print('\n\t[2] Customer Page\n\t')
    print('\n\t[3] Quit\n\t')
    menu_code=int(input('Enter the main menu code here:'))
    
    if menu_code == 1:
        print("\n\t*****Welcome to Admin Management Page*****\n\t")
        admin_username=input('Enter your administrator username: ')
        admin_password=input('Enter your administrator password: ')
        if admin_username == 'APUAdmin' and admin_password == '12345':
            print('\n\t*****Admin Management Page*****\n\t')
            print('\n\tPlease select the below option:\n\t')
            print('\n\t[1] Create New Customer Account\n\t')
            print('\n\t[2] View All Profiles\n\t')
            print('\n\t[3] Search for Specific Customer Account\n\t')
            print('\n\t[4] Search for Specific Customer Transaction\n\t')
            print('\n\t[5] Log Out\n\t')
            admin_page=int(input('Please key in the option code: '))
            if admin_page == 1:
                create_newaccount()
            elif admin_page == 2:
                view_allprofiles()
            elif admin_page == 3:
                search_customer()
            elif admin_page == 4:
                search_transaction()
            elif admin_page == 5:
                break
            else:
                print("You entered wrong option code. Please try again.")
                admin_page=int(input('Please key in the option code: ')) 
            
        else:
            print("You entered the wrong username or password. Please try again")
            
            
    elif menu_code == 2:
        print("\n\t*****Welcome to Customer Page*****\n\t")
        loginid=input('Enter your login ID: ')
        password=input('Enter your password: ')
        
        if check_auth(loginid,password):
            print('\n\tPlease select the below option:\n\t')
            print('\n\t[1] Deposit OR Withdraw Money\n\t')
            print('\n\t[2] View Transactions\n\t')
            print('\n\t[3] Log Out\n\t')
            customer_page=int(input('Please key in the option code: '))
            if customer_page == 1:
                deposit_withdrawal()
            elif customer_page == 2:
                view_transaction()
            elif customer_page == 3:
                break
        else: 
            print('\n\t***Incorrect login ID or password. Please try again***\n\t')
            
    elif menu_code == 3:
        print('\n\t***Exit Successful. Thank you for using our service***\n\t')
        break
    
else:
    print('\n\t***Invalid Code. Please try again.***\n\t')
            
    
        
                
                
        
        
    
    


    
    
    
        
