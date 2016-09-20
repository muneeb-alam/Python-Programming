class VirtualPowerPlant:
    
    def __init__(self,Name,ProfitsNormal,ProfitsPrimaryReserve,ProfitsGridStorage,Tax,Profit):
        self.Name=Name
        self.ProfitsNormal=ProfitsNormal
        self.ProfitsPrimaryReserve=ProfitsPrimaryReserve
        self.ProfitsGridStorage=ProfitsGridStorage
        self.Tax=Tax
        self.Profit=ProfitsNormal+ProfitsPrimaryReserve+ProfitsGridStorage-Tax
        
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
    def __init__(self,Name,Price,ExchangePriceScenario,PrimaryReserveStatus):
        self.Name=Name
        self.Price=Price
        self.ExchangePriceScenario=ExchangePriceScenario
        self.PrimaryReserveStatus=PrimaryReserveStatus

class DistributionSystemOperator:
    def __init__(self,Name,SwitchForGridFriendlyBehaviour,TimeWhenAllowedToCharge):
        self.Name=Name
        self.SwitchForGridFriendlyBehaviour=SwitchForGridFriendlyBehaviour
        self.TimeWhenAllowedToCharge=TimeWhenAllowedToCharge


#========================HouseHold Objects====================================================#
VPP=VirtualPowerPlant('VPP',1,1,1,1,0)
H1=VPP.Household('House 1',1,1,1,0)
standardConsumingDevices=H1.StandardConsumingDevices('StandardConsumingDevices',10,30) # Name,Power,Price
dSM=H1.DSM('DSM',0,28,25) # Name,Power,Price
marketBatteryStorage=H1.MarketBatteryStorage('MarketBatteryStorage',250,21,250,1,250,50,0,18,26,0,0) #Name,Power,Price,rated_capacity_in_kWh,AgeingFactor,UsableCapacityInKWh,PercentageCurrentCapacity,DOD,flag,charging_priority,ChargingPrice,disChargingPrice,Profit 
marketSolarGeneratingUnit=H1.MarketSolarGeneratingUnit('SolarGeneratingUnit',400,1,0) # Name, Power,Price 
marketCogenerationUnit=H1.MarketCogenerationUnit('MarketCogenerationUnit',0,14,0) # Name, Power,Price
feedInTariff=H1.FeedInTariff('FeedInTariff',10,0,12,0) #Name, Power,Price, FeedInPremier,draw_out_Price,Profit
commonGrid=CommonGrid('Common_Grid',-10,0) #name, power,price, feed_in_price,draw_out_price,profit
