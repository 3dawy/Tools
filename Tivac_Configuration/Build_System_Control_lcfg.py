

import Header_File



def Create_SYSCTR_LCFG_h(Number_Of_Peripherals = 0):
    
    Info = Header_File.Create("SYSCTR_LCFG")

    File = {'name':Info[0], 'st.line':Info[1]}
    
    File['st.line'] = Header_File.Insert(File['name'], File['st.line'], f"""include "SERVICE/std_types.h"

#define NUMBER_OF_PERIPHERALS                   {Number_Of_Peripherals}

typedef struct
{{
	uint16_t Peripheral;
	uint8_t  Channel;
}}SYSCL_Type;


extern SYSCL_Type garrstr_SYSCTR_Cfg[NUMBER_OF_PERIPHERALS];""")[1]
    
    print(f"{File['name']} generated")
       
#####################################################################################
#####################################################################################
    
    
    
def Create_SYSCTR_LCFG_c():
    #Create file called SYSCTR_LCFG.c and open with write option and in text mode 
    File = open("SYSCTR_LCFG.c", "wt")
    
    File.writelines('\n \n \n \n')
    
    File.writelines('#include "SYSCTR_LCFG.h" \n')
    
    File.writelines('''#define RCGC_GPIO                           0x608   //GPIO Peripheral
#define GPIO_PORTA                          0       //GPIO Channel A
#define GPIO_PORTB                          1       //GPIO Channel B
#define GPIO_PORTC                          2       //GPIO Channel C       
#define GPIO_PORTD                          3       //GPIO Channel D
#define GPIO_PORTE                          4       //GPIO Channel E
#define GPIO_PORTF                          5       //GPIO Channel F

#define RCGC_ADC                            0x638   //ADC Peripheral
#define ADC_Module_0                        0       //ADC Channel 0
#define ADC_Module_1                        1       //ADC Channel 1


SYSCL_Type garrstr_SYSCTR_Cfg[NUMBER_OF_PERIPHERALS]={''')
    
    File.close()
    
    
    
    
#####################################################################################
#####################################################################################


def ConfgPeripheralClock(Info):
    File = open("SYSCTR_LCFG.c", "at")

    if Info["Peripheral"] == "DIO":
        x = "RCGC_GPIO"
        y = f"GPIO_PORT{Info['Channel']}"
    elif Info["Peripheral"] == "ADC":
        x = "RCGC_ADC"
        y = f"ADC_Module_{Info['Module']}"
    
    File.writelines(f'{{{x}, {y}}},\n')
    
    
    File.close()
       
#####################################################################################

    
        
def Configure_System_Control(Peripheral):
    
    Create_SYSCTR_LCFG_c()
    
    for i in Peripheral:
        ConfgPeripheralClock(i)
    
    
    File = open("SYSCTR_LCFG.c", "at")
    File.writelines("};")
    File.close()
    
    print("SYSCTR_LCFG.c generated")        
    
    Create_SYSCTR_LCFG_h(len(Peripheral))
    
    print("System Control module configuration completed successfully")
