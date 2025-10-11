from sqlmodel import Field
from typing import Optional
from datetime import datetime
from sqlmodel import TIMESTAMP
from tests.DB.models.base.base_model import BaseModel

class TempUser(BaseModel, table=True):
    registration_step_id: Optional[int] = Field(nullable=True)
    id_1c: Optional[int] = Field(nullable=True)
    id_esbd: Optional[int] = Field(nullable=True)
    manager_id: Optional[int] = Field(nullable=True)
    middleman_id: Optional[int] = Field(nullable=True)
    contract_end_date: Optional[str] = Field(nullable=True)
    contract_start_date: Optional[str] = Field(nullable=True)
    contract_date: Optional[str] = Field(nullable=True)
    contract_number: Optional[str] = Field(nullable=True)
    consent_date: Optional[datetime] = Field(
        sa_type=TIMESTAMP(timezone=True),
        nullable=True,
    )
    mobile_phone: str = Field(nullable=False)
    password: str = Field(nullable=False)
    iin: str = Field(nullable=False)
    email: Optional[str] = Field(nullable=True)
    registration_status: Optional[int] = Field(nullable=True)
    test_username: Optional[str] = Field(nullable=True)
    test_password: Optional[str] = Field(nullable=True)
    test_link: Optional[str] = Field(nullable=True)
    test_result: Optional[str] = Field(nullable=True)
    test_passed: Optional[int] = Field(nullable=True)
    test_date: Optional[str] = Field(nullable=True)
    become_agent: int = Field(nullable=False)
    natural_person_bool: int = Field(nullable=False)
    first_name: Optional[str] = Field(nullable=True)
    last_name: Optional[str] = Field(nullable=True)
    middle_name: Optional[str] = Field(nullable=True)
    first_name_eng: Optional[str] = Field(nullable=True)
    last_name_eng: Optional[str] = Field(nullable=True)
    born: Optional[str] = Field(nullable=True)
    resident: int = Field(nullable=False)
    city: Optional[str] = Field(nullable=True)
    address: Optional[str] = Field(nullable=True)
    external: int = Field(nullable=False)
    document_number: Optional[str] = Field(nullable=True)
    document_gived_by: Optional[str] = Field(nullable=True)
    document_gived_by_id: Optional[int] = Field(nullable=True)
    document_start_date: Optional[str] = Field(nullable=True)
    document_end_date: Optional[str] = Field(nullable=True)
    document_type: Optional[str] = Field(nullable=True)
    certificate_number: Optional[str] = Field(nullable=True)
    certificate_date: Optional[str] = Field(nullable=True)
    sex: Optional[str] = Field(nullable=True)