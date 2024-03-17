from sanic import Sanic
from sanic.response import text, json, html, file, file_stream

from sanic_session import Session, InMemorySessionInterface
from sanic_jinja2 import SanicJinja2
from sanic_cors import CORS

from config.config import *  # 导入配置

import multiprocessing as mp
import os
import uuid

# 实例化 app
app = Sanic('app')
# # 设置 Session
session = Session(app, interface=InMemorySessionInterface())
# 设置 Jinja2
# jinja = SanicJinja2(app, session=session, enable_async=True)
# 解决跨域
CORS(app)

# 加载配置
app.config.update_config(DevelopmentConfig)

# 注册静态文件夹路径
app.static(
    '/static',
    './app/static',
    name='static'
)

# 注册蓝图
from apps.anime.anime_index import index

app.blueprint(index)


# @app.route('/')
# @jinja.template('index.html')
# async def index(request):
#     pass


@app.route('/favicon.ico')
async def favicon(request):
    print('获取 favicon.ico 文件')
    return await file('static/favicon.ico')


# 主进程开始
@app.main_process_start
def mps(app, loop):
    print('核心数：', mp.cpu_count())
    print('启动服务中...')


# 主进程结束
@app.main_process_stop
def mps(app, loop):
    print('所有服务已关闭')


# 子进程开始后
@app.after_server_start
async def ass1(app, loop):
    print(f'{os.getpid()}：服务启动')


# 子进程结束时
@app.before_server_stop
async def bss2(app, loop):
    print(f'{os.getpid()}：服务关闭')


if __name__ == '__main__':
    # 获取核心数
    workers = mp.cpu_count()

    app.run(
        host='127.0.0.1',  # 服务器IP
        port=8000,  # 服务器端口
        workers=workers,  # 核心数
        access_log=False,  # 日志处理
        debug=True  # 调试模式
    )
