# def test(xs):
#     num,neg,n = 1,[],1
#     # if xs.count(0) == len(xs) or xs.count(0) == len(xs)-1 or xs.count(0) == len(xs)-2:return str(0)
#     if xs.count(0) in [len(xs),len(xs)-1,len(xs)-2]:return str(0)
#     for elem in xs:
#         if elem > 0: num *= elem
#         if elem < 0: neg.append(elem)
#     if len(neg) % 2 == 0:
#         for elem in neg:num *= elem
#     if len(neg) % 2 != 0:
#         for elem in neg:
#             n *= elem
#         n //= max(neg)
#     return str(num*n)

def test(xs):
    num = 1
    if xs.count(0) == len(xs):return str(0)
    if len(xs) == 1 and len ([n for n in xs if n < 0]) == 1:return(str(xs[0]))
    if len([n for n in xs if n < 0]) == 1 and xs.count(0) == len(xs)-1:return(str(0))
    for elem in xs:
        if elem != 0 and elem <= 1000:num *= elem
    if num < 0:
        neg_max = max([n for n in xs if n < 0])
        num = num/neg_max
    return(str(int(num)))

print(test([2,0,2,2,0]))