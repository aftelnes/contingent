from fastapi import FastAPI, Depends, Path, status
from typing import Annotated

from sqlalchemy.orm import Session

from database.db import session, engine
from database import models

models.Base.metadata.create_all(engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title='КУБ.Контингент',
    description='Первая версия роутов контингента',
    version='0.0.1',
)



@app.get('/contingent/number')
async def get_number_contingent(
        course: Annotated[int | None, Path(description='Введите номер курса', example='1')] = None,
        direction: Annotated[str | None, Path(description='Введите название направления', example='Математика')] = None,
        group: Annotated[str | None, Path(description='Введите номер группы', example='12')] = None,
        subgroup: Annotated[str | None, Path(description='Введите номер подгруппы', example='12/2')] = None,
        department: Annotated[str | None, Path(description='Введите название кафедры', example='ВМиИ')] = None,
        section: Annotated[str | None, Path(description='Введите название профиля', example='ВМиКИ')] = None,
        db: Session = Depends(get_db)
) -> list:
    pass

@app.get('/contingent/personal_cards_by_fullname')
async def get_personal_cards_by_fullname(
        surname: Annotated[str, Path(description='Введите фамилию', example='Курдик')],
        name: Annotated[str | None, Path(description='Введите имя', example='Серафим')] = None,
        patronymic: Annotated[str | None, Path(description='Введите отчество', example='Николаевич')] = None,
        db: Session = Depends(get_db)
) -> dict:
    return {
        'name': name,
        'surname': surname,
        'patronymic': patronymic,
    }

# @app.get("/contingent/fullname")
# async def get_number_contingent()