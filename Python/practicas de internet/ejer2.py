previous_number=0



for i in range(0, 10):
    print("Current number: ", i)
    
    
    previous_number=i-1
    
    if(previous_number<=-1):
        previous_number=0
    print("Previous number: ", previous_number )
    
    print("Sum: ", i+previous_number)
   
    
    