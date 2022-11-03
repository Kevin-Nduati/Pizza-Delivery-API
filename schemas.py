from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'email': 'johndoe@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }



class Settings(BaseModel):
    authjwt_secret_key: str= '4efdefc36a15b95ab6f469473c68b55c3bfdd14618ecb0307be12b29d9f6b8c2'


class LoginMode(BaseModel):
    username: str
    password: str
    