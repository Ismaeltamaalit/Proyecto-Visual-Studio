def mult_or_sum(num, num2):
    product=num1*num2
    
    if product <= 1000:
        return product
    else:
        return num1+num2
    
    result=mult_or_sum(20,30)
    print(result)
    
    result=mult_or_sum(40,30)
    print(result)