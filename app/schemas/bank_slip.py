from pydantic import BaseModel, ConfigDict


class BillingFile(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    government_id: int
    debt_id: str
    hash: str
    email: str
    name: str
    debt_amount: float
    upload_date: str
