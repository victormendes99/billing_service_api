from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from . import Base


class BankSlip(Base):
    """
    @notice Represents a bank slip in the system.
    @dev This model stores metadata about the bank slip, including a unique government ID, debt ID, hash, email, debt amount, and upload date.
         It also establishes a relationship with the BillingFile model.
    """

    __tablename__ = "bank_slip"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    government_id: Mapped[int] = mapped_column(unique=True)
    debt_id: Mapped[str] = mapped_column(unique=True)
    hash: Mapped[str] = mapped_column(index=True, unique=True)
    email: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(30))
    debt_amount: Mapped[float]
    upload_date: Mapped[datetime] = mapped_column(server_default=func.now())

    billing_file_id: Mapped[int] = mapped_column(ForeignKey("billing_file.id"))
    billing_file: Mapped["BillingFile"] = relationship(back_populates="bank_slips")

    def __repr__(self):
        return (
            f"<BankSlip(id={self.id}, hash={self.hash}, "
            f"name={self.name}, debt_amount={self.debt_amount})>"
        )
