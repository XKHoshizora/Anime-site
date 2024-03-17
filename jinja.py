from jinja2 import PackageLoader, select_autoescape
from sanic_jinja2 import SanicJinja2

jinja = SanicJinja2(
    # loader=PackageLoader('templates', package_path='templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl'])
)
