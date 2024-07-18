from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Column, String, ForeignKey

from typing import Optional, Annotated

Base = declarative_base()

class PersonalCard(Base):
    __tablename__ = 'personal_cards'

    student_id: Mapped[Annotated[str, mapped_column(primary_key=True)]]
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[Optional[str]]
    faculty: Mapped[str]


class PersonalInfo(Base):
    __tablename__ = 'personal_info'

    student_id: Mapped[str] = mapped_column(ForeignKey('personal_cards.student_id'), primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[Optional[str]]
    birth_date: Mapped[str]
    citizenship: Mapped[str]
    document_id_type: Mapped[str]
    address: Mapped[str]
    snils: Mapped[Optional[str]]
    status_inside_university: Mapped[str]
    general_status: Mapped[str]