num1=int(input("Enter a Number : "))
num2=int(input("Enter a Number : "))
num3=int(input("Enter a Number : "))

if num1>=num2 and num1>=num3:
    print(num1,"Greater among three numbers")
elif num2>=num1 and num2>=num3:
    print(num2,"Greater among three numbers")
else:
    print(num3,"Greater among three numbers")        
