example = ['1','2','0*6','8','3','0*2','6','0*1','1','0*3','0*5','7','0*2','9','0*9','8','0*2','9','0*3','5','0*1','0*5','3','0*2','6'
,'0*2','8','1','0*2','2','9','7','9','0*1','7','0*1','6','0*1','1','8','0*1','2','0*1','5','0*2','9','0*3']
def table_horizontal(data):
    l,n = [],0
    for elem in data:
        if '0' in elem:
            n += int(elem.split('*').pop(-1))
            while n > 0:
                l.append(elem.split('*').pop(0))
                n-=1
        else:
            l.append(elem)
    # print(l)
    table,n,tab = l,0,[]
    while n < 9:
        tab.append(table[(n*9):((n+1)*9)])
        n+=1
    # print(tab)
    return tab

def table_vertical(data):
    n,tab_vert = 0,[]
    raw_table = table_horizontal(data)
    while n < 9:
        tab=[]
        for row in raw_table:
            tab.append(row[n])
        tab_vert.append(tab)
        n+=1
    return tab_vert

# print(table_horizontal(example))
# table_vertical(example)

def table_square(data):
    raw_table = table_horizontal(example)
    tab_sq,tab,n = {},[],0
    for n in range(3):
        for row in raw_table:
            tab.append(row[n*3:(n+1)*3])
    for n in range(9):
        tab_sq[n+1] = tab[n*3:(n+1)*3]

    new_tab_sq={}
    for key in tab_sq:
        tab=[]
        for elem in tab_sq[key]:
            tab.extend(elem)
            new_tab_sq[key]=tab
    tab_sq = new_tab_sq.copy()
    return tab_sq

def checker(h,v,s):
    l,n=[],1
    for s in h:
        if n in s:
            pass
        else:
            l.append(n)
    return l


horz = table_horizontal(example)
vert = table_vertical(example)
sq =table_square(example)
l = []
l1 = [h for h in horz]
for a in range(0,9):
    for b in range(0,9):
        if horz[a][b] == '0':
            n = 1
            while n < 10:
                if (n in [h for h in horz]) or (n in [v for v in vert]) or (n in [s for s in sq]):
                    # print('found')
                    pass
                else:
                    l.append(n)
                    # print(n)
                n+=1



# print(l1)
print(horz)