i = 0
ListA = [18, 2, 90, 3, 5]
ListB = [2, 86, 42, 5, 7]
ListA.sort()
ListB.sort()

for i in range(len(ListA)):
    if min(ListA) in ListB:
        print(min(ListA))
        ListA.remove(min(ListA))
        i += 1
