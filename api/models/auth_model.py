from pydantic import BaseModel, Field, ConfigDict
from utils.data_generator import FakeData as fake


class Auth(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    username: str
    password: str
    type: str = Field(default_factory="normal")


class PublicRegistry(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str | None = Field(default_factory="public")
    username: str = Field(default_factory=fake.username)
    password: str = Field(default_factory=fake.password)
    email: str = Field(default_factory=fake.email)
    full_name: str = Field(default_factory=fake.full_name)
    accepted_terms: bool = Field(default_factory=True)


class PrivateRegistry(BaseModel):
    type: str
    existing: bool
    token: str
    username: str
    password: str
    email: str
    full_name: str
    