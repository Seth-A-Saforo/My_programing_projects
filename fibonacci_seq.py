# Asking an input from the user
n = int(input("Enter the number of terms needed in fibonacci sequence: "))

f1 = 0
f2 = 1

# Using if statements
if n <= 0:
    print('The number must be positive')
elif n == 1:
    print(f1)
else:
    for n in range(3, n + 1):
        f3 = f1 + f2
        print(f3, end=" ")
        f1 = f2
        f2 = f3



