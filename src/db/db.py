import inspect
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from env import settings

engine = create_async_engine(settings.database_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pydantic_model: BaseModel = None
    
    id: Mapped[int] = mapped_column(primary_key=True)

    def to_read_model(self) -> BaseModel:
        """
        Convert the SQLAlchemy model instance to the specified Pydantic model.
        """
        if not self.pydantic_model:
            return

        fields = {
            name: getattr(self, name)
            for name, field in inspect.getmembers(self.__class__)
            if isinstance(field, Mapped)
        }

        return self.pydantic_model(**fields)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
