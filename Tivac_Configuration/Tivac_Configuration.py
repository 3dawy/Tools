"""
Author: Khaled aladawy
Date: 31/1/2021
Time: 6:39 pm
Discription: This app generate port_lcfg files and system_control_lcfg files to configure tivac tm4c123gh6pm
"""

import Build_PortDriver_lcfg
import Build_System_Control_lcfg


Channels = ('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
            'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
            'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
            'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
            'E0', 'E1', 'E2', 'E3', 'E4', 'E5',
            'F0', 'F1', 'F2', 'F3', 'F4')





def GetInfo():
    Flag = 1
    Confg_Data = []
    NumberOfPins = 0
    
    while(Flag == 1):
        pin = input("Select pin: ").upper()
        if pin in Channels:
            Confg_Data.insert(NumberOfPins, ({"Pin":pin,
                                    "Dir": input("pin direction: ").upper(),
                                    "Function":input("pin function: ").upper(),
                                    "SlewRate":'DISABLE',
                                    "Current":4,
                                    "Attachment":'NOTCONNECTED',
                                    "ExtInt":'DISABLE'})
                             )
            if "ADC" == Confg_Data[NumberOfPins]['Function']:
                Confg_Data[NumberOfPins]['ADC_Module'] = input("ADC module number: ")
                
            NumberOfPins += 1
            while(True):
                Answer = input("Select another pin(Y/N): ").upper()
            
                if ("Y" == Answer):            
                    break
            
                elif("N" == Answer):
                    Flag = 0
                    break
                else:
                    print("Wrong answer please insert Y or N")
                
        else:
            print("please select from given options")
        
    
    return((Confg_Data, NumberOfPins))




def main():
    #Welcome msg.
    print("Configure your TivD_C pins")
    
    print(f"""Avilable pins: {Channels[0:8]} 
               {Channels[8:16]}
               {Channels[16:24]}
               {Channels[24:32]}
               {Channels[32:38]}
               {Channels[38:43]}""")
    
    Data = GetInfo()
    
    Build_PortDriver_lcfg.Configure_PortDriver(Data[0], Data[1])
    
    Clock = []
    
    
    for i in Data[0]:
        if "DIO" == i["Function"]:
            x = {"Peripheral":i["Function"], "Channel":i["Pin"][0]}
            if x in Clock:
                continue
            
        elif "ADC" == i["Function"]:
            x = {"Peripheral":i["Function"], "Module":i["ADC_Module"]}
            if x in Clock:
                continue
        
        Clock.insert(-1, x)
    
    Build_System_Control_lcfg.Configure_System_Control(Clock)
    
    
    
    
if __name__ == '__main__': main()