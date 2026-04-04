import sys

print(sys.argv)

def calculatrice(x:float, y:float, signe:str):
    
    if (signe == '+'):
        print(x + y)
     elif (signe == '-'):
        print(x - y)
    elif (signe == '*'):
        nombre = 0
        for i in range(y):
            nombre += x
        print(nombre)

x = float(sys.argv[1])
signe = sys.argv[2] 
y = float(sys.argv[3])
calculatrice(x,y,signe)
