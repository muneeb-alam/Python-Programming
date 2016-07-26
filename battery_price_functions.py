def BatteryStorage_source_DOD(x):
     return (1.939E-08*(x**4) - 4.065E-06*(x**3) + 0.000326*(x**2) - 0.01141*x + 0.2219)*100
     
def BatteryStorage_discharging(x):
    return -3.551E-18*(x**2)+0.05*x+26
    
def BatteryStorage_charging(x):
    return 2.131E-19*(x**2)-0.1*x+20

import matplotlib.pyplot as plt 
    
DOD=0.0

Price=list()
Price1=list()
Price2=list()
DOD_list=list()

step_size=1

while DOD<=100.0:
    price=BatteryStorage_source_DOD(DOD)
    DOD=DOD+step_size
    DOD_list.append(DOD)
    Price.append(price)

DOD=0.0
    
while DOD<=100.0:
    price1= BatteryStorage_discharging(DOD)
    Price1.append(price1)
    DOD=DOD+step_size    
   
DOD=0.0
    
while DOD<=100.0:    
    price2=BatteryStorage_charging(DOD)
    Price2.append(price2)
    DOD=DOD+step_size    

    

y = [ Price,Price1,Price2 ]
labels=['discharging_old_data', 'discharging_updated', 'charging_updated']
colors=['r','g','b']

for i in range(len(y)):
    plt.plot(DOD_list,y[i],'o-',color=colors[i],label=labels[i])

plt.legend()
plt.show()    
    
    
 


