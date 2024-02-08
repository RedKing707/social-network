from fastapi import APIRouter
from database.postservice import (get_all_posts_db, get_exact_post_db, add_new__post_db, unlike_post_db,
                                  upload_post_photo_db, edit_post_text_db, like_post_db, delete_post_db,
                                  delete_post_photo_db)
from posts import PublicPostValidator, EditPostValidator

posts_router = APIRouter(prefix='/posts', tags=['Работа с постами'])


@posts_router.post('/public-post')
async def public_post(data: PublicPostValidator):
    result = add_new__post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка!'}


@posts_router.delete('/delete-post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден'}


@posts_router.get('/get-all-posts')
async def get_all_posts():

    result = get_all_posts_db()
    return {'message': result}
