def FizzBuzz(start, finish):
    outlist = []

    for x in range(start, finish + 1):   
        if x % 15 == 0:                  
            outlist.append("fizzbuzz")
        elif x % 3 == 0:                 
            outlist.append("fizz")
        elif x % 5 == 0:                 
            outlist.append("buzz")
        else:                           
            outlist.append(str(x))      

    return outlist


