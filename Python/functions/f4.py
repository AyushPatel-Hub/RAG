import math
def circle(r):
    area= math.pi * r**2
    circumference= (2*math.pi)*r
    return round(area,2) , round(circumference,2)


a , c= circle(4)
print ("Aera" , a , "Circumfernec" , c)