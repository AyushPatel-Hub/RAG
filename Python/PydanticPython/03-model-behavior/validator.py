from pydantic import BaseModel, field_validator,model_validator,computed_field

class User(BaseModel):
    username:str  

    @field_validator('username')
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("Username must be at least 4 characters")
        return v

class SignupData(BaseModel ):
    def password_match(cls,values):
        if values.password!=values.confirm_password:
            raise ValueError("Password does not match")
        return values


class Product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self)->float:
        return self.price*self.quantity 
