from pydantic import BaseModel, Field

from utils.data_generator import FakeData as fake


class Auth(BaseModel):    
    username: str
    password: str
    type: str = Field(default="normal")


class PublicRegistry(BaseModel):
    type: str | None = Field(default="public")
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


class RegistryResponse(BaseModel):
    id: int
    username: str
    full_name: str
    full_name_display: str
    color: str
    bio: str
    lang: str
    theme: str
    timezone: str
    is_active: bool
    photo: str | None
    big_photo: str | None
    gravatar_id: str
    