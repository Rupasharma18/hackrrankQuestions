def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    if a<b :
        return "Cat A"
    elif b<a :
        return  "Cat B"
    else:
        return "Mouse C"
print catAndMouse(1, 2, 3) 
print catAndMouse(1, 3, 2)
print catAndMouse(2, 5, 4)  