def converter_to_deci(n,b):
    a,n = 0,n[::-1]
    for i in range(len(n)):
        a+=int(n[i])*(b**i)
    return str(a)

def converter_to_other(n,b):
    l,n,a = [],int(n),""
    while n//b > 0:
        l.append(n%b)
        n //= b
    if n//b == 0:
        l.append(n%b)
    l.reverse()
    for elem in l:
        a+=str(elem)
    return a

def part1_solution(n, b):
    x,y,p,q,k ="","",list(n),list(n),len(n)
    p.sort(reverse=True);q.sort(reverse=False)
    for elem_p in p:x+=elem_p
    for elem_q in q:y+=elem_q
    x,y = converter_to_deci(x,b),converter_to_deci(y,b)
    r = str(int(x)-int(y))
    z = converter_to_other(r, b)
    z = z.zfill(k)
    return z

def solution(n,b):
    l,i,l1,l2=[],0,[],[]
    while i<100:
        n = part1_solution(n, b)
        l.append(n)
        i+=1    
    for elem in l:
        if elem not in l1:
            l1.append(elem)
        elif elem in l1:
            l2.append(elem)
    return len(set(l2))
