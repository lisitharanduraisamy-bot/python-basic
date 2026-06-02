mark=int(input("Enter your Mark : "))
if mark<0 or mark>100:
    print("Invalid Mark")
elif mark>=90:
    print("Your Grade is A")
elif mark>=75:
    print("Your Grade is B")
elif mark>=50:
    print("Your Grade is C")
else:
    print("Fail,Better luck Next Time")            
