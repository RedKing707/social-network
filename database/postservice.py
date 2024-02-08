from database.models import PostPhoto, UserPost
from database import get_db


# Get all Posts
def get_all_posts_db():
    db = next(get_db())
    all_user_posts = db.query(UserPost).all()
    return all_user_posts


def get_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        return exact_post

    else:
        return 'Такого id поста нету(('


def add_new__post_db(user_id, post_text, publish_date):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=publish_date)
    db.add(new_post)

    return f'Успешно {new_post.post_id}'


# Edit post

def edit_post_text_db(post_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.post_text = new_text

        return 'Текст к публикации изменен'
    else:
        return 'Пост не найден'


def delete_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        db.delete(exact_post)
        db.commit()

        return 'Пост успешно удален'
    else:
        return 'Пост не найден'


# Adding likes into posts
def like_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes += 1
        db.commit()
        return 'Успешно'
    else:
        return 'Пост не найден'


# deleting like from post
def unlike_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes -= 1
        db.commit()
        return 'Успешно'
    else:
        return 'Пост не найден'


# Homework upload photo to exact post
def upload_post_photo_db(post_id, photo_path):
    db = next(get_db())
    new_photo = db.query(PostPhoto).filter_by(post_id=post_id, photo_path=photo_path)

    if new_photo:
        db.add(new_photo)
        db.commit()

        return 'Фото к публикацию добавлен'
    else:
        return 'Нету поста'


def delete_post_photo_db(post_id, photo_path):
    db = next(get_db())
    new_photo = db.query(PostPhoto).filter_by(post_id=post_id, photo_path=photo_path)

    if new_photo:
        db.delete(new_photo)
        db.commit()

        return 'Фото к публикацию удален'
    else:
        return 'Нету поста'

