'''
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# not the optimal solution

def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n-1)
    

def solution(a,b):
    for x in range(0,factorial(max(a,b)),max(a,b)):
        temp_list = []
        for y in range(1,max(a,b)+1):
            if x % y == 0:
                temp_list.append(y)
        if len(temp_list) == max(a,b) and x != 0:
            return x
    return 'nothing'


print(solution(1,10))
