from sanic import Blueprint
from .anime_index import index

bp_list = (index,)

anime = Blueprint.group(bp_list, url_prefix='/anime')
