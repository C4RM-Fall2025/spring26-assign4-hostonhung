def getBondPrice(y, face, couponRate, m, ppy=1):
    
    n = m * ppy          
    rate          = y / ppy          
    coupon        = face * couponRate / ppy  
    
    pvcfsum = 0                    

    for i in range(1, n + 1):   
        cf = coupon                       
        df = (1 + rate) ** (-i)          
        pvcf = cf * df                      
        pvcfsum = pvcf + pvcfsum             
        if i == n:               
            pvcfsum = pvcfsum + face * df         

    bondPrice = pvcfsum
    return bondPrice
