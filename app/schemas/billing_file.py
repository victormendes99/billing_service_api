from pydantic import BaseModel, ConfigDict


class BillingFile(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    hash: str
    name: str
    upload_date: str
    completed_load: bool
    last_line_processed: int
