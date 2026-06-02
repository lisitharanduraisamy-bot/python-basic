units=int(input("Enter the number of Units used : "))

if units<100:
    print(units*5)
elif units<200:
    print(500+(units-100)*7)
else:
    print(1200+(units-200)*10)        
