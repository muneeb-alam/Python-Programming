# To transfer power between battery and grid
# To run the code without primary reserve and rectify infinite loop problem
# Grid to provide power to the PD and DSM and then calculate the profits of the grid
# Grid to provide power to battery when power is excess

# To update the charging and discharging price of the battery

#========================Functions=================================================#

#***********************Source_BatteryStorage_Functions***********************************#

# This function gives back new price of BatteryStorage according to depth of discharge shown by variable 'x'.
def BatteryStorage_source_DOD(x):
     #return (1.939E-08*(x**4) - 4.065E-06*(x**3) + 0.000326*(x**2) - 0.01141*x + 0.2219)*100
     #return -3.551E-18*(x**2)+0.05*x+20     
     return battery.discharging_price

def BatteryStorage_source_need_power_greater_than_offer_power(need,offer):
    print 'Current Capacity:', offer.percentage_current_capacity    
    if need.power >= temp_need:
        print 'case A1'
        used_power=temp_offer      
        if need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
            need.profit=profit_calculation_grid_need(offer,need,used_power)
            print 'Common Grid Profits',need.profit
        elif need.name is 'Common_Grid' and ((offer.capacity_for_grid)-offer.percentage_current_capacity)>=discharge_factor:
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
                need.profit=profit_calculation_grid_need(offer,need,used_power)
                print 'Common Grid Profits',need.profit
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
                need.profit=profit_calculation_grid_need(offer,need,used_power)
                print 'Common Grid Profits',need.profit      
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



def BatteryStorage_source_need_power_less_than_offer_power(need,offer):
     print 'Current Capacity:', offer.percentage_current_capacity                    
     if need.power >= temp_need:
         print 'case B1'
         used_power=temp_need
         if need.name is 'Common_Grid' and offer.capacity_for_grid-offer.percentage_current_capacity<discharge_factor:
            need.profit=profit_calculation_grid_need(offer,need,used_power)
            print 'Common Grid Profits',need.profit
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
                 need.profit=profit_calculation_grid_need(offer,need,used_power)
                 print 'Common Grid Profits',need.profit 
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
                need.profit=profit_calculation_grid_need(offer,need,used_power)
                print 'Common Grid Profits',need.profit
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

#***********************Load_BatteryStorage_Functions_End***********************************#

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

#**************************pv and KHP Functions***************************************#

def pv_or_KWK_need_power_greater_than_offer_power(need,offer):
    if need.name is 'BatteryStorage' and need.percentage_current_capacity<100.0:
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
        
def pv_or_KWK_need_power_less_than_offer_power(need,offer):      
    if need.name is 'BatteryStorage' and need.percentage_current_capacity<100.0:
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

def profit_calculation(offer,need,used_power):
    if need.name is not 'Common_Grid':
        offer.profit=offer.profit+(used_power*(hours)/4*need.price-used_power*(hours)/4*offer.price)
    else:
        offer.profit=offer.profit+(-used_power*(hours)/4*need.price+used_power*(hours)/4*offer.price)        
    return offer.profit
    
def profit_calculation_battery_need(offer,need,used_power):
    need.profit=need.profit-(used_power*(hours)/4*need.price-used_power*(hours)/4*offer.price)
    return need.profit    
    
def profit_calculation_grid_need(offer,need,used_power):
    need.profit=need.profit-(-used_power*(hours)/4*need.price+used_power*(hours)/4*offer.price)
    return need.profit    
    
    
      
    
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
        
        
def status_of_BatteryStorage(offers,needs):
    index=0
    for offer in offers:
        if offer.name is 'BatteryStorage' and reserved_for_grid is not 1:
            if ((pv.power + kwk.power)>(pd.power + dsm.power)):                
                offer.price=offer.charging_price
                del(offers[index])
                print 'Need\nCharging Price:',offer.charging_price,'\n'
            else:
                index_BatteryStorage=index_of_BatteryStorage(needs)
                offer.price=BatteryStorage_source_DOD(100-offer.percentage_current_capacity)              
                del(needs[index_BatteryStorage])
                print "Offer\nDischarging Price:",offer.discharging_price,'\n'
            
        elif offer.name is 'BatteryStorage' and reserved_for_grid is 1:
                if common_grid.power>0.0:
                    del(offers[index])
                    print 'battery acting as need to support the grid'
                elif common_grid.power<0.0:
                    print 'battery acting as a source to support the grid'
                    index_BatteryStorage=index_of_BatteryStorage(needs)
                    del(needs[index_BatteryStorage])                                                                          
        else:
            index=index+1
            continue
    return
    
def status_of_Grid(offers,needs):
    index=0
    for offer in offers:
        if offer.name is 'Common_Grid':
            if offer.power<0.0:  
                index_Grid=index_of_Grid(offers)
                offer.price=offer.feed_in_price
                print offer.price
                print 'index_Grid',index_Grid
                del(offers[index_Grid])
                needs=sort_price_descending(needs) 
                offers=sort_price_ascending(offers)
                print_needs(needs)
                print_offers(offers)
                print 'Grid acting as Need with price:',offer.price
            elif offer.power>=0.0:
                index_Grid=index_of_Grid(needs)
                print index_Grid
                offer.price=offer.draw_out_price
                del(needs[index_Grid])
                needs=sort_price_descending(needs) 
                offers=sort_price_ascending(offers)
                print_offers(offers)
                print 'Grid will act as a source with price',offer.price
        else:
            index=index+1
            continue
    return 
    
    
                            
def index_of_BatteryStorage(needs):
    index=0
    for need in needs:
        if need.name is 'BatteryStorage':
            break
        else:
            index=index+1
    return index
    
def index_of_Grid(needs):
    index=0
    for need in needs:
        if need.name is 'Common_Grid':
            break
        else:
            index=index+1
    return index
        
    
def sort_power(string):
    return sorted(string, key=lambda k: k.power)

def sort_price_ascending(string):
    return sorted(string, key=lambda k: k.price)
    
def sort_price_descending(string):
    return sorted(string, key=lambda k: k.price, reverse = True)


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


discharge_factor=70

N=100.0 # no of iterations  (to be written in floating form) 
 
pv_profits=list() 
kwk_profits=list()
battery_profits=list()
common_grid_profits=list()
T=list()
Charging_status=list()

hours=4.0

#Needs
#PD_Power=[300,250,50,0]
#DSM_Power=[200,400,500,0]
#Battery_Power=[250,250,250,250]

#Offers
#PV_Power=[200,900,500,100]
#KWK_Power=[100,200,50,5]
#Common_Grid_Power=[0,0,-70,0]
#Battery_Capacity=[100,80,20,0]
#Reserve_Status=[0,1,0,0]

#Needs
PD_Power=[300,250,50,0]
DSM_Power=[200,400,500,0]
Battery_Power=[250,250,250,250]

#Offers
PV_Power=[0,900,500,100]
KWK_Power=[0,200,50,5]
Common_Grid_Power=[500,0,-75,0]
Battery_Capacity=[100,80,20,0]
Reserve_Status=[0,0,0,0]




x=0

needs=sort_price_descending([pd,dsm,battery,common_grid]) 
offers=sort_price_ascending([pv,kwk,battery,common_grid]) 
print_needs(needs)
print_offers(offers) 

reserved_for_grid=0

Battery_capacity=list()
PV_list=list()
KWK_list=list()
PD_list=list()
DSM_list=list()
Feed_in_list=list()
Draw_out_list=list()
Common_Grid_list=list()


for t in range(int((hours*60)/15)):
    print 'iteration number:',t,'\nTime',t*15,'minutes \n'
    pv.power=int(PV_Power[t])
    kwk.power=int(KWK_Power[t])
    pd.power=int(PD_Power[t])
    dsm.power=int(DSM_Power[t])
    battery.power=int(Battery_Power[t])
    battery.percentage_current_capacity=int(Battery_Capacity[t])
    if t is not 0:
        battery.percentage_current_capacity=int(Battery_capacity[t-1])  
        print 'battery capacity',battery.percentage_current_capacity
    battery.capacity_for_grid=battery.percentage_current_capacity
    primary_reserve_status=int(Reserve_Status[t])
    common_grid.power=int(Common_Grid_Power[t])
    needs=sort_price_descending([pd,dsm,battery,common_grid]) 
    offers = sort_price_ascending([pv,kwk,battery,common_grid]) 
    print "Status of Battery:",status_of_BatteryStorage(offers,needs)
    print_needs(needs)
    print_offers(offers) 
    print 'Status of Grid',status_of_Grid(offers,needs)
    needs=sort_price_descending(needs) 
    offers=sort_price_ascending(offers)
    print_needs(needs)
    print_offers(offers)
    temp_offer=None
    count=0
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
        print 'iteration_var',iteration_var
        while n < (int(N)) and need.power>0.1 and iteration_var<(int(N+20)):
            
            if (battery.power >=0 and battery.percentage_current_capacity>=0.0) or (pv.power or kwk.power or common_grid.power):
                pass
            else:
                print 'all sources are depleted'
                break
            #print count
            if count<len(offers):
                offer=offers[count]
            if need.name is 'BatteryStorage' and primary_reserve_status is 1:
                if need.percentage_current_capacity>79: 
                    print 'Primary Reserve Mode, Battery will act as reserve for grid in next interval'
                    reserved_for_grid=1
                    primary_reserve_status=0
                    break
                
            if offer.name is 'BatteryStorage' and primary_reserve_status is 1:
                print 'YES'
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
                                     
                    
            print 'Offer',offer.name, 'Offered Power',offer.power 
            if temp_offer is None and n is 0:
                temp_offer=offer.power/N
            elif n is 0 and temp_offer is not None:
                temp_offer=offer.power/N
                if (int(N)==1):
                    temp_need=need.power/1.0
            print 'temp_need',temp_need,'temp_offer',temp_offer
            
            if need.name is not 'Common_Grid':
                if temp_need-temp_offer>=0 and offer.price<=need.price and offer.power>0 and need.name is not 'Common_Grid':
                    print 'A'         
                    if offer.name is not 'BatteryStorage':
                        print 'AA'                            
                        pv_or_KWK_need_power_greater_than_offer_power(need,offer)
                            
                    elif offer.name is 'BatteryStorage' and offer.percentage_current_capacity>0.0 and temp_need>=temp_offer and reserved_for_grid is 0:
                        print 'AB'                            
                        BatteryStorage_source_need_power_greater_than_offer_power(need,offer)
               
                elif temp_need -temp_offer<0 and offer.price <= need.price and offer.power>0:
                    print 'B'                        
                    if offer.name is not 'BatteryStorage':                    
                        print 'BA'                            
                        pv_or_KWK_need_power_less_than_offer_power(need,offer)
                        
                    elif  offer.name is 'BatteryStorage' and offer.percentage_current_capacity >0.0 and temp_need<=temp_offer and reserved_for_grid is 0:       
                        print 'BB'                            
                        BatteryStorage_source_need_power_less_than_offer_power(need,offer)  
         
            elif need.name is 'Common_Grid': 
                if temp_need-temp_offer>=0 and offer.power>0 :
                    print 'C'
                    if offer.name is 'BatteryStorage' and offer.percentage_current_capacity>0.0 and reserved_for_grid is 1:
                        print 'CA'                            
                        BatteryStorage_source_need_power_greater_than_offer_power(need,offer)
                        n=n+1
                
                elif temp_need-temp_offer<=0 and offer.power>0 :
                    if offer.name is 'BatteryStorage' and offer.percentage_current_capacity>0.0 and reserved_for_grid is 1:
                        print 'CB'                            
                        BatteryStorage_source_need_power_greater_than_offer_power(need,offer)  
                        n=n+1

                
                           
            elif offer.price>need.price:
                print 'Offered Price', offer.price,'of', offer.name,'is greater than need price',need.price, 'of', need.name
                
            if (offer.power<0.001):
                offer.power=0
                print offer.name,'is delpleted \n'
                count=count+1
                offers = sort_price_ascending(offers)
                    
            if (need.power<=0.001):
                need.power=0
                print need.name, 'power demand is satisfied now for this interval \n'
                print_needs(needs)
                print_offers(offers) 
                if need.name is 'Common_Grid':
                    reserved_for_grid=0                           
                break
            
            
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
            else:
                continue
            print_needs(needs)
            print_offers(offers)   
            
            #needs=sort_price_descending([pd,dsm,battery,feed_in_load]) 
            #offers=sort_price_ascending([pv,kwk,battery,draw_down_grid]) 
            #if battery.power>0 and battery.percentage_current_capacity>0:
                #print "Status of Battery 5:"
                #status_of_BatteryStorage(offers,needs)
            
         
        
            
            
    print 'End of iteration',t

    #print 'PV profit:',pv.profit
    #print 'KWK profit:',kwk.profit
    #print 'battery_profit',battery.profit
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
    #Feed_in_list.append(feed_in_load.power)
    #Draw_out_list.append(draw_down_grid.power)          
    printPowers(needs,offers)

    if t is x:break


