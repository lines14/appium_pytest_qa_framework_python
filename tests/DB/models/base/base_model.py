import re
from typing import Optional
from sqlalchemy import func
from typing import Union, Any
from pydantic import ConfigDict
from datetime import datetime, timezone
from sqlalchemy.orm import declared_attr
from main.utils.DB.base_DB import BaseDB
from sqlmodel import SQLModel, TIMESTAMP, Field

class BaseModel(SQLModel):
    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        arbitrary_types_allowed=True
    )
    
    id: int = Field(primary_key=True, nullable=False)

    created_at: datetime = Field(
        sa_type=TIMESTAMP(timezone=True),
        sa_column_kwargs={"server_default": func.now()},
        nullable=False,
    )

    updated_at: datetime = Field(
        sa_type=TIMESTAMP(timezone=True),
        sa_column_kwargs={
            "onupdate": lambda: datetime.now(timezone.utc), 
            "server_default": func.now()
        },
        nullable=False,
    )

    deleted_at: Optional[datetime] = Field(
        sa_type=TIMESTAMP(timezone=True),
        nullable=True,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower() + 's'

    async def create(self) -> None:
        await BaseDB().create(self)

    async def get(self, with_soft_deleted: bool = False) -> list[SQLModel]:
        return await BaseDB().get(type(self), self, with_soft_deleted)
    
    async def get_with_joined_load(
        self, 
        keys: list[str], 
        with_soft_deleted: bool = False
    ) -> list[SQLModel]:
        result = await BaseDB().get_with_joined_load(self, keys, with_soft_deleted)

        if not with_soft_deleted:
            return self.clean_soft_deleted_relations(result)
    
        return result

    async def update(self) -> list[SQLModel]:
        return await BaseDB().update(
            type(self),
            self.model_dump(exclude_unset=True),
            self.model_dump(exclude_unset=True)
        )

    async def delete(self, soft_delete: bool = True) -> None:
        await BaseDB().delete(type(self), self, soft_delete)

    @classmethod
    async def bulk_get(cls, search_by: dict, with_soft_deleted: bool = False) -> list[SQLModel]:
        return await BaseDB().get(cls, search_by, with_soft_deleted)
    
    @classmethod
    async def bulk_get_with_joined_load(
        cls, 
        search_by: dict, 
        keys: list[str], 
        with_soft_deleted: bool = False
    ) -> list[SQLModel]:
        result = await BaseDB().get_with_joined_load(cls, search_by, keys, with_soft_deleted)

        if not with_soft_deleted:
            return cls.clean_soft_deleted_relations(result)
    
        return result

    @classmethod
    async def bulk_update(cls, search_by: dict, fields_to_update: dict) -> list[SQLModel]:
        return await BaseDB().update(cls, search_by, fields_to_update)
    
    @classmethod
    async def bulk_delete(cls, search_by: dict, soft_delete: bool = True) -> None:
        await BaseDB().delete(cls, search_by, soft_delete)
    
    @classmethod
    def clean_soft_deleted_relations(cls, obj: Union[SQLModel, list[SQLModel]]):
        if isinstance(obj, list):
            return [cls.clean_soft_deleted_relations(item) 
                    for item in obj if item.deleted_at is None]

        if not isinstance(obj, SQLModel):
            return obj

        for key, value in obj.__dict__.items():
            if isinstance(value, list):
                cleaned = [val for val in value if isinstance(val, SQLModel) 
                           and getattr(val, "deleted_at", None) is None]

                for item in cleaned:
                    cls.clean_soft_deleted_relations(item)

                setattr(obj, key, cleaned)
            elif isinstance(value, SQLModel):
                if getattr(value, "deleted_at", None) is not None:
                    setattr(obj, key, None)
                else:
                    cls.clean_soft_deleted_relations(value)

        return obj
    
    @classmethod
    def nested_models_to_dict(cls, obj: Union[SQLModel, list[SQLModel], dict, Any]) -> Any:
        if isinstance(obj, list):
            return [cls.nested_models_to_dict(item) for item in obj]

        elif isinstance(obj, SQLModel):
            result = {}

            for key, value in obj.__dict__.items():
                if key.startswith("_"):
                    continue

                result[key] = cls.nested_models_to_dict(value)

            return result

        elif isinstance(obj, dict):
            return {key: cls.nested_models_to_dict(value) for key, value in obj.items()}

        else:
            return obj