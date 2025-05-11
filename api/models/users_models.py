from pydantic import BaseModel


class ResponseUser(BaseModel):
    accepted_terms: bool
    big_photo: str | None
    bio: str
    color: str
    date_joined: str
    email: str
    full_name: str
    full_name_display: str
    gravatar_id: str
    id: int
    is_active: bool
    lang: str
    max_memberships_private_projects: int | None
    max_memberships_public_projects: int | None
    max_private_projects: int | None
    max_public_projects: int | None
    photo: str | None
    read_new_terms: bool
    roles: list
    theme: str
    timezone: str
    total_private_projects: int
    total_public_projects: int
    username: str
    uuid: str
