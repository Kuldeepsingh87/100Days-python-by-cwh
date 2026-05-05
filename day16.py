#match case statements 
x = int("input(enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")

    case _ x!=50:
        print(x, "is not 50")
    case _x!=70:
        print(x,"is not 70")
    case _:
        print(x)
    
        
    