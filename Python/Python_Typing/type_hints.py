x:str="geffr"

def add_numbers(a:int,b:int,c:int)-> int:  
    return a+b+c 

# print(add_numbers(2,"3",4))

def add_anything(a,b,c):
    return a+b+c


print(add_anything(1,2,3))

def add(x: int, y: int) -> int:
    return x + y

print(add.__annotations__)