def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b): 
        raise ValueError('el tamaño de las cadenas son diferentes')
    
    e = 0
    for i in range(len(strand_a)):
        if  strand_a[i] != strand_b[i]:
            e += 1
    
    return e
