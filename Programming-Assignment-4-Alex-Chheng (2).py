# Alex Chheng, Daniel Duong, and Brandon Walker
# CECS 229 Programming Assignment 4

# https://inventwithpython.com/hacking/chapter23.html
# https://www.geeksforgeeks.org/gcd-in-python/
import math

def RSAencrypt(ip, iq, ie, imessage):
    p = ip
    q = iq
    e = ie
    message = imessage

    if len(message) <= 0:
        return "Message length needs to be greater than 0."
    if not isPrime(p) or not isPrime(q):
        return "Both p and q need to be prime."
    if computeGCD(e, (q - 1) * (p - 1)) != 1:
        return "e needs to be relatively prime to (p-1)(q-1)."

    n = p * q  # mod
    size = len(str(BlockSize(n)))
    toEncrypt = ""
    tempC = ""
    c = []

    for x in message:
        toEncrypt += CharConversion(x)

    #print(toEncrypt)
    #print("size", size)
    block = math.ceil(len(toEncrypt)/size)
    #print("block", block)
    for i in range(block):
        #print("//////")
        for k in toEncrypt[i*size:(i+1)*size]:
            #print("k", k)
            tempC += k
        #print(tempC)
        while len(tempC) != size:
            tempC += "23"
        #print("tempC", tempC)
        c.append(str(Encryption(int(tempC), n, e, size)))
        #print("c", c)
        tempC = ""
    #print(c)

    #return print(p, q, e, message)
    return c

def isPrime(num):
    # Returns True if num is a prime number, otherwise False.

    # Note: Generally, isPrime() is slower than primeSieve().

    # all numbers less than 2 are not prime
    if num < 2:
        return False

    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def computeGCD(x, y):
    while (y):
        x, y = y, x % y

    return x

def CharConversion(l):
    letter = l
    value = "23"
    if letter == "a" or letter == "A":
        value = "00"
    elif letter == "b" or letter == "B":
        value = "01"
    elif letter == "c" or letter == "C":
        value = "02"
    elif letter == "d" or letter == "D":
        value = "03"
    elif letter == "e" or letter == "E":
        value = "04"
    elif letter == "f" or letter == "F":
        value = "05"
    elif letter == "g" or letter == "G":
        value = "06"
    elif letter == "h" or letter == "H":
        value = "07"
    elif letter == "i" or letter == "I":
        value = "08"
    elif letter == "j" or letter == "J":
        value = "09"
    elif letter == "k" or letter == "K":
        value = "10"
    elif letter == "l" or letter == "L":
        value = "11"
    elif letter == "m" or letter == "M":
        value = "12"
    elif letter == "n" or letter == "N":
        value = "13"
    elif letter == "o" or letter == "O":
        value = "14"
    elif letter == "p" or letter == "P":
        value = "15"
    elif letter == "q" or letter == "Q":
        value = "16"
    elif letter == "r" or letter == "R":
        value = "17"
    elif letter == "s" or letter == "S":
        value = "18"
    elif letter == "t" or letter == "T":
        value = "19"
    elif letter == "u" or letter == "U":
        value = "20"
    elif letter == "v" or letter == "V":
        value = "21"
    elif letter == "w" or letter == "W":
        value = "22"
    elif letter == "x" or letter == "X":
        value = "23"
    elif letter == "y" or letter == "Y":
        value = "24"
    elif letter == "z" or letter == "Z":
        value = "25"

    return value

def BlockSize(n):
    tempVar = 25
    oldVar = 25
    while (1):
        if n > tempVar:
            oldVar = tempVar
            tempVar = (int(str(tempVar) + "25"))
        else:
            break

    return oldVar

def concat(a, b):
    return int(f"{a}{b}")

def Encryption(b, n, e, s):  # base, mod, power
    tempB = str(b ** e % n)
    while len(tempB) != s:
        tempB = "0" + tempB
    return tempB

'''def main():

    print(RSAencrypt(43, 59, 13, "STOP"))
    print(RSAencrypt(43, 59, 13, "ABC"))
    print(RSAencrypt(43, 59, 13, ""))
    print(RSAencrypt(503, 509, 21, "HELLO"))
    print(RSAencrypt(43,14,13,"ABC"))
    print(RSAencrypt(11,13,10,"EXCELLENT"))

main()'''

