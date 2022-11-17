# to find the prime factors of a number
s = []
def prime_factors(n):
    for i in [2,3,5,7,11,13,17,19]:
        while n % i == 0:
            s.append(i)
            n = n/i
prime_factors(2100)
print(str(s).removeprefix("[").removesuffix("]").replace(', ',' x ',len(s)),f"= {2100}")


# def primes(x):
#     return [i for i in range(2,x) if 0 not in [i%j for j in range(2,i)]]
# print(primes(20))
