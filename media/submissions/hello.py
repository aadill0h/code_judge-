def square_sum( n):
    temp = 0
    sum =0
    while(temp <= n):
        sum = sum + temp*temp
        temp = temp +1
    print(f"the sum is {sum}")
    return sum

square_sum(5)