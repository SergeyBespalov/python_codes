
def fibo(x):
    if x == 1:
        return 1
    if x == 0:
        return 1
    return fibo(x - 1) + fibo(x - 2)


#  print(fibo(5))


def fibonacci_sum(a):
    my_sum = 0
    number = 1
    while a > fibo(number):
        if fibo(number) % 2 == 0:
            my_sum += fibo(number)
        number += 1
    return my_sum


print(fibonacci_sum(4000000))


