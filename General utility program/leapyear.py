year = int(input("Enter the year: "))

if(year %4==0 and year%100!= 0 or year % 400 ==0):
    
     print("Yes, The year is a leap year")
    
else:
    print("No, The year is a leap year")
    
