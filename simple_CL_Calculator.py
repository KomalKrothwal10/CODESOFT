def make_subtraction_of(a ,b):
    return a - b

def divide(a,b):
    if b == 0:
        return "Bug!"
    return a/b

def add(a,b):
    return a + b

def multiplication(a,b):
    return a * b



def main():
   
    print("Operations available are listed below in the Simple_Command_line Calculator:")
    print("add : +")
    print("subtract: - ")
    print("multiplication: *")
    print("divide : /")
    
    
    try:
        a = float(input("Enter the required first number i.e number1: "))
        b = float(input("Enter the required second number i.e. number2:  "))
    except ValueError:
        print("Invaid!")
        return
    
    
    
    arithmetic_operation = input("enter the required arithmetic_operation (+,-,*,/) : ")
    
    if arithmetic_operation == '+' :
        result = add(a,b)
        
    elif arithmetic_operation == '-' :
        result = make_subtraction_of(a,b)
    
    elif arithmetic_operation == '*':
        result = multiplication(a,b)
        
    elif arithmetic_operation == '/':
        result = divide(a,b)
        
    else:
        print("Invalid inserted arithmetic_operation ,Please try again!!")
        
    print(f"Required Result:  {result}")   
        
        
__name__ == '__main__' 
main()
    
    



   
    


