def solution(data,n):
    l=[]
    for elem in data:
        if not data.count(elem) >n:
            l.append(elem)
    return [data,l]

print(solution([1,1,1,1,2,2,2,3,3,4],1))
