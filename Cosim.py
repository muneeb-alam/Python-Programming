# This file gets value and return values after time step of 5 minutes

#Permanent Needs for four time intervals
StandardConsumingDevicesPower=[20,200,200,100,100,200,200,100]
DSMPower=[0,300,240,200,200,300,240,200]

#Permanent Offers for four time intervals
MarketSolarGeneratingUnitPower=[100,1000,300,0,90,200,300,0]
MarketCogenerationUnitPower=[200,100,140,0,500,460,140,0]

#Conditional Needs or Offers
Common_Grid_Power=[300,-50,-300,200,50,-10,-190,200] # negative sign in power means that grid will acts as load and postive sign means grid has excess of electricity and will act as source
MarketBatteryPower=[250,250,250,250,250,250,250,250] # MarketMarketBattery power remains same all the time (assumption)
MarketBatteryCapacity=[35,80,20,0,0,80,20,0] # Only first entry of this array will be used in code. The rest will be updated after each time interval.
Reserve_Status=[0,0,0,0,1,1,1,1] # Reserve status for grid

def get_MarketBattery_SOC():
    return MarketBatteryCapacity
    
def get_MarketBattery_Power():
    return MarketBatteryPower
    
def get_MarketSolarGeneratingUnit_Power():
    return MarketSolarGeneratingUnitPower
    
def get_DSM_Power():
    return DSMPower

def get_StandardConsumingDevices_Power():
    return StandardConsumingDevicesPower
    
def get_MarketCogenerationUnit_Power():
    return MarketCogenerationUnitPower
    
def get_Common_Grid_Power():
    return Common_Grid_Power


# Output of optimizer

def return_MarketBattery_SOC():
    return MarketBatteryCapacity
    
def return_MarketBattery_Power():
    return MarketBatteryPower
    
def return_MarketSolarGeneratingUnit_Power():
    return MarketSolarGeneratingUnitPower
    
def return_DSM_Power():
    return DSMPower

def return_StandardConsumingDevices_Power():
    return StandardConsumingDevicesPower
    
def return_MarketCogenerationUnit_Power():
    return MarketCogenerationUnitPower
    
def return_Common_Grid_Power():
    return Common_Grid_Power

    
   

