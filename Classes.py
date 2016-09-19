class VirtualPowerPlant:
    
    def __init__(self,Name,ProfitsNormal,ProfitsPrimaryReserve,ProfitsGridStorage,Profits):
        self.Name=Name
        self.ProfitsNormal=ProfitsNormal
        self.ProfitsPrimaryReserve=ProfitsPrimaryReserve
        self.ProfitsGridStorage=ProfitsGridStorage
        self.Profits=ProfitsNormal+ProfitsPrimaryReserve+ProfitsGridStorage
        
        class Household:  
            def __init__(self,Name,ProfitsFromPR,ProfitsFromGridSupport,BuyingPrice,Profit):
                self.Name=Name
                self.ProfitsFromPR=ProfitsFromPR
                self.ProfitsFromGridSupport=ProfitsFromGridSupport
                self.BuyingPrice=BuyingPrice
                self.Profit=ProfitsFromPR+ProfitsFromGridSupport-BuyingPrice
                
            class StandardConsumingDevices:
                def __init__(self,Name,Power,Price):
                    self.Name=Name
                    self.Power = Power
                    self.Price=Price
                
            class DSM:
                def __init__(self,Name,Power,Price,FreezerTemperature):
                    self.Name=Name
                    self.Power = Power
                    self.Price=Price
                    self.FreezerTemperature=FreezerTemperature
    
            class MarketBatteryStorage:
                def __init__(self,Name,Power,Price,rated_capacity_in_kWh,AgeingFactor,UsableCapacityInKWh,PercentageCurrentCapacity,CapacityForGrid,ChargingPrice,DischargingPrice,Profit,ParticipationinPR):
                    self.Name=Name
                    self.Power = Power
                    self.Price=Price
                    self.rated_capacity_in_kWh=rated_capacity_in_kWh
                    self.AgeingFactor=AgeingFactor
                    self.UsableCapacityInKWh=rated_capacity_in_kWh*AgeingFactor
                    self.PercentageCurrentCapacity=PercentageCurrentCapacity
                    self.CapacityForGrid=CapacityForGrid
                    self.ChargingPrice=ChargingPrice
                    self.DischargingPrice=DischargingPrice
                    self.Profit=Profit
                    self.ParticipationinPR=ParticipationinPR
                    
            class MarketSolarGeneratingUnit:
                def __init__(self,Name,Power,Price,Profit):
                    self.Name=Name
                    self.Power = Power
                    self.Price=Price
                    self.Profit=Profit
            
            class MarketCogenerationUnit:
                def __init__(self,Name,Power,Price,Profit):
                    self.Name=Name
                    self.Power=Power
                    self.Price=Price
                    self.Profit=Profit

            class FeedInTariff: 
                def __init__(self,Name,Power,Price,FeedInPremier,Profit):
                    self.Name=Name
                    self.Power=Power
                    self.Price=Price        
                    self.FeedInPremier=FeedInPremier
                    self.Profit=Profit
                    
class CommonGrid:
    def __init__(self,Name,Power,Price):
        self.Name=Name
        self.Power=Power
        self.Price=Price

class ElectricityStockExchange:
    def __init__(self,Name,ExchangePriceScenario,PrimaryReserveStatus):
        self.Name=Name
        self.ExchangePriceScenario=ExchangePriceScenario
        self.PrimaryReserveStatus=PrimaryReserveStatus

class DistributionSystemOperator:
    def __init__(self,Name,SwitchForGridFriendlyBehaviour,TimeWhenAllowedToCharge):
        self.Name=Name
        self.SwitchForGridFriendlyBehaviour=SwitchForGridFriendlyBehaviour
        self.TimeWhenAllowedToCharge=TimeWhenAllowedToCharge


#========================HouseHold Objects====================================================#
VPP=VirtualPowerPlant('VPP')
H1=VPP.Household('House 1')
StandardConsumingDevices=H1.StandardConsumingDevices('StandardConsumingDevices',10,30) # Name,Power,Price
DSM=H1.DSM('DSM',0,28) # Name,Power,Price
MarketBatteryStorage=H1.MarketBatteryStorage('MarketBatteryStorage',250,21,250,1,250,50,0,18,26,0) #Name,Power,Price,rated_capacity_in_kWh,AgeingFactor,UsableCapacityInKWh,PercentageCurrentCapacity,DOD,flag,charging_priority,ChargingPrice,disChargingPrice,Profit 
pv=H1.MarketSolarGeneratingUnit('SolarGeneratingUnit',400,1,0) # Name, Power,Price 
kwk=H1.MarketCogenerationUnit('MarketCogenerationUnit',0,14,0) # Name, Power,Price
FeedInTariff=VirtualPowerPlant.H1.FeedInTariff('FeedInTariff',-10,0,12,30,0) #Name, Power,Price, FeedInPremier,draw_out_Price,Profit
common_grid=VPP.Grid.Common_Grid('Common_Grid',-10,0,12,30,0) #name, power,price, feed_in_price,draw_out_price,profit
