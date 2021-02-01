"""
Author: Khaled aladawy
Date: 31/1/2021
Time: 2:49 pm
Discription: 
"""

import  Header_File



def Create_PortDriver_lcfg_h(Number_Of_Channels = 0):
    
    Info = Header_File.Create("PortDriver_Lcfg")

    File = {'name':Info[0], 'st.line':Info[1]}
    
    File['st.line'] = Header_File.Insert(File['name'], File['st.line'], f"""#include "PortDriver_Types.h"

#define NUM_OF_ACTIVATED_CHANNELS            {Number_Of_Channels}

extern PortDriver_CfgType PortDriver_CfgArr[NUM_OF_ACTIVATED_CHANNELS];""")[1]
    
    print(f"{File['name']} generated")
    
    
    
    
#####################################################################################
#####################################################################################
    
        
def Creat_PortDriver_lcfg_c():
    #Create file called PortDriver_Lcfg.c and open with write option and in text mode 
    File = open("PortDriver_Lcfg.c", "wt")
    
    File.writelines('\n \n \n \n')
    
    File.writelines('#include "PortDriver_Lcfg.h" \n')
    
    File.writelines('''PortDriver_CfgType PortDriver_CfgArr[NUM_OF_ACTIVATED_CHANNELS] =
{/* Channel		                 PortDriver_Channel_Direction             PortDriver_Channel_Current_mA                      PortDriver_Channel_SlewRate                PortDriver_Channel_Attachment                    PortDriver_Channel_Function             PortDriver_Channel_Exti  */
''')
    
    File.close()
    
    
    
    
#####################################################################################
#####################################################################################
    
    
def ConfgPin(Info):
    File = open("PortDriver_Lcfg.c", "at")

    File.writelines(f'  {{PORTDRIVER_CHANNEL_{Info["Pin"]},      ')
          
    
    File.writelines(f'PORTDRIVER_CHANNEL_DIRECTION_{Info["Dir"]},')
    
    
    File.writelines(f'      PORTDRIVER_CHANNEL_CURRENT_mA_{Info["Current"]},')
    
    
    File.writelines(f'                   PORTDRIVER_CHANNEL_SLEWRATE_{Info["SlewRate"]},')
    
    
    File.writelines(f'       PORTDRIVER_CHANNEL_ATTACHMENT_{Info["Attachment"]},')
    
    
    File.writelines(f'      PORTDRIVER_CHANNEL_FUNCTION_X_{Info["Function"]},')
    
    
    File.writelines(f',      PORTDRIVER_CHANNEL_EXTI_{Info["ExtInt"]} }},\n')
    
    File.close()
       
#####################################################################################
#####################################################################################
    
    
    

def Configure_PortDriver(Data, Pins_Number):
    
    Creat_PortDriver_lcfg_c()
    
    for i in Data:
        ConfgPin(i)
    
    
            
    print("PortDriver_Lcfg.c generated")        
    
    Create_PortDriver_lcfg_h(Pins_Number)
    
    print("Port Driver module configuration completed successfully")



def main():
    Configure_PortDriver()
    
    
    
    
    
if __name__ == '__main__': main()