def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        print(i)
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = 2
prime_checker(number=n)
