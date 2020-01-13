x=100
while x>1:

    if  x % 5 == 0:
        print(str(x) + " Agile")  
    if  x % 3 == 0:
        print(str(x) + " Software") 
    if  x % 5 == 0 and  x%3==0:
        print(str(x) + " Test")   
    else:
        print x
    x=x-1
        
