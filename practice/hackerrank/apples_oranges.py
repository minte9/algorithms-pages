def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    aLands = 0
    for x in apples:
        dist = a + x
        if dist >= s and dist <= t:
            aLands += 1
        
    oLands = 0
    for y in oranges:
        dist = b + y
        if s <= dist <= t:
            oLands += 1
            
    print(aLands)
    print(oLands)


countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
