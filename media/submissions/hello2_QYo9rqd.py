def factorial( n):
    temp = 1
    fact =1
    while(temp <= n):
        fact = fact*temp
        temp = temp +1
    print(f"the sum is {fact}")
    return fact
factorial(5)