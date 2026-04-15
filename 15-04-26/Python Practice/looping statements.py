for i in range(1, 51):
    print(i)



print('================================================')

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


print('================================================')
total = 0
for i in range(1, 101):
    total += i

print("The sum is:", total)


print('================================================')

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")