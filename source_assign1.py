import math

# function to convert to roman numeral
#1.initialize string 
#2.create loop to iterate over the dictionary
#3.create loop to maximize the chosen numerals valeu
#3b.Adds the numeral to the result string
#3c.Subtracts the nuemral value used
#3x.repeats until value is 0
def convert(x):
    num_string=''
    for value in numerals:
        while x >= value:
            num_string += numerals[value]
            x-= value
    return num_string
#error checks to verify the user is inputting an integer, and that it is representbale by roman numerals
def isgoodnumber():
    while True:
        try:
            n=int((input(f"Enter the number you wish to convert\n:")))
            break
        except ValueError:
            print("Error:\n Please enter a number")
    while n > 3999 or  n < 0:
        print('Error:n\Please enter a number between 0 and 3999.')
        n=int(input(f"Enter the number you wish to convert \n:"))
    return n
#"main" function
def to_roman():
    n=isgoodnumber()
    stringnum=convert(n)
    print(stringnum)
#dictionary from the table you provided w/ added special cases 
numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
#call main
to_roman()