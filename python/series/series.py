def slices(series, length):
    
    if length > len(series) or length <= 0 :
        raise ValueError("el length es debe ser mayor ni menor que el tamaño de las series")
    
    l = []
    i = 0
    
    while True :
       if i + length <= len(series):
           l.append( series[i: (i + length) ] )
           i += 1
       else:
           break
        
    return l
