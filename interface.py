from Classes import *

marketBatteryStorage.Power=2
marketBatteryStorage.PercentageCurrentCapacity=1
marketCogenerationUnit.Power=3
marketSolarGeneratingUnit.Power=4
standardConsumingDevices.Power=5
dSM.Power=6
commonGrid.Power=7

def get_MarketBattery_SOC():
    return marketBatteryStorage.PercentageCurrentCapacity
    
def get_MarketBattery_Power():
    return marketBatteryStorage.Power

def get_MarketCogenerationUnit_Power():
    return marketCogenerationUnit.Power
            
def get_MarketSolarGeneratingUnit_Power():
    return marketSolarGeneratingUnit.Power

def get_StandardConsumingDevices_Power():
    return standardConsumingDevices.Power

def get_DSM_Power():
    return dSM.Power
        
def get_Common_Grid_Power():
    return commonGrid.Power


def return_MarketBattery_SOC(OptimizedBatterySOC):
    #print 'SOC Updation'
    return OptimizedBatterySOC
 
            
def return_MarketBattery_Power(OptimizedBatteryPower):
    #print 'Power Updation'
    return OptimizedBatteryPower
    
def return_MarketCogenerationUnit_Power(OptimizedCogenerationPower):
    return OptimizedCogenerationPower
    
def return_MarketSolarGeneratingUnit_Power(OptimizedSolarGeneratingUnitPower):
    return OptimizedSolarGeneratingUnitPower

def return_StandardConsumingDevices_Power(OptimizedStandardConsumingDevicesPower):
    return OptimizedStandardConsumingDevicesPower
    
def return_DSM_Power(OptimizedDSMPower):
    return OptimizedDSMPower
    
def return_CommonGrid_Power(OptimizedCommonGridPower):
    return OptimizedCommonGridPower





    
   



    
   

