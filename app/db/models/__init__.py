from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .billing_file import BillingFile
from .bank_slip import BankSlip
from .user import User
