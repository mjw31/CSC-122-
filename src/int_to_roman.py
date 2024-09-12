import math
"""
* Converts inputted integers between 1-5999 to roman numerals
*
* Bugs: add reloop, make it pass tessts (see alvin?)
*
* @author <Michael Wolfe>
* @date <8/27/2024>
"""
# function to convert to roman numeral. did it wrong way in this commented section, but this also works.
#1.initialize string 
#2.create loop to iterate over the dictionary
#3.create loop to maximize the chosen numerals valeu
#3b.Adds the numeral to the result string
#3c.Subtracts the nuemral value used
#3x.repeats until value is 0
# use floor division by place amount to determine the single number value for that place
#multiply by count to determine how many of numeral are needed
# modulo determines left over amount to be converted still
LOWER =1
UPPER = 5999
def thousands(n):
    n=int(n)
    roman = ''
    if n >= 1000:
        count = n // 1000
        roman = 'M' * count
        n %= 1000
    return (n, roman)
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
def tens(n):
    roman = ''
    if n >= 10:
        count = n // 10
        if count == 9:
            roman = 'XC'
        elif count >= 5:
            roman = 'L' + 'X' * (count - 5)
        elif count == 4:
            roman = 'XL'
        else:
            roman = 'X' * count
        n %= 10
    return (n, roman)

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
# def isgoodnumber():
#     n=int(n)
#     int((input(f"Enter the number you wish to convert\n:")))
#     if n > 5999 or  n <=1: 
#         blank_str= ''
#         return blank_str
#     else:
#         return n
# new convert function
def to_roman(n):
    n=int(n)
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
