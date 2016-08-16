class VPP:
    class HouseHolds:
        def __init__(self,name):
            self.name=name
        class PD:
            def __init__(self,name,power,price):
                self.name=name
                self.power = power
                self.price=price
        class DSM:
            def __init__(self,name,power,price):
                self.name=name
                self.power = power
                self.price=price

        
        class BatteryStorage:
            def __init__(self,name,power,price,rated_capacity_in_kWh,ageing_factor,usable_capacity_in_kWh,percentage_current_capacity,capacity_for_grid,charging_price,discharging_price,profit):
                self.name=name
                self.power = power
                self.price=price
                self.rated_capacity_in_kWh=rated_capacity_in_kWh
                self.ageing_factor=ageing_factor
                self.usable_capacity_in_kWh=rated_capacity_in_kWh*ageing_factor
                self.percentage_current_capacity=percentage_current_capacity
                self.capacity_for_grid=capacity_for_grid
                self.charging_price=charging_price
                self.discharging_price=discharging_price
                self.profit=profit
               
        class SolarGeneratingUnit:
            def __init__(self,name,power,price,profit):
                self.name=name
                self.power = power
                self.price=price
                self.profit=profit

        class KWK:
            def __init__(self,name,power,price,profit):
                self.name=name
                self.power = power
                self.price=price
                self.profit=profit

    class Grid:
                
        class Common_Grid:
            def __init__(self,name,power,price,feed_in_price,draw_out_price,profit):
                self.name=name
                self.power=power
                self.price=price        
                self.feed_in_price=feed_in_price
                self.draw_out_price=draw_out_price
                self.profit=profit              
#========================HouseHold Objects====================================================#
H1=VPP.HouseHolds('House 1')
pd=H1.PD('PD',10,30) # name,power,price
dsm=H1.DSM('DSM',0,28) # name,power,price
battery=H1.BatteryStorage('BatteryStorage',250,21,250,1,250,50,0,18,26,0) #name,power,price,rated_capacity_in_kWh,ageing_factor,usable_capacity_in_kWh,percentage_current_capacity,DOD,flag,charging_priority,charging_price,discharging_price,profit 
pv=H1.SolarGeneratingUnit('SolarGeneratingUnit',400,1,0) # name, power,price 
kwk=H1.KWK('KWK',0,14,0) # name, power,price

#========================Grid Objects=================================================#

common_grid=VPP.Grid.Common_Grid('Common_Grid',-10,0,12,30,0) #name, power,price, feed_in_price,draw_out_price,profit
