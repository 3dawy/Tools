"""
Author: Khaled Aladawy
Date: 31/1/2021
Time: 2:49 pm
Discription: This app creates makefile for ARM gcc tool chain
"""
import glob

def main():
    #Welcome msg.
    print("Create your own linker script for ARM GCC tool chain")
    
    #Get project name to create output files with same name.
    Project_Name = input("What is your project name? ")
    
    #Create list to store c files names.
    C_Files = []
    
    #Fill the list with c files names without .c extension.
    for f in glob.glob("*.c"):
        C_Files.append((f[0:-2]))
    
    #Get the linker script file name without .ld extension.    
    LS_File = (str(glob.glob("*.ld"))[2:-5])
    ########################################################
    ########################################################
    
    #Create file called Makefile. and open with write option and in text mode 
    Make_File = open('Makefile.', 'wt')
    
    #Start writing in make file with respect guidelines rules
    
    #Create variable(CC) to store compiler command
    Make_File.writelines("CC=arm-none-eabi-gcc \n")
    
    #Create variable(MACH) to store CPU arch
    Make_File.writelines("MACH=cortex-m4 \n")
    
    #Create variable(CFLAGS) to store compiler flags
    Make_File.writelines("CFLAGS= -c -mcpu=$(MACH) -mthumb -std=gnu11 -Wall -O0 \n")
    
    #Create variable(LDFLAGS) to store linker flags
    Make_File.writelines(f"LDFLAGS= -nostdlib -T {LS_File}.ld -Wl,-Map={Project_Name}.map \n")
    
    #Write make command
    Make_File.writelines("\nall:")
    
    #Make abject files
    for i in C_Files:
        Make_File.writelines(f"{i}.o ")
        
    #Make elf file    
    Make_File.writelines(f"{Project_Name}.elf \n\n")
    
    #Generate object files command
    for i in C_Files:
        Make_File.writelines(f"""{i}.o:{i}.c
\t$(CC) $(CFLAGS) -o $@ $^
    
""")
    
    #Generate elf file command
    Make_File.writelines(f"{Project_Name}.elf:")
    for i in C_Files:
        Make_File.writelines(f"{i}.o ")
    Make_File.writelines("\n\t$(CC) $(LDFLAGS) -o $@ $^ \n\n")
    
    
if __name__ == '__main__': main()