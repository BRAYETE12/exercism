def decode(string):
    r = ""
    n = ""
    
    for i in range(len(string)) :
        
        if string[i].isnumeric() :            
            n += string[i]
           
        else:
            
           if n == "": 
               n = "1"
           r +=  str(string[i]) * int(n)
           n = ""
            
    return r


def encode(string):
    r = ""
    au = 1
    
    for i in range(len(string)) :
        
        if i+1 < len(string) :
            
            if string[i] == string[i+1] :
                au += 1
            else:
                if au > 1 :
                    r +=  f"{au}{string[i]}"
                else:
                     r +=  string[i]
                au = 1
        else:
            if string[i] != string[i-1] :
                r +=  string[i]
            else:
                 r +=  f"{au}{string[i]}"
    return r
            
