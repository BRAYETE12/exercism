def abbreviate(words):
    
    words = words.replace('-',' ')
    words = words.replace('_','')
    words = words.replace('  ',' ')
    words = words.replace('  ',' ')
    
    r =  ''.join([i[0] for i in words.split(' ')])
    
    return r.upper()
    

