def getBondPrice_Z(face, couponRate, times, yc):

    coupon = face * couponRate
    pvcfsum = 0

    for y, t in zip(yc, times):              
        cf = coupon
        df = (1 + y) ** (-t)
        pvcf = cf * df
        pvcfsum = pvcf + pvcfsum

        if t == times[-1]:                   
            pvcfsum = pvcfsum + face * df

    bondPrice = pvcfsum
    return bondPrice


