def solution(x, y):
    m,f,s = int(x),int(y),0
    while True:
        if m <= 0 or f <= 0:break
        if m > 100 or f > 100:
            if m > f:
                val = (m-f)//f
                m-=val*f;s+=val
            elif m < f:
                val = (f-m)//m
                f-=val*m;s+=val
            else:break
        else:
            if m > f:m-=f
            elif m < f:f-=m
            else:break
            s+=1
    if m == 1 and f == 1 and s >= 0:
        return str(s)
    return "impossible"
                




# if min(l)==0 or max(l)==0:return 'impossible'
# if max(l) == min(l):return 'impossible'
# while max(l)>1:
#     i+=1;l=[((max(l)-min(l))/min(l))+1,min(l)]
#     if min(l)==0:return 'impossible'
# return str(i)

# print(solution(2,4))

for a in range(0,10):
    for b in range(0,10):
        print(a,'',b,'',solution(a,b))