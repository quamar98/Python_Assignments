# Reverse a number using recursion

def reverse(n, r):
    if n==0:
        return r

    return reverse(n//10, r*10 + n%10)

# Read number
number = int(input("Enter number: "))

# Function call
reversed_number = reverse(number,0)

# Display output
print(reversed_number)
