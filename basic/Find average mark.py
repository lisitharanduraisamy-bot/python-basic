n = int(input("Enter number of subjects: "))

total = 0

for i in range(n):
    mark = int(input("Enter mark: "))
    total += mark

average = total / n

print("Average mark:", average)
