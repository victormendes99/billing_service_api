from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base


class User(Base):
    """
    @notice Represents a user in the system.
    @dev This model stores user information including name, email, and associated billing files.
    """

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(unique=True, index=True)

    billing_files: Mapped[List["BillingFile"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
