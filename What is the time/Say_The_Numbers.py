"""
Author: Khaled Aladawy
Date: 28/1/2021
Time: 2:09
Name: Say the numbers
"""
def main():
    for i in range(5, 15):
        x = Number_Name(i)
        print(f"{x} ", end=' ')
    print("\nDone")
    l = [1,2]
    x = Number_Name(l[0])
    print(x)


#tuples stores the names of numbers. it's tuple because it's constant and can't change
Ones = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")

Tens = ('ten', 'N/A', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

Teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' )


"""
Name: Number_Name(Num)
I/P: (Num) integer 
O/P: string
Description: it takes a number in digit and return the name of this number in English litter
"""

def Number_Name(Num):
    if isinstance(Num, int):
        if ( (0 <= Num) & (10 > Num) ):
            return Ones[Num]
        elif ( (10 <= Num) & (20 > Num) ):
            return Teens[Num%10]
        elif ( (20 <= Num) & (100 > Num) ):
            x1 = "{} {}".format( Tens[Num//10] , Ones[Num%10])
            return x1
        else:
            raise UnboundLocalError(f'This function expect number between 0:99 not {Num}')
    else:
        raise TypeError(f'This function expect integer argument insted of type {type(Num)} ')

if __name__ == '__main__': main()