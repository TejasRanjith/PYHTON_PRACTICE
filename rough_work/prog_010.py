# def odd_splitter(n):
    #     n1,n2 = n+1,n-1
    #     n1c,n2c = solution(n1),solution(n2)
    #     if n1c < n2c:return n2
    #     else:return n1

    # def solution(n):
    #     count,n = 0,int(n)
    #     while n > 1:
    #         if n % 2 == 0:n//=2;count += 1
    #         else:n = odd_splitter(n);count+=1
    #     return count

    # print(solution(5))
    # # for a in range(0,11):
    #     # print(a,'   ',solution(a))

    # def prime_factors(n):
    #     l = []
    #     while n > 1:
    #         for i in [2,3,5,7,11,13,17,19]:
    #             if n % i == 0:
    #                 l.append(i)
    #                 n //= i
    #     return l

    # def solution(n):
    #     count,n = 0,int(n)
    #     if n % 2 == 0:return len(prime_factors(n))
    #     else:print("OOPS")

    # print(solution(input()))

def solution(n):
    n = int(n)
    if n == 0:return 0
    if n <= 2:return n-1
    elif n%2 == 0:return solution(n//2)+1
    return min(solution(n+1), solution(n-1))+1

for a in range(0,21):
    print(a,'   ',solution(a))