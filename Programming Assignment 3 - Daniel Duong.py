from math import gcd #This tool imports the built in function for the GCD.

#CECS 229 Programming Assignment 3

#Names: Daniel Duong, Brandon Walker, Alex Chheng

def ChineseRemainderTheorem(L):
    #pass
    
    #print(L)

    #print("Number of sub-lists:", len(L))

    list_length = len(L)

    #print(list_length)

    M = 1

    y_list = []
    m_list = []

    for x in range(list_length):
        n = L[x][1] % L[x][0]
        #print(n)

    #print("Cane's")

    for x in range(list_length):
        #print(L[x][0], L[x][1])
        M *= L[x][1]
        m_list.append(L[x][1]) #L[x][1] represents the m values

    #print(m_list)

    for x in range(list_length):
        Mx = M / L[x][1]
        y = 1
        My = Mx * y % L[x][1]

        while(My != 1):

            if y > L[x][1]:
                #print("Error in y, programmer please check again")
                break

            y += 1

            My = Mx * y % L[x][1]

        y_list.insert(x,y)

    result = 0

    for x in range(list_length):
        Mx = M / L[x][1]
        result += L[x][0] * Mx * y_list[x]

    result %= M
    #print(int(result))

    if not(IsRelativelyPrime(m_list)):
        return("Cannot proceed, the modulus values are not relatively prime")

    elif(IsRelativelyPrime(m_list)):
        return int(result)
    
def IsRelativelyPrime(m_list): #The way that we check is by the m values not a values.
    #pass
    
    relativelyPrime = True

    for a in range(len(m_list)):

        for m in range(len(m_list)):

            #print ("A:", a)
            #print ("M:", m)
            #print("GCD of A and M:", gcd(a,m))

            if a != m: #If the m values of each sublist are not equal, then check amongs the other m values of other sublists.
                
                if gcd(m_list[a], m_list[m]) != 1: #If the gcds of the m values of sublists are not 1, then it is not relatively prime.
                    relativelyPrime = False
                
    return relativelyPrime
    
def main():

    print(ChineseRemainderTheorem([[2,3],[3,5],[2,7]]), "\n")

    print(ChineseRemainderTheorem([[1,5],[2,7],[3,9],[4,11]]), "\n")

    print(ChineseRemainderTheorem([[1,5],[2,7],[3,9],[4,11],[8,22]]), "\n")

    #Test cases above are the samples provided as a demo

    #Here these are some additional test cases

    print(ChineseRemainderTheorem([[6,11],[13,16],[9,21],[19,25]]), "\n")

    print(ChineseRemainderTheorem([[2,5], [3,7]]), "\n")

    print(ChineseRemainderTheorem([[6,7], [4,8]]), "\n")

    print(ChineseRemainderTheorem([[5,2], [3,7], [28,98], [100,2]]), "\n")

    print(ChineseRemainderTheorem([[2,3],[3,5],[2,25]]), "\n")
    
main()

