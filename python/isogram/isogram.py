def is_isogram(string):
    
    try:
        string = string.replace("-", "")
        string = string.replace(" ", "")
        string = string.lower()
        
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                if  string[i] == string[j]:
                    return False
                
        return True
    
    except:
         raise Exception("Error al validar cadena")
        
    
