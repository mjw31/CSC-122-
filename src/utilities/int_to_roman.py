"""
* Converts inputted integers between 1-5999 to roman numerals.
*
* Bugs: All fixed now. Initially added too much extracurricular(reloop, complex error check.. etc) messed with the testing functions.
*
* Algorithm:function pathway
*use floor division by place amount to determine the single number value for that place
*multiply by count to determine how many of numeral are needed
*deal with 6-10
*modulo determines left over amount to be converted still
*repeat for all places
* @author <Michael Wolfe>
* @date <8/27/2024>
"""


import math


#set limits
LOWER =1
UPPER = 5999
#thousands
def thousands(n):
    n=int(n)
    roman = ''
    if n >= 1000:
        count = n // 1000
        roman = 'M' * count
        n %= 1000
    return (n, roman)
#hundreds
def hundreds(n):
    roman = ''
    if n >= 100:
        count = n // 100
        if count == 9:
            roman = 'CM'
        elif count >= 5:
            roman = 'D' + 'C' * (count - 5)
        elif count == 4:
            roman = 'CD'
        else:
            roman = 'C' * count
        n %= 100
    return (n, roman)
#tens
def tens(n):
    roman = ''
    if n < 10:
        return (n , roman)
    count = n // 10
    if count == 9:
        roman = 'XC'
    elif count >= 5:
        roman = 'L' + 'X' * (count - 5)
    elif count == 4:
        roman = 'XL'
    else:
        roman = 'X' * count
    return (n%10, roman)
#ones
def ones(n):
    roman = ''
    if n >= 1:
        if n == 9:
            roman = 'IX'
        elif n >= 5:
            roman = 'V' + 'I' * (n - 5)
        elif n == 4:
            roman = 'IV'
        else:
            roman = 'I' * n
    return (0, roman)


#error checks to verify the user is inputting an integer, and that it is representbale by roman numerals
def isgoodnumber(n):
    n=int(n)
    return  not (n > 5999 or  n < 1)
  
def to_roman(n):
    if not isgoodnumber(n):
        return ''
    accum = ''

    # thousands place
    n, roman = thousands(n)
    accum += roman

    # hundreds place
    n, roman = hundreds(n)
    accum += roman

    # tens place
    n, roman = tens(n)
    accum += roman

    # ones place
    n, roman = ones(n)
    accum += roman

    return accum
