from pydantic import BaseModel, StrictStr


class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr
