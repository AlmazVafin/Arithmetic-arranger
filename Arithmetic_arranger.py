def arithmetic_arranger(problems, show_answers=False):
    mainlist=[] #список для слогаемых
    maxlenlist=[] # список максимальных длин строк слогаемых
    for i in problems:
        item1= i.split()
        mainlist.append(item1)
        lenlist = []
        for i in item1:
            len1=len(i)
            lenlist.append(len1)
        maxlenlist.append(max(lenlist))
    #print(maxlenlist)
    #print(mainlist)
    i=0
    for i in range(len(mainlist)):
        newstring=mainlist[i][0].rjust(maxlenlist[i]+2)+'    '+ mainlist[i+1][0].rjust(maxlenlist[i+1]+2)
    print(newstring)
    return problems

arithmetic_arranger(["32 + 698","3801 - 2"])

#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
#print(f'\n{arithmetic_arranger(["32 + 698"])}')