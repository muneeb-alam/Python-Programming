import time
from interface import *
from Classes import *
 

try:   
    print 'C'
    print 'marketBatteryStorage.PercentageCurrentCapacity',marketBatteryStorage.PercentageCurrentCapacity
    print 'marketBatteryStorage.Power',marketBatteryStorage.Power
    print 'marketCogenerationUnit.Power',marketCogenerationUnit.Power
    print 'marketSolarGeneratingUnit.Power',marketSolarGeneratingUnit.Power
    print 'standardConsumingDevices.Power',standardConsumingDevices.Power
    print 'dsm.Power',dSM.Power
    print 'commonGrid.Power',commonGrid.Power
except:
    pass

try:
    print 'D'
    marketBatteryStorage.PercentageCurrentCapacity=int(get_MarketBattery_SOC())
    marketBatteryStorage.Power=int(get_MarketBattery_Power())
    marketCogenerationUnit.Power=int(get_MarketCogenerationUnit_Power())
    marketSolarGeneratingUnit.Power=int(MarketSolarGeneratingUnit_Power())
    standardCosumingDevices.Power=int(get_StandardConsumingDevices_Power())
    dSM.Power=int(get_DSM_Power())
    commonGrid.Power=int(get_Common_Grid_Power())
    
    print 'MarketBatteryStorage.PercentageCurrentCapacity',marketBatteryStorage.PercentageCurrentCapacity
    print 'MarketBatteryStorage.Power',marketBatteryStorage.Power
    print 'MarketCogenerationUnit.Power',marketCogenerationUnit.Power
    print 'MarketSolarGeneratingUnit.Power',marketSolarGeneratingUnit.Power
    
    print 'StandardCosumingDevices',standardCosumingDevices
    print 'dSM.Power',dSM.Power
    print 'commonGrid.Power',commonGrid.Power

except: 
    pass

# Output of optimizer


OptimizedBatterySOC=10
OptimizedBatteryPower=9
OptimizedCogenerationPower=8
OptimizedSolarGeneratingUnitPower=7
OptimizedStandardConsumingDevicesPower=6
OptimizedDSMPower=5
OptimizedCommonGridPower=4

try:
    marketBatteryStorage.PercentageCurrentCapacity=return_MarketBattery_SOC(OptimizedBatterySOC)
    print 'MarketBatteryCapacity',MarketBatteryCapacity
    marketBatteryStorage.Power=return_MarketBattery_Power(OptimizedBatteryPower)
    #print 'MatteryBatteryPower',MarketBatteryPower
    marketCogenerationUnit.Power=return_MarketCogenerationUnit_Power(OptimizedCogenerationPower)
    marketSolarGeneratingUnit.Power=return_MarketSolarGeneratingUnit_Power(OptimizedSolarGeneratingUnitPower)
    standardConsumingDevices.Power=return_StandardConsumingDevices_Power(OptimizedStandardConsumingDevicesPower)
    dSM.Power=return_DSM_Power(OptimizedDSMPower)
    commonGrid.Power=return_CommonGrid_Power(OptimizedCommonGridPower)
except:
    pass

seconds=0
while seconds<5:
    #print seconds
    time.sleep(1)
    seconds=seconds+1
    if seconds is 5:
        print '\nUpdation\n'

try:   
    #print 'C'
    print 'marketBatteryStorage.PercentageCurrentCapacity',marketBatteryStorage.PercentageCurrentCapacity
    print 'marketBatteryStorage.Power',marketBatteryStorage.Power
    print 'marketCogenerationUnit.Power',marketCogenerationUnit.Power
    print 'marketSolarGeneratingUnit.Power',marketSolarGeneratingUnit.Power
    print 'standardConsumingDevices.Power',standardConsumingDevices.Power
    print 'dsm.Power',dSM.Power
    print 'commonGrid.Power',commonGrid.Power
except:
    pass
