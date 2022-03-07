from fastapi import APIRouter, Body

from application.crud.shortener_crud import get_link_by_key, delete_link, create_link
from application.structures.links import LinkSchema

router = APIRouter()


@router.get('/{key}')
def redirect_to(key):
    return get_link_by_key(key)


@router.post('/')
def create_new_link(link_data: LinkSchema = Body(...)):
    return create_link(link_data)


@router.delete('/{key}')
def delete_link(key):
    return delete_link(key)