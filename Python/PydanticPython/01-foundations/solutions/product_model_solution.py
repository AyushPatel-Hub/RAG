from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:int
    in_stock:bool

data={'id':101,'name':"Iphone",'price':99000,'in_stock':True}
