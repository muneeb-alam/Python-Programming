import xlrd
work_book=xlrd.open_workbook('Perfekter Batteriealgorithmus.xlsx')
sheet=work_book.sheet_by_index(0)
print sheet.nrows
print sheet.ncols
print sheet.cell_value(7,2)
data=list()
for row in range(sheet.nrows):
    if row>1:
        data.append(sheet.cell_value(row,25))

Price1=data[:40]
Price2=[9,15,13,14,18,13,16,13,17,19,20,19,17,12,14,19,25]
Price3=[3,2,4,1,6,7,5,8,4,9,6,10,5,15,10,16]
Price4=[1,3,2,1,4,6,8,10,50,5,3,4,5,6,7,8,9,10,11,1]
Price5=[1,5,10,20,5,1,10,20,10,40,5,26,1,27,28,20,25,45,30]
Price9=[1,4,2,8,5,1,25,9,50]
Price10=[2,10,2,5,6,1,10,1,5,6,7,8,9,11,2,3,5]
Price6=[3,2,5,4,1,2,3,18,20,19,20]
Price7=[4,9]
Price9=[0,1,2,3,4,5,6,7,8,9,10,1]
Price10=[8,9,10,8,9,8,9,10]
Price8=data[:200]
Price=Price2
Pmin=None
Pmax=None
next_Pmin=None
next_Pmax=None
index_Pmin=None
index_Pmax=None
Pmin_list=list()
Pmax_list=list()
T_charging=list()
T_discharging=list()
Delta=5
log=0
index=0
previous_Pmax=None
Profit_list=list()

def show_points_on_graph(x):
    for a,b in zip(T, x): 
        plt.text(a, b, str(b))
        
def profit_calculation(x,y,z):
    for i in range(len(x)):
        z.append(y[i]-x[i])
    return z
    
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
    
def printTimevalues(a,b):
    print a
    print b
    
def printPriceValues(a,b):
    print a
    print b

def resetPminPmax():
    a=current_price
    b=current_price
    c=None
    d=index
    e=index
    return (a,b,c,d,e)
    
def resetNextPminPmax():
    a=None
    b=None
    c=None
    d=None
    return (a,b,c,d)
    
def storingValuesinLists(a,b,c,d):
    Pmin_list.append(a)
    Pmax_list.append(b)
    T_charging.append(c)
    T_discharging.append(d)
    return (Pmin_list,Pmax_list,T_charging,T_discharging)

while index < len(Price):
    
    current_price=Price[index]
    
    if index<len(Price)-1:
        next_price=Price[index+1]
   
    print '\nindex',index
    print'current_price:',current_price
    print 'next_price',next_price
   
   
    if Pmin is None and Pmax is None:
        (Pmin,Pmax,previous_Pmax,index_Pmin,index_Pmax)=resetPminPmax() # resetting the values of Pmin and Pmax
        print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
        
    elif current_price>Pmax and (Pmax-Pmin<Delta):
        print 'updation of Pmax and its index'
        Pmax=current_price
        index_Pmax=index
        print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
             
                         
    elif current_price<Pmin and (Pmax-Pmin<Delta):
        print 'updation of Pmin and Pmax to',current_price
        (Pmin,Pmax,previous_Pmax,index_Pmin,index_Pmax)=resetPminPmax()
        print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
            
    if (Pmax-Pmin)>=Delta:
        print 'Pmax:',Pmax,'>','Pmin:',Pmin
        print 'Pmin:',Pmin,' is logged in'
        print Pmin_list
        print Pmax_list
        
        if previous_Pmax is None:
            previous_Pmax=Pmax
            index_previous_Pmax=index


        if log is 0:
            print 'log is update'
            log=1
            print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
            if index is len(Price)-1:
                print 'only for last two items if only these two verify Delta'
                (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,Pmax,index_Pmin,index_Pmax)
                print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging
                break
            index=index+1
            continue
        
        if index is len(Price)-1: #only last two items are satisfying Delta
            Pmax=max(Pmax,current_price)
            print 'only for last two items when log is 1 already'
            (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,Pmax,index_Pmin,index)
            print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging
            break
        

        if next_Pmin is None and next_Pmax is None and log is 1:
            next_Pmin=current_price
            next_Pmax=current_price
            index_next_Pmin=index
            index_next_Pmax=index
            print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
            
          
        if index<len(Price)-2:
            if Price[index+1]-Price[index]>=Delta:
                previous_Pmax=Pmax
                index_previous_Pmax=index
                print 'updation of previous Pmax and its index',previous_Pmax,'and its index to',index_previous_Pmax          
          
        if current_price>Pmax and index<len(Price)-2:
            Pmax=current_price
            index_Pmax=index
            print 'updation of Pmax to',Pmax, 'and its index to',index_Pmax

        if current_price>next_Pmax and index<len(Price)-2:
            next_Pmax=current_price
            index_next_Pmax=index
            print 'updation of next_Pmax',next_Pmax,'and its index to',index_next_Pmax 
          
        print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax                

            
        if current_price<next_Pmin and log is 1:
            print 'A'
            if (next_Pmax-next_Pmin)>=Delta:
                print 'next_Pmax-next_Pmin>=Delta'
                print index_next_Pmin,index_previous_Pmax
                if index_next_Pmin>index_previous_Pmax:
                    print 'index of next_Pmin > index of previous_Pmax'
                    if (next_Pmax-Pmin)>(next_Pmax-next_Pmin)+(previous_Pmax-Pmin):
                        (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,next_Pmax,index_Pmin,index_next_Pmax)
                        print 'AA'
                        (Pmin,Pmax,previous_Pmax,index_Pmin,index_Pmax)=resetPminPmax()
                        (next_Pmin,next_Pmax,index_next_Pmin,index_next_Pmax)=resetNextPminPmax()
                        log=0
                        index=index+1
                        print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                        print Pmin_list,'\n',Pmax,'\n',T_charging,'\n',T_discharging
                        continue      
                    else:
                        (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,previous_Pmax,index_Pmin,index_previous_Pmax)
                        (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(next_Pmin,next_Pmax,index_next_Pmin,index_next_Pmax)
                        print 'AB'
                        (Pmin,Pmax,previous_Pmax,index_Pmin,index_Pmax)=resetPminPmax()
                        (next_Pmin,next_Pmax,index_next_Pmin,index_next_Pmax)=resetNextPminPmax()
                        log=0
                        index=index+1
                        print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                        print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging
                        continue  
                else:
                    (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,next_Pmax,index_Pmin,index_next_Pmax)
                    print 'AC'
                    (Pmin,Pmax,previous_Pmax,index_Pmin,index_Pmax)=resetPminPmax()
                    (next_Pmin,next_Pmax,index_next_Pmin,index_next_Pmax)=resetNextPminPmax()
                    log=0
                    index=index+1
                    print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                    print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging
                    continue      
                    
                    
            else:
                print 'AD'
                z=max(previous_Pmax,Pmax)
                if previous_Pmax is Pmax: 
                    u=index_Pmax
                elif z is previous_Pmax:
                    print 'case a'
                    u=index_previous_Pmax
                elif z is Pmax:
                    print 'case b'
                    u=index_Pmax
                (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,max(previous_Pmax,Pmax),index_Pmin,u)
                (Pmin,Pmax,previous_Pmax,index_Pmin,index_Pmax)=resetPminPmax()
                (next_Pmin,next_Pmax,index_next_Pmin,index_next_Pmax)=resetNextPminPmax()   
                log=0
                index=index+1
                print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging
                continue

        

        if index is len(Price)-2:
            print 'last case'
            print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
            
            if next_Pmin is not None: 
                print index_previous_Pmax,index_next_Pmin
                if index_previous_Pmax<=index_next_Pmin:
                    current_price=min(current_price,next_Pmin)
                    print 'update current price',current_price
                
            if (next_price-current_price)>=Delta:
                previous_Pmax=max(previous_Pmax,Pmax)
                print 'previous Pmax',previous_Pmax
                if (next_price-Pmin)>(next_price-current_price)+(previous_Pmax-Pmin):
                    (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,next_price,index_Pmin,index+1)                     
                    print 'BA'
                    Pmin=None
                    Pmax=None
                    next_Pmin=None
                    next_Pmax=None
                    log=0
                    index=index+2
                    print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                    print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging
                    break
                
                else:
                    z=max(previous_Pmax,Pmax)
                    if previous_Pmax==Pmax: 
                        u=index_Pmax
                    elif z is previous_Pmax:
                        print 'case a'
                        u=index_previous_Pmax
                    elif z is Pmax:
                        print 'case b'
                        u=index_Pmax
                    (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,previous_Pmax,index_Pmin,u) 
                    (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(current_price,next_price,index,index+1)
                    print 'BB'
                    Pmin=None
                    Pmax=None
                    next_Pmin=None
                    next_Pmax=None
                    log=0
                    index=index+1
                    print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                    print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging  
                    break            
            
            else: 
                print 'BC'
                z=max(previous_Pmax,current_price, next_price, Pmax)
                if z is previous_Pmax:
                    u=index_previous_Pmax
                elif z is current_price:
                    u=index
                elif z is next_price:
                    u=index+1
                elif z is Pmax:
                    u=index_Pmax
                (Pmin_list,Pmax_list,T_charging,T_discharging)=storingValuesinLists(Pmin,z,index_Pmin,u) 
                next_Pmin=None
                next_Pmax=None
                log=0
                index=index+1
                print 'Pmin,Pmax,previous_Pmax,next_Pmin,next_Pmax',Pmin,previous_Pmax,Pmax,next_Pmin,next_Pmax
                print Pmin_list,'\n',Pmax_list,'\n',T_charging,'\n',T_discharging 
                break
            
    index=index+1
   

import matplotlib.pyplot as plt

Profit_list=profit_calculation(Pmin_list,Pmax_list,Profit_list)
y=[Pmin_list,Pmax_list,Profit_list]
labels=['Pmin', 'Pmax','Profit']
colors=['r','g','k']


T=list()
for i in range(len(Pmin_list)):
    T.append(i)
    
plt.figure(1)
for i in range(len(y)):
    plt.plot(T,y[i],'o-',color=colors[i],label=labels[i])

plt.legend()
plt.show()
plt.axis([min(T)-0.5,max(T)+1,min(min(y))-5,max(max(y))+5])
show_points_on_graph(Pmin_list)
show_points_on_graph(Pmax_list)
show_points_on_graph(Profit_list)
plt.legend()
plt.show()


plt.figure(3)
plt.plot(T,Pmin_list,'o-r',label='Pmin')
plt.plot(T,Pmax_list,'o-g',label='Pmax')
plt.legend()
plt.show()
plt.axis([min(T)-0.5,max(T)+1,min(min(Pmin_list,Pmax_list))-5,max(max(Pmin_list,Pmax_list))+5])
    
plt.figure(4)
plt.plot(T_charging,Pmin_list,'o-r',label='Pmin')
plt.plot(T_discharging,Pmax_list,'o-g',label='Pmax')
plt.plot(T_discharging,Profit_list,'o-k',label='Profit')
plt.legend()
plt.show()
plt.axis([min(min(T_charging,T_discharging))-0.5,max(max(T_discharging,T_charging))+1,min(min(Pmin_list,Pmax_list))-5,max(max(Pmin_list,Pmax_list))+5])

plt.figure(2)
plt.plot(T_charging,Profit_list,'o-r',label='Profit')
plt.legend()
plt.show()
plt.axis([min(min(T_charging,T_discharging))-0.5,max(max(T_discharging,T_charging))+1,min(Profit_list)-5,max(Profit_list)+5])
show_points_on_graph(Profit_list)

