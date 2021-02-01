"""
Author: Khaled Aladawy.
Date: 28/1/2021
Time: 2:05 pm
Name: Say the time
"""
import Say_The_Numbers
import time
"""
Name: Write_Time(mode)
I/P: mode: type -> intger
           value -> 12 or 24
O/P: list (Hour, Minutes, Seconds, None) in case of i/p is 24 or
     list (Hour, Minutes, Seconds, pm/am) in case of i/p is 12
Discription: it take the mode of output (12hr mode or 24hr mode) and return the time in list of strings
"""
def Write_Time(mode = 12):
    if isinstance(mode, int):       #check input type
        if ( (12 == mode) | (24 == mode)):      #check input value
            Now = time.strftime("%H:%M:%S", time.localtime())     #get the time in string and form of HH : mm : ss
            Now = Now.split(':')    #split the string into list of  hours string, minutes string and seconds string
            Hr = int(Now[0])        #convert the  hours strings to integers
            Min = int(Now[1])       #convert the  mintues strings to integers
            Sec = int(Now[2])       #convert the  seconds strings to integers
            if ( (12 == mode) & (12 >= Hr) ):
                Status = "am"
            elif ( (12 == mode) & (12 < Hr) ):
                Hr = Hr - 12
                Status = "pm"
            else:
                Status = "hr"
            #convert the time to string    
            Hr = Say_The_Numbers.Number_Name(Hr)
            Min = Say_The_Numbers.Number_Name(Min)
            Sec = Say_The_Numbers.Number_Name(Sec)
            
            return (Hr, Min, Sec, Status)
        else:
            #error: unexpected value
            print(f"expected value is 12 or 24 not {mode}")
            #raise UnboundLocalError(f"expected value is 12 or 24 not {mode}")
    else:
        #error: unexpected data type
        print(f"expected type is integer not {type(mode)}")
        #raise TypeError(f"expected type is integer not {type(mode)}")
    
def main():
    n = int(input("""In which form do you want the time
insert 12 for 12hr       or 24 for 24hr
"""))
    x = Write_Time(n)
    if None != x:
        print(f"Time now is {x[0]} {x[3]} and {x[1]} mins and {x[2]} secs")
    input("enter any thing to close")
    
	
#use this command in cmd to create the exe file: pyinstaller --onefile file_name.py
    
if __name__ == '__main__': main ()
