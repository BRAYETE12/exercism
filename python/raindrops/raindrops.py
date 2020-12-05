def convert(number):
    """

    Parameters
    ----------
    number : int
        numero  a validar.

    Returns
    -------
    resp : str
        respuesta al usuario.

    """
    
    resp = ""
    
    if number % 3 == 0 :
        resp += "Pling"
        
    if number % 5 == 0 :
        resp += "Plang"
    
    if number % 7 == 0 :
        resp += "Plong"
        
    if resp == "" :
        resp = str(number)
        
    return resp
        
    
