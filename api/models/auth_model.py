from pydantic import BaseModel


class Auth(BaseModel):
    username: str
    password: str
    type: str


class PublicRegistry(BaseModel):
    type: str
    username: str
    password: str
    email: str
    full_name: str
    accepted_terms: str


class PrivateRegistry(BaseModel):
    type: str
    existing: bool
    token: str
    username: str
    password: str
    email: str
    full_name: str
    