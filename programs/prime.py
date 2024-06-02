# Problem: 
# Tell whether the number is prime or not

# Take input from user for a number
print('Enter a number:')
num = int(input())

# If any factor for the number exists 
# other than 1 or itself, then number is not prime 
isPrime = True

for x in range(2, num//2):
    if num % x == 0:
        isPrime = False

print(isPrime)
