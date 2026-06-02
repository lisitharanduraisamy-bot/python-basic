bill=int(input("Enter Your Electricity Bill : "))

if bill<=100:
    print("Low Consumption")
elif bill>100 and bill<=300:
    print("Medium Consumption")
else:
    print("High Consumption")        
