# a = m2-n2
# b = 2mn
# c = n2+m2
def pythogorean_triplets(m,n):
    l,i,j = [],0,0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i>j:
                a = (i*i)-(j*j)
                b = 2*i*j
                c = (i*i)+(j*j)
                l.append([a,b,c])
            else:
                pass
    for elem in l:
        print(elem)

# while True:
#     print("<<----  MENU  ---->>\n")
#     print("n --> To enter number of pythogorean triplets")
#     print("m --> To enter m and n values")
#     print("0 --> To quit\n")
#     opt = input("Your Option: ").lower()
#     if opt == "n":
#         m = int(input("Enter number of pythagorean triplets : "))
#         n = m - 1
#         print(m, n)
#     elif opt == "m":
#         m = int(input("Enter m value : "))
#         n = int(input("Enter n value : "))
#         #.r n > m                                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         print(m, n)
#     elif opt == "0":
#         break
#     else:
#         print("Invalid Option")
pythogorean_triplets(50, 49)