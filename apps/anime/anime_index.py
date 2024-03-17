import server
from sanic import Sanic, Blueprint, request
from sanic.response import html
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic_jinja2 import SanicJinja2

import os
templates_path = os.path.join(os.path.abspath(os.path.abspath(os.getcwd()+os.path.sep+'..')+os.path.sep+'..'), 'templates')

index = Blueprint('anime_index', url_prefix='/index')

app = Sanic.get_app()

# jinja2 Config
# env = Environment(
#     # loader=PackageLoader('anime_index', templates_path),
#     autoescape=select_autoescape(['html', 'xml', 'tpl']),
#     enable_async=True
# )
jinja = SanicJinja2(app)


# def template(tpl, **kwargs):
    # templates = env.get_template(tpl)
    # return html(templates.render(kwargs))


@index.route('/')
@jinja.template('index.html')
async def index(request):
    pass
    # return template('index.html')
