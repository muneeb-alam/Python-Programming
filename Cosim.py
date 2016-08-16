# This file gets value and return values after time step of 5 minutes

#Permanent Needs for four time intervals
PD_Power=[20,200,200,100,100,200,200,100]
DSM_Power=[0,300,240,200,200,300,240,200]

#Permanent Offers for four time intervals
PV_Power=[100,1000,300,0,90,200,300,0]
KWK_Power=[200,100,140,0,500,460,140,0]

#Conditional Needs or Offers
Common_Grid_Power=[300,-50,-300,200,50,-10,-190,200] # negative sign in power means that grid will acts as load and postive sign means grid has excess of electricity and will act as source
Battery_Power=[250,250,250,250,250,250,250,250] # Battery power remains same all the time (assumption)
Battery_Capacity=[35,80,20,0,0,80,20,0] # Only first entry of this array will be used in code. The rest will be updated after each time interval.
Reserve_Status=[0,0,0,0,1,1,1,1] # Reserve status for grid

def get_Battery_SOC():
    return Battery_Capacity
    
def get_Battery_Power():
    return Battery_Power
    
def get_PD_Power():
    return PD_Power
    
def get_DSM_Power():
    return DSM_Power

def get_PV_Power():
    return PV_Power
    
def get_KWK_Power():
    return KWK_Power
    
def get_Common_Grid_Power():
    return Common_Grid_Power
        
def return_Battery_SOC():
    return Battery_capacity
    
def return_Battery_Power():
    return Battery_Power


    
   

