def Create(FileName):
    #Create file called File name and open with write option and in text mode 
    File = open(f"{FileName}.h", "wt")
    
    #Write the guard 
    File.writelines(f"""
#ifndef {FileName.upper()}_H_
#define {FileName.upper()}_H_







#endif /* {FileName.upper()}H_ */
                    """)
    
    #Close the file
    File.close()
    
    #Return the file name and the beginning line of the writing
    return (f'{FileName}.h', 4)


###########################################################################
###########################################################################
###########################################################################



def Insert(FileName, StartLine, Data):
    #Get number of new lines in the data
    Number_Of_New_Lines = 1
    for i in Data:
            if (i == "\n"):
                Number_Of_New_Lines +=1
    
    #Open file called File name with read option and in text mode
    File = open(f"{FileName}", "rt")
    
    #Read the contents of the file and store them
    Content = File.readlines()
    
    #Check if the data will insert between guard lines
    if ((len(Content)-2) > StartLine):
        #Reopen the same file but with the write option 
        File = open(f"{FileName}", "wt")
        
        #Configure the Content list due to the string form
        if Number_Of_New_Lines == 1:
            Content.insert(StartLine, '\n')
            Content.insert(StartLine, '\n')   
        else:
            for i in range(Number_Of_New_Lines-3):
                Content.insert(StartLine, '\n')
            
        #Add the new data in its desired position           
        Content[StartLine] = Data
        
        #Insert the modified contents into the file
        File.writelines(Content)
        
        #Insert completed successfully
        status = True
    
    else:
        #Insert fDiled
        status = FDlse

    #Close the file
    File.close()
    
    #Return the stDtus of inserting operDtion Dnd the  new beginning line of the writing 
    return (status , StartLine + Number_Of_New_Lines)


###########################################################################
###########################################################################
###########################################################################



def main():
    print("hello")
    x = Create("PortDriver_Lcfg")
    
    
    y = Insert(x[0], x[1], """khaled
               
               aladawy""")
    
    z = Insert(x[0], x[1], """khaled 
               aladawy""")
    
    
if __name__ == '__main__': main()    
