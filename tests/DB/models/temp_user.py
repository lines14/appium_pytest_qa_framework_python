from sqlmodel import Field
from typing import Optional
from datetime import datetime
from sqlmodel import TIMESTAMP
from models.base.base_model import BaseModel

class TempUser(BaseModel, table=True):
    registration_step_id: int = Field(nullable=True)
    id_1c: int = Field(nullable=True)
    id_esbd: int = Field(nullable=True)
    manager_id: int = Field(nullable=True)
    middleman_id: int = Field(nullable=True)
    contract_end_date: str = Field(nullable=True)
    contract_start_date: str = Field(nullable=True)
    contract_date: str = Field(nullable=True)
    contract_number: str = Field(nullable=True)
    consent_date: Optional[datetime] = Field(
        sa_type=TIMESTAMP(timezone=True),
        nullable=True,
    )
    mobile_phone: str = Field(nullable=False)
    password: str = Field(nullable=False)
    iin: str = Field(nullable=False)
    email: str = Field(nullable=True)
    registration_status: int = Field(nullable=True)
    test_username: str = Field(nullable=True)
    test_password: str = Field(nullable=True)
    test_link: str = Field(nullable=True)
    test_result: str = Field(nullable=True)
    test_passed: int = Field(nullable=True)
    test_date: str = Field(nullable=True)
    become_agent: int = Field(nullable=False)
    natural_person_bool: int = Field(nullable=False)
    first_name: str = Field(nullable=True)
    last_name: str = Field(nullable=True)
    middle_name: str = Field(nullable=True)
    first_name_eng: str = Field(nullable=True)
    last_name_eng: str = Field(nullable=True)
    born: str = Field(nullable=True)
    resident: int = Field(nullable=False)
    city: str = Field(nullable=True)
    address: str = Field(nullable=True)
    external: int = Field(nullable=False)
    document_number: str = Field(nullable=True)
    document_gived_by: str = Field(nullable=True)
    document_gived_by_id: int = Field(nullable=True)
    document_start_date: str = Field(nullable=True)
    document_end_date: str = Field(nullable=True)
    document_type: str = Field(nullable=True)
    certificate_number: str = Field(nullable=True)
    certificate_date: str = Field(nullable=True)
    sex: str = Field(nullable=True)