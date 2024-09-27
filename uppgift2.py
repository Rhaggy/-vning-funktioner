import math
x1=int(input("vad är det första x värdet "))
y1=int(input("vad är det första y värdet "))
x2=int(input("vad är det andra x värdet "))
y2=int(input("vad är det andra y värdet "))
def pythagoras(x1, y1, x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"Distanen mellan punkt {(x1,y1)} och punkten {(x2,y2)} är {pythagoras(x1,y1,x2,y2):.1f}")