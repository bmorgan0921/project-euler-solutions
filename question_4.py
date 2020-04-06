'''
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def solution(a,b):
    ''' 
        enter two numbers and this function will return the largest palindrome made from the product of two numbers within the range specified
    '''

    for i in range(max(a,b), min(a,b), -1):
        for j in range(max(a,b), min(a,b), -1):
            str_mult = [letter for letter in str(i*j)]
            halfway = round(len(str_mult) / 2)
            if str_mult[:halfway] == str_mult[::-1][:halfway]:
                return int(i * j)
    return 'No palindromes found... :('
            

print(solution(100,1200))

