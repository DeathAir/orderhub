from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column


from app.db.session import Base

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    order_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow,
                                                 onupdate=datetime.utcnow)

