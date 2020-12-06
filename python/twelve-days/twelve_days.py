def recite(start_verse, end_verse):
    
    days = [ "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth" ];
   
    strs = [ "a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ",        
            "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "
           ]
    

    rt = []
    
    for x in range( start_verse-1, end_verse):
        r =  f"On the {days[x]} day of Christmas my true love gave to me: "
        for i in range( x, -1, -1 ):
            if x >= 1 and i == 0 :
                 r = r +"and "+ strs[i]
            else:
                 r = r + strs[i]
        rt.append( r )
    
    return rt