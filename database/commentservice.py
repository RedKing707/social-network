from database.models import PostComments
from database import get_db

from datetime import datetime


def add_comment_db(post_id, comment_text, user_id):
    db = next(get_db())

    new_comment = PostComments(post_id=post_id, comment_text=comment_text, user_id=user_id)

    if new_comment:
        db.add(new_comment)
        db.commit()
        return 'Комментарий успешно добавлен'
    else:
        return 'Нету такого поста'


def delete_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(PostComments).filter_by(comment_id=comment_id)

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Комментарий успешно удален'

    else:
        return 'Нету такого поста'


def edit_comment_db(comment_id, changed_text):
    db = next(get_db())

    edit_comment = db.query(PostComments).filter_by(comment_id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = changed_text
        db.commit()
        return 'Комментарий успешно изменен '
    else:
        return 'Нету такого коммента'


def get_post_comments_db(post_id):
    db = next(get_db())
    post_comments = db.query(PostComments).filter_by(post_id=post_id).all()

    if post_comments:
        return post_comments
    else:
        return 'нету'



