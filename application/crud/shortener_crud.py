from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse

from application.utils.connections import links


def get_link_by_key(key: str):
    result = links.get(key)

    if result:
        return RedirectResponse(url=result.longUrl, status_code=302)

    return "Woops!"


def create_link(link_data):

    link = links.put(jsonable_encoder(link_data))

    return link


def delete_link(key: str):
    links.delete(key)

    return "We did it!"
