from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from . import Base


class BillingFile(Base):
    """
    @notice Represents a billing file uploaded to the system.
    @dev This model stores metadata about the billing file, including its unique hash, name, upload date, completion status, and the last line processed.
         It also establishes relationships with the User and BankSlip models.
    """

    __tablename__ = "billing_file"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    hash: Mapped[str] = mapped_column(index=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    upload_date: Mapped[datetime] = mapped_column(server_default=func.now())
    completed_load: Mapped[bool] = mapped_column(default=False)
    last_line_processed: Mapped[int] = mapped_column(default=1)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="billing_files")
    bank_slips: Mapped[List["BankSlip"]] = relationship(back_populates="billing_file")

    def __repr__(self):
        return f"<BillingFile(id={self.id}, hash={self.hash}, name={self.name}, upload_date={self.upload_date})>"
