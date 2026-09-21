from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None     #this is nested model in the same model

Comment.model_rebuild() #this is forward refrencing   


address=Address(
    street="123 Jankipuram",
    city="Lucknow",
    postal_code="226031"
)

user=User(
    id=1,
    name="Ayush",
    address=address
)

comment=Comment(
    id=1,
    content="This is Ayush",
    replies=[
        Comment(id=2,content="replied"),
        Comment(id=3,content="replied 2")
    ]
)