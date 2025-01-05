# Fibonacci  generator
def fibonacci_generator(n):
    a, b = 0, 1 
    count = 0

    while count < n:
        yield a
        
        a, b = b, a + b
        count += 1


num_terms = int(input("Enter the number of terms you want in the Fibonacci series: "))

print("Fibonacci series:")
for number in fibonacci_generator(num_terms):
    print(number, end=" ")
