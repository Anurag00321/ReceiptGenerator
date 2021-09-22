sum = 0
while(True):
    UserInput=input("Enter the price of product or press q: \n")
    
    if (UserInput!='q'):
        sum = sum + int(UserInput)
        print(f"Your subtotal is {sum}")
    else:
        print(f"Your bill is {sum}.Thanks for shopping with us.")        

