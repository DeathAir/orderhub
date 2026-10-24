from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Order
from app.db.session import get_db
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    new_order = Order(
        order_id=order.order_id,
        amount=order.amount,
        status="created"
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order


