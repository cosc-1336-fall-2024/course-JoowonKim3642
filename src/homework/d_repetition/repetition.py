#get_factorial and sum_odd_numbers

def get_factorial(num):
    factorial = 1
    for i in range(1, num+1, 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    a = 1
    sumodd = 0
    while a <= num :
        if a%2 != 0 :
            sumodd += a
        a += 1
    return sumodd