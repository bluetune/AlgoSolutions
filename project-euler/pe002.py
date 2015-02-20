'''
Each new term in the Fibonacci sequence is generated by adding
the previous two terms. By starting with 1 and 2, the first 10
terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''

__author__ = 'SUN'

def calculate():
    total = 0
    a,b = 1, 1
    while b <= 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            total += b
    print(total)

if __name__ == '__main__':
    calculate()

