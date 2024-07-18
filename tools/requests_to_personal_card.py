ids = {
   'КурдикСерафимНиколаевич': '102383',
    'КрасиловДаниилЛеонидович': '102303',
    'КубатинДенисВадимович': '100000'
}

async def get_personal_info(
        student_id: int,
        name: str,
        surname: str,
        patronymic: str
) -> dict:
    """
    Идём в базу и по айдишнику возвращаем словарь со всей личной инфой.
    """
    return {
        'name': ...
    }

async def get_student_id_by_fullname(
        name: str,
        surname: str,
        patronymic: str
) -> dict:
    return 
