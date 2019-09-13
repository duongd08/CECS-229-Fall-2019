import math

#Names: Daniel Duong, Brandon Walker

#CECS 229 Python Assignment 1

#Problem 1

print(" ----------- Problem 1: -----------\n")

hours_per_day = 24 

seconds_per_minute = 60

minutes_per_hour = 60 

days_per_year = 365 

years_per_decade = 10

seconds_per_decade = hours_per_day * seconds_per_minute * minutes_per_hour * days_per_year * years_per_decade
#Formula for seconds per decadee: 24 * 60 * 60 * 365 * 10

print("There are", seconds_per_decade, "seconds per decade\n")

#Problem 2

print(" ----------- Problem 2: -----------\n")

remainder_with_mod = 5789248 % 6
#The remainder of the number after it was divided

print("The remainder is", remainder_with_mod, "\n")

#Problem 3 - Here we will find remainder without the "%"

print(" ----------- Problem 3: -----------\n")

divisor = 6

dividened = 5789248

remainder_without_mod = dividened - ((dividened // divisor) * divisor)

print("The remainder without using the modulo(%) is", remainder_without_mod, "\n")

#Problem 4

print(" ----------- Problem 4: -----------\n") 

array = {1, 3, 5, 7, 11}

new_result = {(i ** 4) - 2 for i in array}

print("The new values for the set are", new_result, "\n")
      
#Problem 5

print(" ----------- Problem 5: -----------\n")

M = [11, -2, 8, 15, 22] # Declaring M as a new list

N = [(M[k] ** 3) - M[k] for k in range(len(M))]

#The comprehension is the Mth index[k] cubed - the value of M index[k]
#And to iterate through M to assign new value of the list N

print("The new values are", N, "\n")

#Problem 6

print(" ----------- Problem 6: -----------\n")

firstSet = set()

for cubes in range(1, 31):
    firstSet.add(cubes ** 3)

#print("The first list has", firstSet, "\n")

secondSet = set()

for triples in range(1, 31):
    secondSet.add(triples * 3)

#print("The second list has", secondSet, "\n")

intersected = firstSet.intersection(secondSet)

print("The intersected set has", intersected, "\n")



             




















