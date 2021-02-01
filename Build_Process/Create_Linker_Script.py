"""
Author: Khaled Aladawy
Date: 30/1/2021
Time: 1:30 pm
Discription: This app creates linker script in .ld extention for ARM gcc tool chain
"""
def main():
    #Welcome msg
    print("Create your own linker script for ARM GCC tool chain")
    
    #Get the inputs from the user
    
    #Ask user to input the address in hex (input)
    #Convert the input string to decimal integer with respect that the string hold hex value (int(str, 16)),
    #because int function accept only decimal value in string 
    Flash_Start_Address = int( input( "FLASH start address (in hex) = 0x" ), 16 )
    
    #Ask user to input Flash length in kilo-byte
    Flash_Length = int( input( f'FLASH length (in K) = ') )
    
    #Ask user to input the address in hex (input)
    #Convert the input string to decimal integer with respect that the string hold hex value (int(str, 16))
    Sram_Start_Address = int( input("SRAM start address (in hex) = 0x"), 16  )
    
    #Ask user to input SRAM length in kilo-byte
    Sram_Length = int( input(f'SRAM length (in K) = ') )
    #############################################################
    #############################################################
    
    
    #List stores exist memories
    #Type list to allow the user to add other memories.
    #Type tuples to create constant values to avoid edit them by accident during programing.
    #Type dic to facilitate use it's values during writing the file or printing
    Memories = [({'name':'FLASH', 'st_add':Flash_Start_Address, 'length':Flash_Length, 'access':'r'}),
                ({'name':'SRAM',  'st_add': Sram_Start_Address, 'length':Sram_Length,  'access':'rw'})]
    
    #loop to add other memories if they exist and stores them and it's info in the Memories list.
    while(True):
        Answer = input('Is there another memory? (Y,N): ')
        if ( 'Y' == Answer.upper() ):
            #If there is another memory gets its info and store them in the Memories list.
            Memories.append ( ({'name'  :input("New Memory name is: ").upper(), #Convert the name to uppercase to follow linker script guideline rules during writing the file.
                                'st_add':int( input("New Memory start address is: 0x"),16), #Get the address in hex, because it is easy for the user.
                                'length':int( input("New Memory length (in kilo-byte)is: ") ), #Get the length in kilo-byte, because it is easy for the user.
                                'access':input("New Memory access (r, rw): ")
                              })
                            )
        else:
            #If no other memory stop the loop 
            break
    #############################################################
    #############################################################
    
    
    #List stores exist sections
    #Type list to allow the user to add other sections.
    #Type tuples to create constant values to avoid edit them by accident during programing.
    #Type dic to facilitate use it's values during writing the file or printing    
    Sections = [({'name':'isr_vector', 'run_add':'FLASH', 'load_add':'FLASH'}),
                ({'name':'text'      , 'run_add':'FLASH', 'load_add':'FLASH'}),
                ({'name':'rodata'    , 'run_add':'FLASH', 'load_add':'FLASH'}),
                ({'name':'data'      , 'run_add':'SRAM' , 'load_add':'FLASH'}),
                ({'name':'bss'       , 'run_add':'SRAM' , 'load_add':'SRAM' })]
    
    #Print the default sections and their info to the user.
    print("Sections are:")
    for i in Sections:
        print(f"section: {i['name']}, start label: _s{i['name']}, end label: _e{i['name']}")
    
    #loop to add other sections if they exist and stores them and it's info in the Section list.
    while(True):
        Answer = input("Do you want any other section? (Y,N): ")
        if ('Y' == Answer.upper()):
            #If there is another section gets its info and store them in the Sections list.
            Name = input("What is the new section name? ").lower() #Convert the name to lowercase to follow linker script guideline rules during writing the file.
            Run_add = input("What is the run memory? ").upper()    #Convert the run memory name to upprcase to follow linker script guideline rules during writing the file.
            Load_add = input("What is the load memory? ").upper()  #Convert the load memory name to uppercase to follow linker script guideline rules during writing the file.
            Sections.append( ( {'name': Name, 'run_add':Run_add, 'load_add':Load_add} ) ) #Stores the new section and its info to Section list.
            
            #Show the user the new section start label name and end label name. 
            print(f"{Sections[-1]['name']}'s start label is _s{Sections[-1]['name']} and end label is _e{Sections[-1]['name']}")
        else:
            #If no other section stop the loop
            break
    ##################################################################
    ##################################################################
            
    #Create file called Linker_Script.ld and open with write option and in text mode 
    Linker_Script_File = open('Linker_Script.ld', 'wt')
    
    #Start writing in linker script file
    Linker_Script_File.writelines("ENTRY(Reset_Handler)")
    
    #Beginning defining the memories 
    Linker_Script_File.writelines(f"""
MEMORY
{{                                """) 
    
    #Loop on writing all memories in the target
    for i in Memories:
        Linker_Script_File.writelines(f"""
    {i['name']}({i['access']}x):ORIGIN ={hex(i['st_add'])},LENGTH ={i['length']}K """)        
    
    #End defining the memory
    Linker_Script_File.writelines(f"""
}}""")
####################################################

    #Beginning defining the sections
    Linker_Script_File.writelines(f"""
                                  
                                  
SECTIONS
{{                                """)
    
    #Loop on writing all sections in the application
    for i in Sections:
        Linker_Script_File.writelines(f"""
    .{i["name"]} :
    {{
        _s{i["name"]} = .;
        *(.{i["name"]})
        _e{i["name"]} = .;            """)
    
        #Define the run address and load address following linker script guideline rules.
        if( (i['run_add']) == (i['load_add']) ):    
            Linker_Script_File.writelines(f"""
    }}> {i['run_add']}
                                      """)
        else:
            Linker_Script_File.writelines(f"""
    }}> {i['run_add']} AT> {i['load_add']}
                                      """)
    
    #End defining the sections
    Linker_Script_File.writelines(f"""
}}""")
    
if __name__ == '__main__': main()