a=int(input("Enter a Number : "))
b=int(input("Enter a Number : "))
ch=str(input("Enter a Operator : "))

if ch=='+':
    print(a+b)
elif ch=='-':
    print(a-b)
elif ch=='*':
    print(a*b)
elif ch=='/':
    print(a/b)
elif ch=='//':
    print(a//b)                
elif ch=='%':
    print(a%b)
else:
    print("Invalid Operator")    
