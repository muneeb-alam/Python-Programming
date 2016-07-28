# How to select the status of battery at any SOC e.g at 20 % SOC
  # Battery should always serve as a source as long as their capacity is not zero and they
    # will be charged when PV is maximum or all other needs are fulfilled

# To add zero power code if all the offer powers are zero so that code does not go into loop

# To add primary reserve in the battery storage system (charging of battery upto 85 percent
# and discharging upto 15 percent)
# To update the charging and discharging price of the battery

# To make power of battery equal to rated power after each interval
# To make a class from which the data will be collected and to send the data back
# To calculate the profits of battery and PV and KWK

#========================Functions=================================================#

#***********************Source_BatteryStorage_Functions***********************************#

# This function gives back new price of BatteryStorage according to depth of discharge shown by variable 'x'.
def BatteryStorage_source_DOD(x):
     #return (1.939E-08*(x**4) - 4.065E-06*(x**3) + 0.000326*(x**2) - 0.01141*x + 0.2219)*100
     return battery.discharging_price

def BatteryStorage_source_need_power_greater_than_offer_power(need,offer):
    print 'Current Capacity:', offer.percentage_current_capacity
    offer.percentage_current_capacity=((offer.percentage_current_capacity*0.01*offer.usable_capacity_in_kWh)-(temp_need*hours/4))/offer.usable_capacity_in_kWh*100                       
    offer.DOD=100-offer.percentage_current_capacity    
    print 'Capacity after Discharge', offer.percentage_current_capacity
    print 'battery DOD', offer.DOD
    if need.power >= temp_need:
        print 'case A1'
        used_power=temp_offer
        offer.profit=profit_calculation(offer,need,used_power)
        print offer.name,'Profit:',offer.profit
        need.power=need.power-temp_offer
        offer.power=offer.power-temp_offer
        
    elif need.power < temp_need:
        print 'case A2'
        if offer.power-need.power>=0:
            print 'case A21'
            used_power=need.power
            offer.profit=profit_calculation(offer,need,used_power)
            print offer.name,'Profit:',offer.profit
            offer.power=offer.power-need.power
            need.power=0
        elif offer.power-need.power<0:
            print 'case A22'
            used_power=offer.power
            offer.profit=profit_calculation(offer,need,used_power)
            print offer.name,'Profit:',offer.profit
            need.power=need.power-offer.power
            offer.power=0
    print 'Remaining Need Power',need.power
    print 'Remaining Offer Power',offer.power
    if (offer.power is 0 or offer.DOD>=100):
        offer.flag=1
        print 'Battery peak power for this interval has been used, battery flag=',offer.flag
    offer.discharging_price=BatteryStorage_source_DOD(offer.DOD) # new price after discharge
    print 'New Discharging Price',offer.discharging_price
    return



def BatteryStorage_source_need_power_less_than_offer_power(need,offer):
     print 'Current Capacity:', offer.percentage_current_capacity                    
     offer.percentage_current_capacity=((offer.percentage_current_capacity*0.01*offer.usable_capacity_in_kWh)-(temp_need*hours/4))/offer.usable_capacity_in_kWh*100     
     print 'Capacity after Discharge', offer.percentage_current_capacity
     offer.DOD=100.0-offer.percentage_current_capacity
     print 'battery DOD', offer.DOD
     if need.power >= temp_need:
         print 'case B1'
         used_power=temp_need
         offer.profit=profit_calculation(offer,need,used_power)
         print offer.name,'Profit', offer.profit
         offer.power=offer.power-temp_need
         need.power=need.power-temp_need
         
     elif need.power < temp_need:
         print 'case B2'
         if offer.power-need.power>=0:
             print 'case B21'
             used_power=need.power
             offer.profit=profit_calculation(offer,need,used_power)
             print offer.name,'Profit=',offer.profit     
             offer.power=offer.power-need.power
             need.power=0
         elif offer.power-need.power<0:
            print 'case B22'
            used_power=offer.power
            offer.profit=profit_calculation(offer,need,used_power)
            print offer.name,'Profit=',offer.profit     
            need.power=need.power-offer.power
            offer.power=0
     print 'Remaining Need Power',need.power
     print 'Remaining Offer Power',offer.power,'\n'
     if (offer.power is 0 or offer.DOD>=100):
        offer.flag=1
        print 'Battery peak power has been used, battery flag =',offer.flag
     offer.discharging_price=BatteryStorage_source_DOD(offer.DOD) # new price after discharge
     print 'New Discharging Price',offer.discharging_price
     return

#***********************Load_BatteryStorage_Functions_End***********************************#

def BatteryStorage_load_need_power_less_than_offer_power(need,offer):
        if  need.power >= temp_need:    
            print 'case C1'
            if offer.name is not 'BatteryStorage':
                print 'case C11'
                used_power=temp_need
                offer.profit=profit_calculation(offer,need,used_power)
                need.profit=profit_calculation_battery_need(offer,need,used_power)
                print offer.name, 'Profit=',offer.profit
                print need.name,'Profit=',need.profit
            offer.power=offer.power-temp_need
            need.power=need.power-temp_need
            need.percentage_current_capacity=need.percentage_current_capacity+((temp_need*hours/4))/need.usable_capacity_in_kWh*100
            print 'need CC=', need.percentage_current_capacity
            need.DOD=100.0-need.percentage_current_capacity
            if need.percentage_current_capacity>=95 and need.percentage_current_capacity<=100:
                need.flag=2
                print 'battery is fully charged now', 'need flag=',need.flag           
            print 'Current Capacity',need.percentage_current_capacity
            print 'battery DOD',need.DOD
            return need.percentage_current_capacity
            
        elif need.power < temp_need:
            print 'case C2'
            if offer.power-need.power>=0:
                print 'case C21'
                if offer.name is not 'BatteryStprage':
                    print 'case C211'                    
                    used_power=need.power
                    offer.profit=profit_calculation(offer,need,used_power)
                    need.profit=profit_calculation_battery_need(offer,need,used_power)
                    print offer.name, 'Profit=',offer.profit
                    print need.name,'Profit=',need.profit                    
                offer.power=offer.power-need.power
                need.power=0
            elif offer.power-need.power<0:
                print 'case C22'
                if offer.name is not 'BatteryStorage':
                    used_power=offer.power
                    offer.profit=profit_calculation(offer,need,used_power)
                    need.profit=profit_calculation_battery_need(offer,need,used_power)      
                    print offer.name, 'Profit=',offer.profit
                    print need.name,'Profit=',need.profit
                need.power=need.power-offer.power
                offer.power=0
            need.percentage_current_capacity=need.percentage_current_capacity+((used_power*hours/4))/need.usable_capacity_in_kWh*100
            print 'Current Capacity=',need.percentage_current_capacity            
            need.DOD=100.0-need.percentage_current_capacity
            print 'battery DOD',need.DOD
            if need.percentage_current_capacity>=95 and need.percentage_current_capacity<=100:
                need.flag=2
                print 'battery is fully charged now', 'need flag=',need.flag            
            print 'Current Capacity',need.percentage_current_capacity
            print 'battery DOD',need.DOD
        return
        
def BatteryStorage_load_need_power_more_than_offer_power(need,offer):        
    if  need.power >= temp_need: 
        print 'case D1'
        if offer.name is not 'BatteryStorage':
            print 'case D11'
            used_power=temp_offer
            offer.profit=profit_calculation(offer,need,used_power)
            need.profit=profit_calculation_battery_need(offer,need,used_power)
            print offer.name, 'Profit=',offer.profit
            print need.name,'Profit=',need.profit
        need.power=need.power-temp_offer
        offer.power=offer.power-temp_offer
        print need.usable_capacity_in_kWh,hours/4,need.percentage_current_capacity,temp_offer,hours/4
        need.percentage_current_capacity=need.percentage_current_capacity+((temp_offer*hours/4))/need.usable_capacity_in_kWh*100
        print 'Current Capacity=',need.percentage_current_capacity    
        need.DOD=100.0-need.percentage_current_capacity
        if need.percentage_current_capacity>=95 and need.percentage_current_capacity<=100:
            need.flag=2
            print 'battery is fully charged now', 'need flag=',need.flag          
        print 'battery_load current capacity',need.percentage_current_capacity
        print 'battery_load DOD ',need.DOD,'\n'      
    elif need.power < temp_need:
        print 'case D2'
        if offer.power-need.power>=0:
            print 'case D21'
            if offer.name is not 'BatteryStorage':
                print 'case D211'                
                used_power=need.power
                offer.profit=profit_calculation(offer,need,used_power)
                need.profit=profit_calculation_battery_need(offer,need,used_power)
                print offer.name, 'Profit=',offer.profit
                print need.name,'Profit=',need.profit  
            offer.power=offer.power-need.power
            need.power=0
        elif offer.power-need.power<0:
            print 'case D22'
            if offer.name is  not 'BatteryStorage':                
                print 'case D222'
                used_power=offer.power
                offer.profit=profit_calculation(offer,need,used_power)
                need.profit=profit_calculation_battery_need(offer,need,used_power)
                print offer.name, 'Profit=',offer.profit
                print need.name,'Profit=',need.profit
            need.power=need.power-offer.power
            offer.power=0
        
        need.percentage_current_capacity=need.percentage_current_capacity+((used_power*hours/4))/need.usable_capacity_in_kWh*100
        need.DOD=100.0-need.percentage_current_capacity        
        if need.percentage_current_capacity>=100:
            need.flag=2
            print 'battery is fully charged now', 'need flag=',need.flag                         
        print 'Current Capacity',need.percentage_current_capacity
        print 'battery DOD',need.DOD        
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
                if offer.name is not'BatteryStorage':                
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
    offer.profit=offer.profit+(used_power*(hours)/4*need.price-used_power*(hours)/4*offer.price)
    return offer.profit
    
def profit_calculation_battery_need(offer,need,used_power):
    need.profit=need.profit-(used_power*(hours)/4*need.price-used_power*(hours)/4*offer.price)
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
        if offer.name is 'BatteryStorage':
            if offer.charging_priority is 1:
                offer.price=offer.charging_price
                del(offers[index])
                print 'Need\nCharging Price :',offer.charging_price,'\n12'                
            elif (offer.percentage_current_capacity<2.0 or offer.DOD>98.0) and offer.charging_priority is not 1:                
                offer.price=offer.charging_price
                del(offers[index])
                print 'Need\nCharging Price:',offer.charging_price,'\n'
            elif (offer.flag is 0 or offer.percentage_current_capacity>=2.0 or offer.DOD<=98.0) and offer.charging_priority is not 1:
                index_BatteryStorage=index_of_BatteryStorage(needs)
                offer.price=offer.discharging_price                
                del(needs[index_BatteryStorage])
                print "Offer\nDischarging Price:",offer.discharging_price,'\n'
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
            print 'Name', need.name,'Power',need.power, 'Price', need.price,'(current capacity in %)',need.percentage_current_capacity,'usbale_capacity',need.usable_capacity_in_kWh,'kWh  DOD',need.DOD
        else:
            print 'Name',need.name,'Power', need.power,'Price',need.price
    print '\n'
    
    
def print_offers(offers):
    print 'Offers:'    
    for offer in offers:
        if offer.name is 'BatteryStorage':
            print 'Name', offer.name,'Power',offer.power, 'Price', offer.price,'(current capacity in %)',offer.percentage_current_capacity,'DOD',offer.DOD,'Profit',offer.profit
        else:
            print 'Name', offer.name,'Power',offer.power, 'Price', offer.price
    print '\n'

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


needs=sort_price_descending([pd,dsm,battery,feed_in_load]) 
offers=sort_price_ascending([pv,kwk,battery,draw_down_grid]) 

N=2.0 # no of iterations  (to be written in floating form) 
 
pv_profits=list() 
kwk_profits=list()
battery_profits=list()
T=list()
Charging_status=list()

hours=1.0
#battery.charging_priority=1
primary_reserve_status=0

PV_Power=[100,0,150,0]
KWK_Power=[100,200,0,50]
PD_Power=[1000,100,100,100]
DSM_Power=[200,100,100,100]
battery.percentage_current_capacity=100.0
battery.DOD=0.0
#Battery_Power=[250,250,250,250]
#Charging_status=[0,0,0,0]
#Battery_Flag=[0,0,0,0]
Feed_in_Power=[0,0,0,0]
Feed_out_Power=[0,0,0,0]

Battery_capacity=list()
PV_list=list()
KWK_list=list()
PD_list=list()
DSM_list=list()
Feed_in_list=list()
Draw_out_list=list()



for t in range(int((hours*60)/15)):
    print 'iteration number:',t,'\nTime',t*15,'minutes'
    pv.power=int(PV_Power[t])
    pd.power=int(PD_Power[t])
    dsm.power=int(DSM_Power[t])
    battery.charging_priority=int(Charging_status[t])
    print 'battery charging status',battery.charging_priority
    #dsm.power=int(DSM_Power[t])
    kwk.power=int(KWK_Power[t])
    battery.power=int(Battery_Power[t])
    battery.flag=int(Battery_Flag[t])
    feed_in_load.power=int(Feed_in_Power[t])
    draw_down_grid.power=int(Feed_out_Power[t])
    print 'battery power', battery.power  
    needs=sort_price_descending([pd,dsm,battery,feed_in_load]) 
    offers = sort_price_ascending([pv,kwk,battery,draw_down_grid]) 
    print "Status of Battery:"
    status_of_BatteryStorage(offers,needs)
    print_needs(needs)
    print_offers(offers)
    temp_offer=None
    count=0
    for need in needs:
        temp_need=need.power/N
        temp_price=need.price/N
        print 'Need name', need.name, 'required Power',need.power 
        if need.power<=0:continue
        n=0
        iteration_var=0
        print 'iteration_var',iteration_var
        while n < (int(N)) and need.power>0.1 and iteration_var<(int(N+10)):
            if pd.power<=0 and kwk.power<=0 and draw_down_grid.power<=0:
                if battery.percentage_current_capacity<=0 or battery.power<=0:
                    print 'all sources are depleted'                    
                    break
                    
            offer=offers[count]
            if need.name is 'BatteryStorage' and primary_reserve_status is 1:
                if need.percentage_current_capacity>=80.0: 
                    n=n+1 
                    continue
                
            elif offer.name is 'BatteryStorage' and primary_reserve_status is 1:
                if offer.percentage_current_capacity<=20.0: 
                    n=n+1
                    continue
               
            print 'Offer',offer.name, 'Offered Power',offer.power 
            if temp_offer is None and n is 0:
                temp_offer=offer.power/N
            elif n is 0 and temp_offer is not None:
                temp_offer=offer.power/N
                if (int(N)==1):
                    temp_need=need.power/1.0
            print 'temp_need',temp_need,'temp_offer',temp_offer
                    
            if temp_need-temp_offer>=0 and offer.price<=need.price and offer.power>0:
                print 'A'                        
                if offer.name is not 'BatteryStorage':
                    print 'AA'                            
                    pv_or_KWK_need_power_greater_than_offer_power(need,offer)
                            
                elif offer.name is 'BatteryStorage' and offer.percentage_current_capacity>0.0 and temp_need>=temp_offer and offer.flag==0:
                    print 'AB'                            
                    BatteryStorage_source_need_power_greater_than_offer_power(need,offer)
                
                         
    
            elif temp_need -temp_offer<0 and offer.price <= need.price and offer.power>0:
                print 'B'                        
                if offer.name is not 'BatteryStorage':                    
                    print 'BA'                            
                    pv_or_KWK_need_power_less_than_offer_power(need,offer)
                        
                elif  offer.name is 'BatteryStorage' and offer.percentage_current_capacity >0.0 and temp_need<=temp_offer and offer.flag ==0:       
                    print 'BB'                            
                    BatteryStorage_source_need_power_less_than_offer_power(need,offer)                        
                
                           
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
                break
            
            offers=sort_price_ascending(offers)
            prev_offer=offer.name
            count=Removing_Zero_Power_Sources(offers,count) 
            
        
                
            if count is None:count=0
            if offers[count].name is not prev_offer:
                iteration_var=iteration_var+1
                offer=offers[count]
                n=0
                
            if offers[count].name is prev_offer:
                n=n+1
            print_needs(needs)
            print_offers(offers)    
            
            

    print 'End of iteration',t
    print 'PV profit:',pv.profit
    print 'KWK profit:',kwk.profit
    print 'battery_profit',battery.profit
    pv_profits.append(pv.profit)
    kwk_profits.append(kwk.profit)
    battery_profits.append(battery.profit)
    T.append(t)
    Battery_capacity.append(battery.percentage_current_capacity)
    PV_list.append(pv.power)
    KWK_list.append(kwk.power)
    PD_list.append(pd.power)
    DSM_list.append(dsm.power)
    Feed_in_list.append(feed_in_load.power)
    Draw_out_list.append(draw_down_grid.power)    


    if t is 3:break


print 'PV Profits',pv_profits,'\n','KWK Profits', kwk_profits,'\n','Battery Profits',battery_profits

y=[pv_profits,kwk_profits,battery_profits]

if t<3:
    PV_Power=PV_Power[:t+1]
    KWK_Power=KWK_Power[:t+1]

Z=[Battery_capacity, PV_Power,PV_list, KWK_Power,KWK_list,PD_list,DSM_list]
labels=['PV Profits', 'KWK Profits', 'Battery Profits']
colors=['r','g','b']

plt.figure(1)
for i in range(len(y)):
    plt.plot(T,y[i],'o-',color=colors[i],label=labels[i])

plt.legend()
plt.show()    
plt.axis([min(T)-0.5, max(T)+1, min(min(y))-200, max(max(y))+600])

colors1=['r','g','b','c','m','y','k']
labels1=['Battery_capacity', 'PV_Power','PV_list', 'KWK_Power','KWK_list','PD_list','DSM_list']
plt.figure(2)

for i in range(len(Z)):
    print i,T,Z[i],len(Z),Z[4]
    plt.plot(T,Z[i],'o-',color=colors1[i],label=labels1[i])
plt.legend()
plt.show()
plt.axis([min(T)-0.5, max(T)+1, min(min(Z))-200, max(max(Z))+600])

