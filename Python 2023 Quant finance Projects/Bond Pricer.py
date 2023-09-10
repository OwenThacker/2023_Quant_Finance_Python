def Price_of_bond(years, Coup_int, Yield_maturity, Face_value):
    
    AI = Face_value * Coup_int * 0.01
    PB = 0
    for i in range(years):
        PB += AI / ((1 + Yield_maturity * 0.01) ** (i + 1))
        
    PB += Face_value / ((1 + Yield_maturity * 0.01) ** years)
    
    return PB

years = 5
Coup_int = 7
Yield_maturity = 8.5
Face_value = 1000
print(Price_of_bond(5, 7, 8.5, 1000))
