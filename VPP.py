# To run the code without primary reserve and rectify infinite loop problem
# To update the charging and discharging price of the battery

#========================Functions============================================#

#***********************Source_BatteryStorage_Functions***********************#

#This function returns updated price of BatteryStorage according to current capacity.

def BatteryStorage_source_DOD(x):
     #return (1.939E-08*(x**4) - 4.065E-06*(x**3) + 0.000326*(x**2) - 0.01141*x + 0.2219)*100
     #return -3.551E-18*(x**2)+0.05*x+20     
     return battery.discharging_price

# This function is used when Battery acts as source and need(load) power is more than source power.
# Current Capacity is updated, profit calculations for battery is done here when battery provide energy to PD and DSM.
# Dicharge factor is also defined which tells how much of battery capacity should be used while acting as....
# ....primary reserve for grid.
# No profit calculation when grid acts as need as grid operator has to pay a fixed amount to battery owner....
#... independent of power shared. 

def BatteryStorage_source_need_power_greater_than_offer_power(need,offer):
    print 'Current Capacity:', offer.percentage_current_capacity    
    if need.power >= temp_need:
        print 'case A1'
        used_power=temp_offer      
        if need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
            pass
        elif need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity>=discharge_factor:
            return
        print offer.name,'Profit:',offer.profit
        offer.profit=profit_calculation(offer,need,used_power)
        need.power=need.power-temp_offer
        offer.power=offer.power-temp_offer
        
    elif need.power < temp_need:
        print 'case A2'
        print need.power,temp_need
        if offer.power-need.power>=0:
            print 'case A21'
            used_power=need.power
            if need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
                pass
            elif need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity>=discharge_factor:
                return
            print offer.name,'Profit:',offer.profit
            offer.profit=profit_calculation(offer,need,used_power)
            offer.power=offer.power-need.power
            need.power=0
        elif offer.power-need.power<0 :
            print 'case A22'
            used_power=offer.power
            print used_power
            if need.name is 'Common_Grid'and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
                pass
            elif need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity>=discharge_factor:
                return
            print offer.name,'Profit:',offer.profit
            offer.profit=profit_calculation(offer,need,used_power)
            need.power=need.power-offer.power
            offer.power=0
            
          
    offer.percentage_current_capacity=((offer.percentage_current_capacity*0.01*offer.usable_capacity_in_kWh)-(used_power*hours/4))/offer.usable_capacity_in_kWh*100                       
    print 'Capacity after Discharge', offer.percentage_current_capacity
    print 'Remaining Need Power',need.power
    print 'Remaining Offer Power',offer.power
    
    if (offer.power is 0 or offer.percentage_current_capacity<=0):
        print 'Battery peak power for this interval has been used'
    offer.discharging_price=BatteryStorage_source_DOD(100-offer.percentage_current_capacity) # new price after discharge
    offer.price=offer.discharging_price    
    print 'New Discharging Price',offer.discharging_price
    return



# This function is used when Battery acts as source and need(load) power is less than source power.
# Current Capacity is updated, profit calculations for battery is done here when battery provide energy to PD and DSM.
# Dicharge factor is also defined which tells how much of battery capacity should be used while acting as....
# ....primary reserve for grid.
# No profit calculation when grid acts as need as grid operator has to pay a fixed amount to battery owner....
#... independent of power shared. 


def BatteryStorage_source_need_power_less_than_offer_power(need,offer):
     print 'Current Capacity:', offer.percentage_current_capacity                    
     if need.power >= temp_need:
         print 'case B1'
         used_power=temp_need
         if need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
             pass
         elif need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity>=discharge_factor:
            return  
         print offer.name,'Profit', offer.profit
         offer.profit=profit_calculation(offer,need,used_power)
         offer.power=offer.power-temp_need
         need.power=need.power-temp_need
         
     elif need.power < temp_need:
         print 'case B2'
         if offer.power-need.power>=0:
             print 'case B21'
             used_power=need.power
             if need.name is 'Common_Grid'and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
                 pass
             elif need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity>=discharge_factor:
                return     
             print offer.name,'Profit=',offer.profit  
             offer.profit=profit_calculation(offer,need,used_power)
             offer.power=offer.power-need.power
             need.power=0
         elif offer.power-need.power<0:
            print 'case B22'
            used_power=offer.power
            if need.name is 'Common_Grid'and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
                pass
            elif need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity>=discharge_factor:
                return  
            
            print offer.name,'Profit=',offer.profit 
            offer.profit=profit_calculation(offer,need,used_power)
            need.power=need.power-offer.power
            offer.power=0
            
  
               
     offer.percentage_current_capacity=((offer.percentage_current_capacity*0.01*offer.usable_capacity_in_kWh)-(used_power*hours/4))/offer.usable_capacity_in_kWh*100                       
     print 'Capacity after Discharge', offer.percentage_current_capacity        
     print 'Remaining Need Power',need.power
     print 'Remaining Offer Power',offer.power,'\n'
     if (offer.power is 0 or offer.percentage_current_capacity<=0):
        print 'Battery peak power has been used'
     offer.discharging_price=BatteryStorage_source_DOD(100-offer.percentage_current_capacity) # new price after discharge
     offer.price=offer.discharging_price     
     print 'New Discharging Price',offer.discharging_price
     return

#***********************Load_BatteryStorage_Functions_End*********************#

# This function is used when Battery acts as need and need power is less than source power.
# Current Capacity is updated, profit calculations for PV and KWK is done here.


def BatteryStorage_load_need_power_less_than_offer_power(need,offer):
        need.price=need.charging_price
        if  need.power >= temp_need:    
            print 'case C1'
            used_power=temp_need
            if offer.name is 'SolarGeneratingUnit' or offer.name is 'KWK':
                print 'case C11'
                offer.profit=profit_calculation(offer,need,used_power)
                need.profit=profit_calculation_battery_need(offer,need,used_power)
                print offer.name, 'Profit=',offer.profit
                print need.name,'Profit=',need.profit
            offer.power=offer.power-temp_need
            need.power=need.power-temp_need
            need.percentage_current_capacity=need.percentage_current_capacity+((temp_need*hours/4))/need.usable_capacity_in_kWh*100
            print 'need CC=', need.percentage_current_capacity
            
            if need.percentage_current_capacity>=99 and need.percentage_current_capacity<=100:
                print 'battery is fully charged now'        
            print 'Current Capacity',need.percentage_current_capacity
            return need.percentage_current_capacity
            
        elif need.power < temp_need:
            print 'case C2'
            if offer.power-need.power>=0:
                print 'case C21'
                used_power=need.power
                if offer.name is 'SolarGeneratingUnit' or offer.name is 'KWK':
                    print 'case C211'                    
                    offer.profit=profit_calculation(offer,need,used_power)
                    need.profit=profit_calculation_battery_need(offer,need,used_power)
                    print offer.name, 'Profit=',offer.profit
                    print need.name,'Profit=',need.profit                    
                offer.power=offer.power-need.power
                need.power=0
            elif offer.power-need.power<0:
                print 'case C22'
                used_power=offer.power
                if offer.name is 'SolarGeneratingUnit' or offer.name is 'KWK' :
                    offer.profit=profit_calculation(offer,need,used_power)
                    need.profit=profit_calculation_battery_need(offer,need,used_power)      
                    print offer.name, 'Profit=',offer.profit
                    print need.name,'Profit=',need.profit
                need.power=need.power-offer.power
                offer.power=0
                
            need.percentage_current_capacity=need.percentage_current_capacity+((used_power*hours/4))/need.usable_capacity_in_kWh*100
            print 'Current Capacity=',need.percentage_current_capacity
            if need.percentage_current_capacity>=99 and need.percentage_current_capacity<=100:
                print 'battery is fully charged now'          
            print 'Current Capacity',need.percentage_current_capacity
        return
        
# This function is used when Battery acts as need and need power is less than source power.
# Current Capacity is updated, profit calculations for PV and KWK is done here.     
        
def BatteryStorage_load_need_power_more_than_offer_power(need,offer):
    need.price=need.charging_price        
    if  need.power >= temp_need: 
        print 'case D1'
        used_power=temp_offer
        if offer.name is 'SolarGeneratingUnit' or offer.name is 'KWK':
            print 'case D11'
            offer.profit=profit_calculation(offer,need,used_power)
            print offer.name, 'Profit=',offer.profit
            need.profit=profit_calculation_battery_need(offer,need,used_power)
            print need.name,'Profit=',need.profit
        need.power=need.power-temp_offer
        offer.power=offer.power-temp_offer
        
        need.percentage_current_capacity=need.percentage_current_capacity+((temp_offer*hours/4))/need.usable_capacity_in_kWh*100
        print 'Current Capacity=',need.percentage_current_capacity    
        
        if need.percentage_current_capacity>=99 and need.percentage_current_capacity<=100:
            print 'battery is fully charged now'          
        print 'battery current capacity',need.percentage_current_capacity
        
    elif need.power < temp_need:
        print 'case D2'
        if offer.power-need.power>=0:
            print 'case D21'
            used_power=need.power
            if offer.name is 'SolarGeneratingUnit' or offer.name is 'KWK':
                print 'case D211'                
                offer.profit=profit_calculation(offer,need,used_power)
                print offer.name, 'Profit=',offer.profit
                need.profit=profit_calculation_battery_need(offer,need,used_power)
                print need.name,'Profit=',need.profit  
            offer.power=offer.power-need.power
            need.power=0
            
        elif offer.power-need.power<0:
            print 'case D22'
            used_power=offer.power
            if offer.name is 'SolarGeneratingUnit' or offer.name is 'KWK':                
                print 'case D222'
                offer.profit=profit_calculation(offer,need,used_power)
                print offer.name, 'Profit=',offer.profit
                need.profit=profit_calculation_battery_need(offer,need,used_power) 
                print need.name,'Profit=',need.profit
            need.power=need.power-offer.power
            offer.power=0
        
        need.percentage_current_capacity=need.percentage_current_capacity+((used_power*hours/4))/need.usable_capacity_in_kWh*100       
        if need.percentage_current_capacity>=100:
            print 'battery is fully charged now'                     
        print 'Current Capacity',need.percentage_current_capacity       
        print need.percentage_current_capacity
    return

#**************************PV,KWK or Grid Functions********************************#

# This function is used when PV, KWK or Grid are used as source of electricity and they have less power than needed.
# Profit calculations for theses sources is also done here.


def pv_or_KWK_or_Grid_need_power_greater_than_offer_power(need,offer):
    if need.name is 'BatteryStorage' and need.percentage_current_capacity<100.0 and reserved_for_grid is 0:
        print 'case E1'
        BatteryStorage_load_need_power_more_than_offer_power(need,offer)
        
    elif need.name is not 'BatteryStorage':
        print 'case E2'
        if need.power >= temp_need:
            print 'case E21'
            if offer.name is not 'BatteryStorage':
                print 'case E211'
                used_power=temp_offer
                offer.profit=profit_calculation(offer,need,used_power)
                print offer.name,'Profit=',offer.profit
            need.power=need.power-temp_offer
            offer.power=offer.power-temp_offer
        elif need.power < temp_need:
            print 'case E22'
            if offer.power-need.power>=0:
                print 'case E221'
                if offer.name is not 'BatteryStorage':
                    used_power=need.power
                    offer.profit=profit_calculation(offer,need,used_power)
                    print 'Profit=',offer.profit       
                offer.power=offer.power-need.power
                need.power=0
            elif offer.power-need.power<0:
                print 'case E222'
                if offer.name is not 'BatteryStorage':                
                    used_power=offer.power
                    offer.profit=profit_calculation(offer,need,used_power)
                    print 'Profit=',offer.profit       
                need.power=need.power-offer.power
                offer.power=0          
    print 'Remaining Need Power',need.power
    print 'Remaining Offer Power',offer.power,'\n'
    return
    

# This function is used when PV, KWK or Grid are used as source of electricity and they have more power than needed.
# Profit calculations for theses sources is also done here.    
        
def pv_or_KWK_or_Grid_need_power_less_than_offer_power(need,offer):      
    if need.name is 'BatteryStorage' and need.percentage_current_capacity<100.0 and reserved_for_grid is 0:
        print 'case F1'
        BatteryStorage_load_need_power_less_than_offer_power(need,offer)
      
    elif need.name is not 'BatteryStorage':
        print 'case F2'
        if need.power >= temp_need:
            print 'case F21'
            if offer.name is not 'BatteryStorage':
                print 'case F211'
                used_power=temp_need
                offer.profit=profit_calculation(offer,need,used_power)
                print used_power,offer.name,offer.power,offer.price,need.name,need.power,need.price
                print offer.name,'Profit=',offer.profit
            offer.power=offer.power-temp_need
            need.power=need.power-temp_need
        elif need.power < temp_need:
            print 'case F22'
            if offer.power-need.power>=0:
                print 'case F221'
                if offer.name is not 'BatteryStorage':
                    print 'case F2211'
                    used_power=need.power
                    offer.profit=profit_calculation(offer,need,used_power)
                    print offer.name,'Profit=',offer.profit     
                offer.power=offer.power-need.power
                need.power=0
            elif offer.power-need.power<0:
                print 'case F222'
                if offer.name is not 'BatteryStorage':
                    used_power=offer.power
                    offer.profit=profit_calculation(offer,need,used_power)
                    print offer.name,'Profit=',offer.profit                     
                need.power=need.power-offer.power
                offer.power=0
            
    print 'Remaining Need Power',need.power,
    print 'Remaining Offer Power',offer.power,'\n'
    return

#***********************Profit Calculations***********************************#

# This function is used to calculate profits of PV, battery, KWK and grid.
# For the grid case, we calculate profit is calculated on fixed price and used energy...
#...but for PV, KWK and battery, profit is calculated based on difference of need price and source price.

def profit_calculation(offer,need,used_power):
    if need.name is not 'Common_Grid' and offer.name is not 'Common_Grid':
        offer.profit=offer.profit+(used_power*(hours)/4*need.price-used_power*(hours)/4*offer.price)
    elif offer.name is 'Common_Grid':
        offer.profit=offer.profit+(used_power*(hours)/4*offer.price)   
        print 'Grid profits',offer.profit
    return offer.profit
    
def profit_calculation_battery_need(offer,need,used_power):
    need.profit=need.profit-(used_power*(hours)/4*need.price-used_power*(hours)/4*offer.price)
    return need.profit     
        
# This function is used to move to next source to meet the required power of one need
#....based on the minimum price source. If one source is depleted, it moves on to next
#...source until either all the sources are depleted or need demand is fulfilled.
  
def Removing_Zero_Power_Sources(offers,count):
     #print 'length of offers',len(offers)
     if offers[0].power is 0:
         if offers[1].power is 0:
             if offers[2].power is 0:
                 if len(offers)>3:
                     if offers[3].power is 0:
                         count=0
                         return count
                     else:
                         count =3
                         return count
             elif offers[2].power is not 0:
                 count=2
                 return count
         elif offers[1].power is not 0:
            count=1
            return count
     elif offers[0].power is not 0:
        count=0
        return count
        
# This function is used to determine the status of battery. If it is not reserved for grid
#..in next time interval, it will act as need if combined power of PV and KWK is more than
#...combined power of PD and DSM and in this case battery will be charged. If it is not the case, 
#...then battery will act as source and meet the need demands. If battery is reserved for grid,then
#...it will act as source or load depending on the excess or deficit of power in grid in next time interval.
        
def status_of_BatteryStorage(offers,needs):
    index=0
    for offer in offers:
        if offer.name is 'BatteryStorage' and reserved_for_grid is not 1:
            if ((pv.power + kwk.power)>(pd.power + dsm.power)):                
                offer.price=offer.charging_price
                del(offers[index])
                print 'Need Charging Price:',offer.charging_price
            else:
                index_BatteryStorage=index_of_BatteryStorage(needs)
                offer.price=BatteryStorage_source_DOD(100-offer.percentage_current_capacity)              
                del(needs[index_BatteryStorage])
                print 'Offer Discharging Price',offer.price
            
        elif offer.name is 'BatteryStorage' and reserved_for_grid is 1:
                if common_grid.power>0.0:
                    del(offers[index])
                    print 'battery acting as a need to support the grid'
                elif common_grid.power<0.0:
                    print 'battery acting as a source to support the grid'
                    index_BatteryStorage=index_of_BatteryStorage(needs)
                    del(needs[index_BatteryStorage])                                                                          
        else:
            index=index+1
            continue
    return

# This function gives back index of battery which is used in above function.
def index_of_BatteryStorage(needs):
    index=0
    for need in needs:
        if need.name is 'BatteryStorage':
            break
        else:
            index=index+1
    return index
    
# This function defines the status of the grid based on the deficit or excess of power.
# If grid power is positive, it means that grid has excess power and if it is negative, 
#...it means that grid will act as need.
    
def status_of_Grid(offers,needs):
    index=0
    for offer in offers:
        if offer.name is 'Common_Grid':
            if offer.power<0.0:  
                index_Grid=index_of_Grid(offers)
                offer.price=offer.feed_in_price
                del(offers[index_Grid])
                needs=sort_price_descending(needs) 
                offers=sort_price_ascending(offers)
                print 'Grid acting as Need with price:',offer.price
            elif offer.power>=0.0:
                index_Grid=index_of_Grid(needs)
                print index_Grid
                offer.price=offer.draw_out_price
                del(needs[index_Grid])
                needs=sort_price_descending(needs) 
                offers=sort_price_ascending(offers)
                print 'Grid will act as a source with price',offer.price
        else:
            index=index+1
            continue
    return 

# This function returns the index of grid which is used in the above function.    
def index_of_Grid(needs):
    index=0
    for need in needs:
        if need.name is 'Common_Grid':
            break
        else:
            index=index+1
    return index

# This function is used to sort needs and offers on the basis of price in 
#...descending and ascending order respectively.

def sorting_needs_and_offers(needs,offers): 
    needs=sorted(needs, key=lambda k: k.price, reverse = True) 
    offers=sorted(offers, key=lambda k: k.price)
    print_needs(needs)
    print_offers(offers)


def print_needs(needs):
    print 'Needs:'
    for need in needs:
        if need.name is 'BatteryStorage':
            print 'Name', need.name,'Power',need.power, 'Price', need.price,'(current capacity in %)',need.percentage_current_capacity,'usbale_capacity',need.usable_capacity_in_kWh,'kWh ','Profit',need.profit
        else:
            print 'Name',need.name,'Power', need.power,'Price',need.price
    print '\n'
    
    
def print_offers(offers):
    print 'Offers:' 
    for offer in offers:
        if offer.name is 'BatteryStorage':
            print 'Name', offer.name,'Power',offer.power, 'Price', offer.price,'Usable capacity',offer.usable_capacity_in_kWh,'(current capacity in %)',offer.percentage_current_capacity,'Profit',offer.profit
        else:
            print 'Name', offer.name,'Power',offer.power, 'Price', offer.price
            if offer.name is not'Common_Grid':
                print 'Profit',offer.profit
    print '\n'

def printPowers(needs,offers):

        print 'Battery_capacity',Battery_capacity
        print 'PV Power',PV_list
        print 'KWK Power',KWK_list
        print 'Common_Grid Power',Common_Grid_list
        print 'PD Power',PD_list
        print 'DSM Power',DSM_list
        print 'PV Profits',pv_profits
        print 'KWK Profits',kwk_profits
        print 'Battery Profits',battery_profits
        print  'Common Grid Profits',common_grid_profits
        
def PV_Power_Profile():
    temp=list()
    with open('PV_data.csv') as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            p=row[1]
        
            temp.append(p)
    return temp
#========================Functions_End=============================================#

#========================Needs=====================================================#

import matplotlib.pyplot as plt
import csv
from Classes import * 


discharge_factor=99 # How much the battery should be discharged while supporting the grid
N=5.0 # no of iterations  (to be written in floating form) 
x=3 # break point
hours=4.0
reserved_for_grid=0
primary_reserve_status=0

# initialization of lists for profit calculations# 
pv_profits=list() 
kwk_profits=list()
battery_profits=list()
common_grid_profits=list()

#initialization of lists for power calculations#
Battery_capacity=list()
PV_list=list()
KWK_list=list()
PD_list=list()
DSM_list=list()
Common_Grid_list=list()

#Permanent Needs for four time intervals
PD_Power=[100,200,200,100,100,200,200,100]
DSM_Power=[200,300,240,200,200,300,240,200]

#Permanent Offers for four time intervals
PV_Power=[90,200,300,0,90,200,300,0]
KWK_Power=[400,460,140,0,400,460,140,0]

#Conditional Needs or Offers
Common_Grid_Power=[0,-1,-190,200,50,-1,-190,200] # negative sign in power means that grid will acts as load and postive sign means grid has excess of electricity and will act as source
Battery_Power=[250,250,250,250,250,250,250,250] # Battery power remains same all the time (assumption)
Battery_Capacity=[0,80,20,0,0,80,20,0] # Only first entry of this array will be used in code. The rest will be updated after each time interval.
Reserve_Status=[0,0,0,1,1,1,1,1] # Reserve status for grid

#Needs
#PD_Power=[300,250,50,0]
#DSM_Power=[200,400,500,0]
#Battery_Power=[250,250,250,250]

#Offers
#PV_Power=[0,900,500,100]
#KWK_Power=[0,200,50,5]
#Common_Grid_Power=[500,0,-75,0]
#Battery_Capacity=[0,80,20,0]
#Reserve_Status=[0,0,0,0]

for t in range(int((hours*60)/15)):
    print 'iteration number:',t,'\nTime',t*15,'minutes'
    pv.power=int(PV_Power[t])
    kwk.power=int(KWK_Power[t])
    pd.power=int(PD_Power[t])
    dsm.power=int(DSM_Power[t])
    battery.power=int(Battery_Power[t])
    primary_reserve_status=int(Reserve_Status[t])
    common_grid.power=int(Common_Grid_Power[t])
    battery.percentage_current_capacity=int(Battery_Capacity[t])
    if t is not 0: # To update the value of battery capacity after each interval 
        battery.percentage_current_capacity=int(Battery_capacity[t-1])  
        print 'battery capacity',battery.percentage_current_capacity
    battery.capacity_for_grid=battery.percentage_current_capacity  # reference to determine how much battery should be discharged/charged while supporting the grid
    needs=([pd,dsm,battery,common_grid]) 
    offers = ([pv,kwk,battery,common_grid]) 
    sorting_needs_and_offers(needs,offers)
    print "Status of Battery:",status_of_BatteryStorage(offers,needs)
    print 'Status of Grid',status_of_Grid(offers,needs)
    sorting_needs_and_offers(needs,offers) # function which sorts needs on basis of price in descending order and sorts offers on basis of price in ascending order
    temp_offer=None
    count=0 
    print 'Primary Reserve Status', primary_reserve_status,'Reserved for Grid', reserved_for_grid
    for need in needs:
        if need.name is 'Common_Grid':
            need.power=need.power*-1
            print 'Common Grid Power',need.power
        temp_need=need.power/N
        temp_price=need.price/N
        print 'Need name', need.name, 'required Power',need.power 
        if need.power<=0 :continue
        n=0
        iteration_var=0
        print 'iteration_var',iteration_var # to allow all the power sources to be used to meet load demands
        
        while n < (int(N)) and need.power>0.1 and iteration_var<(int(N+20)):
            
            print 'n=',n, 'reserved_for_grid',reserved_for_grid

            if (battery.power >=0 and battery.percentage_current_capacity>=0.0) or (pv.power or kwk.power or common_grid.power):
                pass
            else:
                print 'all sources are depleted'
                break
            
            if count<len(offers):
                offer=offers[count]
                
 #=====================================For Primary Reserve Settings===============================================#               
            if need.name is 'BatteryStorage' and primary_reserve_status is 1:
                if need.percentage_current_capacity>79: 
                    print 'Primary Reserve Mode, Battery will act as reserve for grid in next interval'
                    reserved_for_grid=1
                    break
                
            elif offer.name is 'BatteryStorage' and primary_reserve_status is 1:
                print offer.percentage_current_capacity
                if offer.percentage_current_capacity<21:
                    print 'Primary Reserve Mode, Battery will act as offer for grid in next interval'
                    if reserved_for_grid is 0:
                        offer.power=0
                        if count<=2:
                            count=count+1
                            offer=offers[count]
                        reserved_for_grid =1
                        primary_reserve_status=0
                        print 'updation'
                        n=0
                        continue
            elif battery.percentage_current_capacity>21 and battery.percentage_current_capacity<79 and primary_reserve_status is 1:
                    if (pd.power is 0 or dsm.power is 0) and offer.name is 'BatteryStorage' and offer.power>0:
                        print 'reserved for grid'
                        reserved_for_grid=1
                        primary_reserve_status=0
                        
 #=====================================For Primary Reserve Settings===============================================#

                        
#=================Grid reserve case when battery supplies electricity to grid======================================#
                                     
            if reserved_for_grid is 1 and need.name is 'Common_Grid':
                if battery in needs:
                    n=n+N
                    print 'n',n
                    break
                else:
                    offer=offers[index_of_BatteryStorage(offers)]
                    print 'Offer name is Battery for Grid', offer.name
                    
            if reserved_for_grid is 0 and need.name is 'Common_Grid':
                n=n+N
                continue
                
            if reserved_for_grid is 1 and need.name is 'BatteryStorage':
                offer=offers[index_of_Grid(offers)]
                print 'Offer name is Grid for battery', offer.name
                
                
#=================Grid reserve case when battery supplies electricity to grid======================================#

                
            print 'Offer',offer.name, 'Offered Power',offer.power,'Reserve status',reserved_for_grid
            if temp_offer is None and n is 0:
                temp_offer=offer.power/N
            elif n is 0 and temp_offer is not None:
                temp_offer=offer.power/N
                if (int(N)==1):
                    temp_need=need.power/1.0
            print 'temp_need',temp_need,'temp_offer',temp_offer

#=======================For Needs other than Grid==============================================================#            
            if need.name is not 'Common_Grid':
                if temp_need-temp_offer>=0 and offer.price<=need.price and offer.power>0:
                    print 'A'         
                    if offer.name is not 'BatteryStorage':
                        print 'AA'                            
                        pv_or_KWK_or_Grid_need_power_greater_than_offer_power(need,offer)
                            
                    elif offer.name is 'BatteryStorage' and offer.percentage_current_capacity>0.0 and temp_need>=temp_offer and reserved_for_grid is 0:
                        print 'AB'                            
                        BatteryStorage_source_need_power_greater_than_offer_power(need,offer)
               
                elif temp_need -temp_offer<0 and offer.price <= need.price and offer.power>0:
                    print 'B',reserved_for_grid                   
                    if offer.name is not 'BatteryStorage':                    
                        print 'BA'                            
                        pv_or_KWK_or_Grid_need_power_less_than_offer_power(need,offer)
                        
                    elif  offer.name is 'BatteryStorage' and offer.percentage_current_capacity >0.0 and temp_need<=temp_offer and reserved_for_grid is 0:       
                        print 'BB'                            
                        BatteryStorage_source_need_power_less_than_offer_power(need,offer)  

#=======================For Needs other than Grid==============================================================#                        


#=======================Case when Grid acts as Need==============================================================#
         
            elif need.name is 'Common_Grid' and reserved_for_grid is 1 and offer.name is 'BatteryStorage': 
                print 'C'
                if temp_need-temp_offer>=0 and offer.power>0 :
                    print 'C'
                    if offer.percentage_current_capacity>0.0 and reserved_for_grid is 1:
                        print 'CA'                            
                        BatteryStorage_source_need_power_greater_than_offer_power(need,offer)
                        n=n+1
                
                elif temp_need-temp_offer<0 and offer.power>0 :
                    print 'D'
                    if offer.percentage_current_capacity>0.0 and reserved_for_grid is 1:
                        print 'DA'                            
                        BatteryStorage_source_need_power_less_than_offer_power(need,offer)  
                        n=n+1
#=======================Case when Grid acts as Need==============================================================#                        
             
            
            if offer.name is 'BatteryStorage':
                if offer.power>0 and offer.percentage_current_capacity>0:
                    if need.name is not 'Common_Grid' and offer.price<need.price:
                        offer.power=offer.power
                    elif need.name is 'Common_Grid':
                        continue
                else:
                    if need.name is not 'Common_Grid':
                        print 'Making battery power zero to use another source'
                        offer.power=0
                    elif need.name is 'Common_Grid':
                        reserved_for_grid=0
                        need.power=need.power*-1
                        break             
                    
#=======================Case when Grid acts as Source for Battery during high generation==============================================================#                

            if offer.name is 'Common_Grid' and offer.power>=0:
                print 'E'
                if reserved_for_grid is 1 and need.name is 'BatteryStorage' and need.percentage_current_capacity<100:
                    print 'Battery acting as load for Grid'
                    if temp_need-temp_offer>=0:
                        print 'EA'
                        BatteryStorage_load_need_power_more_than_offer_power(need,offer)
                        
                    elif  temp_need-temp_offer<0:
                        print 'EB'
                        BatteryStorage_load_need_power_less_than_offer_power(need,offer)
                    
#=======================Case when Grid acts as Source for Battery during high generation==============================================================#                
                          
                    
#=======================No power sharing if price of offer is more than need price==============================================================#                
                                                            
            elif offer.price>need.price and need.name is not 'Common_Grid':
                print 'Offered Price', offer.price,'of', offer.name,'is greater than need price',need.price, 'of', need.name
                n=n+1
#=======================No power sharing if price of offer is more than need price==============================================================#                

#=========================To move onto next need, if current need is fulfilled======================================#

            if (need.power<=0.001):
                need.power=0
                print need.name, 'power demand is satisfied now for this interval \n'
                print_needs(needs)
                print_offers(offers) 
                if need.name is 'Common_Grid':
                    reserved_for_grid=0 # resetting the grid status   
                if offer.name is 'BatteryStorage':
                    print 'Check reserve status'
                    continue  
                break
#=========================To move onto next need, if current need is fulfilled======================================#
             
             
#=========================To move to next offer to satisfy one need======================================#                        
            if (offer.power<0.001):
                offer.power=0
                print offer.name,'is delpleted \n'
                count=count+1
                offers = sort_price_ascending(offers)

                                        
            offers=sort_price_ascending(offers)
            prev_offer=offer.name
            print 'COUNT',count
            count=Removing_Zero_Power_Sources(offers,count) 
            print 'COUNT',count
                
            if count is None:count=0
            if offers[count].name is not prev_offer:
                iteration_var=iteration_var+1
                offer=offers[count]
                print 'new offer', offer.name
                n=0
                
            if offers[count].name is prev_offer:
                n=n+1
            print_needs(needs)
            print_offers(offers) 
            
#=========================To move to next offer to satisfy one need======================================#
            
    print 'End of iteration',t
    if primary_reserve_status is 1:
        print 'CHANGE'
        reserved_for_grid =1
    elif primary_reserve_status is 0:
        reserved_for_grid=0

    pv_profits.append(pv.profit)
    kwk_profits.append(kwk.profit)
    battery_profits.append(battery.profit)    
    common_grid_profits.append(common_grid.profit)
    T.append(t)
    Battery_capacity.append(battery.percentage_current_capacity)
    PV_list.append(pv.power)
    KWK_list.append(kwk.power)
    PD_list.append(pd.power)
    DSM_list.append(dsm.power)
    Common_Grid_list.append(common_grid.power)        
    printPowers(needs,offers)
    print 'Primary Reserve Status', primary_reserve_status,'Reserved for Grid', reserved_for_grid
    if t is x:break


