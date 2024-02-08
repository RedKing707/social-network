from fastapi import APIRouter
from users import LoginValidator, RegisterValidator
from database.userservice import login_user_db, add_new_user_db, get_all_users_db

user_router = APIRouter(prefix='/user', tags=['Работа с пользлователями'])


@user_router.post('/login')
async def login_user(data: LoginValidator):
    result = login_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'У нас ошибка '}


@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = add_new_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь уже имеется'}


@user_router.get('/all-users')
async def all_users():
    users = get_all_users_db()

    return users

