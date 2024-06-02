# Problem: 
# Print FizzBuzz if divisible by both 3 and 5
# Print Fizz if divisible by 3
# Print Buzz if divisible by 5

# Take input from user for a number
print('Enter a number:')
num = int(input())

# If divisible by 3 and 5, print FizzBuzz
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')

# If divisible by 3, print Fizz
elif num % 3 == 0:
    print('Fizz')

# If divisible by 5, print Buzz
elif num % 5 == 0:
    print('Buzz')