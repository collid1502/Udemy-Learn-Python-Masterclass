########################################################
####          Building a better Calculator          ####
########################################################


num1 = float(input("Enter First Number: ")) ;  # Using float will turn the text to a number after they write it in
op = input("Enter Operator: ") ;
num2 = float(input("Enter Second Number: ")) ;

if op == "+":
    print(num1 + num2) ;

elif op == "-":
    print(num1 - num2) ;

elif op == "/":
    print(num1 / num2) ;

elif op == "*":
    print(num1 * num2) ;

else:
    print("Invalid Operator") ;

