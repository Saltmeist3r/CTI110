year = int(input("")) 

if (year%400 == 0):
    print("%d - leap year" %year)

elif (year%100 == 0):        
    print("%d - not a leap year" %year)  

elif (year%4 == 0):           
    print("%d - leap year" %year)

else:         
    print("%d - not a leap year" %year)