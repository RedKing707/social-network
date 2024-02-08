from database.models import User
from database import get_db


def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Get all specific user
def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user

    else:
        return 'Такого id пользователья нету(('


# add user to db
def add_new_user_db(name, surname, phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return 'Такой номер телефона уже существует'

    else:
        new_user = User(name=name, surname=surname, phone_number=phone_number, city=city, password=password)
        db.add(new_user)
        db.commit()

        return f'Пользователь успешно зарегистрирован {new_user.user_id}'


# Login or check password
def login_user_db(phone_number, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'

    else:
        return "Ошибка данных"


# Edit user information
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id)
    if exact_user:
        if edit_info == 'name':
            exact_user.name = new_info
        elif edit_info == 'city':
            exact_user.city = new_info

        db.commit()

        return 'Данные успешно изменены'

    else:
        return 'Пользователь не найден'


# Deleting user
def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        db.delete(exact_user)
        db.commit()
        return 'Пользователь удален из базы'
    else:
        return 'Пользователь не найден'


# Add photo profile
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id)

    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()
        return 'Фото профиля добавлен'
    else:
        return 'Пользователь не найден'


def delete_profile_photo_db(user_id):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)
    if exact_user:
        exact_user.profile_photo = "None"
        db.commit()
        return 'Фото профиля удален'
    else:
        return 'Пользователь не найден'


