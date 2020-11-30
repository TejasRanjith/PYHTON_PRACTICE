for i in range(0,25):
    import random as r
    str1 = "CBSEONLINE"
    num = r.randint(0,3)
    N = 9
    while str1[N] != "L":
        a = (str1[N] + str1[num] + "# "+str(num))
        print(a,end= " ")
        num= num+ 1
        N-=1
    print()

input("PLEASE PRESS ENTER TO COMPLETELY TERMINATE THE *.EXE FILE :) ")
