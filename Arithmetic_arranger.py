def arithmetic_arranger(problems, show_answers=False):
# список для слогаемых
    mainlist=[]

# список максимальных длин строк слогаемых
    maxlenlist=[]

# создаем список из исходных строк
    for i in problems:
        item1= i.split()
        mainlist.append(item1)
        lenlist = []

#попутно вычисляем  в каждой паре максимальную длину слогаемого и помещаем их в список
        for i in item1:
            len1=len(i)
            lenlist.append(len1)
        maxlenlist.append(max(lenlist))
#Первая строка для результата
    finalString1=''
#Вторая строка для результата
    finalString2=''
#Третья строка для результата
    finalString3=''
#Четвертая строка для результата
    finalString4=''

    print(mainlist)
#добавляем нужное число пробелов в слогаемых и между столбиками
    for i in range(len(mainlist)):
        if i ==len(mainlist)-1:
            newstring1 = mainlist[i][0].rjust(maxlenlist[i] + 2)
        else:
            newstring1=mainlist[i][0].rjust(maxlenlist[i]+2)+'    '

#конкатенируем все в итоговую первую строку
        finalString1=finalString1+newstring1
    #print(finalString1)

#работаем аналогично со второй строкой

#добавляем нужное число пробелов в слогаемых и между столбиками, а также знаки "+/-"
    for i in range(len(mainlist)):
        if i ==len(mainlist)-1:
            newstring2 = mainlist[i][1] + mainlist[i][2].rjust(maxlenlist[i] + 1)
        else:
            newstring2=mainlist[i][1] + mainlist[i][2].rjust(maxlenlist[i]+1)+'    '

#конкатенируем все в итоговую вторую строку
        finalString2=finalString2+newstring2
    #print(finalString2)

#работаем аналогично с третьей строкой

#добавляем нужное число пробелов между столбиками и заполняем стобики знаком "-"
    for i in range(len(mainlist)):
        if i ==len(mainlist)-1:
            newstring3 = ''.rjust(maxlenlist[i] + 2,'-')
        else:
            newstring3=''.rjust(maxlenlist[i] + 2,'-')+'    '

#конкатенируем все в итоговую третью строку
        finalString3=finalString3+newstring3
    #print(finalString3)

#работаем с четвертой строкой

#Создаем список для результатов
    resultList=[]
#Вычисляем результат операции
    for i in range(len(mainlist)):
        if mainlist[i][1] =="-":
            resultItem = str(int(mainlist[i][0]) - int(mainlist[i][2]))
        else:
            resultItem = str(int(mainlist[i][0]) + int(mainlist[i][2]))
        resultList.append(resultItem)
    print(resultList)
#добавляем нужное число пробелов между столбиками и
    for i in range(len(mainlist)):
        if i == len(mainlist) - 1:
            newstring4 = resultList[i].rjust(maxlenlist[i] + 2)
        else:
            newstring4 = resultList[i].rjust(maxlenlist[i] + 2) + '    '
        #print(newstring4)
#конкатенируем все в итоговую третью строку
        finalString4=finalString4+newstring4
    #print(finalString4)
#Объединяем первые 3 строки в одну
    finalStringStep1=finalString1+"\n"+finalString2+"\n"+finalString3
    #print(finalStringStep1)
#Объединяем 4 строки в одну
    finalStringStep2=finalString1+"\n"+finalString2+"\n"+finalString3+"\n"+finalString4
    print(finalStringStep2)
    if show_answers == True:
        finalString = finalStringStep2
    else:
        finalString = finalStringStep1
    #print(finalString)
    return finalString

#arithmetic_arranger(["32 + 698","3801 - 2"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
#print(f'\n{arithmetic_arranger(["32 + 698"])}')