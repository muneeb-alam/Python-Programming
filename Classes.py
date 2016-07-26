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
            def __init__(self,name,power,price,rated_capacity_in_kWh,ageing_factor,usable_capacity_in_kWh,percentage_current_capacity,DOD,flag,charging_priority,charging_price,discharging_price,profit):
                self.name=name
                self.power = power
                self.price=price
                self.rated_capacity_in_kWh=rated_capacity_in_kWh
                self.ageing_factor=ageing_factor
                self.usable_capacity_in_kWh=rated_capacity_in_kWh*ageing_factor
                self.percentage_current_capacity=percentage_current_capacity
                self.DOD=DOD
                self.flag=flag
                self.charging_priority=charging_priority
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
        class Feed_in_Load:
            def __init__(self,name,power,price):
                self.name=name
                self.power = power
                self.price=price
    
    
        class Draw_Down_Grid:
            def __init__(self,name,power,price):
                self.name=name
                self.power = power
                self.price=price
                


#========================HouseHold Objects====================================================#

H1=VPP.HouseHolds('House 1')
pd=H1.PD('PD',0,28)
dsm=H1.DSM('DSM',0,30) 
battery=H1.BatteryStorage('BatteryStorage',250,25,2500,1,2500,0,100,0,0,18,26,0) #name,power,price,rated_capacity_in_kWh,ageing_factor,usable_capacity_in_kWh,percentage_current_capacity,DOD,flag,charging_priority,charging_price,discharging_price,profit 
pv=H1.SolarGeneratingUnit('SolarGeneratingUnit',400,1,0) 
kwk=H1.KWK('KWK',0,14,0)

#========================Grid Objects=================================================#


feed_in_load=VPP.Grid.Feed_in_Load('feed_in_load',100,24) 
draw_down_grid=VPP.Grid.Draw_Down_Grid('Draw_Down_Grid',0,6)
