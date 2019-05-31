mylist = [6.1, 4.2, 3.3, 7.4, 5.5, 2.6, 8.7, 1.8]

def bubble(badList):
    length = len(badList) - 1
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False
            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print(badList)

            else:
                unsorted = True

print (bubble(mylist))
