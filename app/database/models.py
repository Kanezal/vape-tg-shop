from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String
from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = mapped_column(BigInteger, primary_key=True, unique=True)

# Класс для заказов, список позиций определеяется в виде списка целых значений id товаров
class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id = mapped_column(BigInteger, unique=True)
    status: Mapped[str] = mapped_column(String(50))

class OrderItem(Base):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column()
    product_id: Mapped[int] = mapped_column()
    amount: Mapped[int] = mapped_column()

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)