def getBondPrice_E(face, couponRate, yc):
   
    coupon = face * couponRate          
    pvcfsum = 0
    for t, y in enumerate(yc, start=1):  
        cf = coupon       
        df = (1 + y) ** (-t)  
        pvcf = cf * df                      
        pvcfsum = pvcf + pvcfsum                    
        if t == len(yc):                         
           pvcfsum = pvcfsum + face * df                  
        bondPrice = pvcfsum

    return bondPrice

