# def test(start,length):
#     l,i,n,b,main,s = [],0,{},0,[],0
#     if length == 1:return start
#     for num in range(start,start+(length**2)):l.append(num)
#     while i<len(l):n[i]=l[i:i+length];i+=length
#     for k in n:
#         for dum in range(0,int(k/length)):
#             n[k].pop()
#         main.extend(n[k])
#     for elem in main:
#         s^=elem
#     return s
# # print(test(1,3))
# for a in range(5):
#     for b in range(5):
#         print(a,b,test(a,b))
#         # print(a,b,solution(a,b))

def XOR(n):
    if n % 4 == 0:return n
    elif n % 4 == 1:return 1
    elif n % 4 == 2:return n + 1
    else:return 0

def solution(start, length):
    if length == 1:return start
    val = XOR(start + 2*(length-1))
    if start > 1:val = val ^ XOR(start - 1)
    for i in range(length-2):
        elems = length - 2 - i
        init = start + length*(2 + i) - 1
        val = val ^ XOR(init + elems) ^ XOR(init)
    return val
print(solution(1,0))

# program asked from tejasranjith035611@gmail.com foobar challenge named Queue To do
