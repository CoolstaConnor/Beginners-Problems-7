NumList = [1,3,8,35,4,2,3]
CheckedList = []
for i in range(len(NumList)):
    if NumList[i] in CheckedList:
        print("YES")
    else:
        print("NO")
        CheckedList.append(NumList[i])
