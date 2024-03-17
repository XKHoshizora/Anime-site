import os


class Config:
    AUTHOR = 'Hoshizora'

    ENV = 'Base'

    DEBUG = False

    TESTING = False

    DATABASE_URI = ''

    ROOT_PATH = os.getcwd()
    STATIC_FOLDER = os.path.abspath('../static')
    TEMPLATE_FOLDER = os.path.abspath('../templates')
    UPLOAD_FOLDER = os.path.abspath('../static/uploads')


class DevelopmentConfig(Config):
    ENV = 'Development'
    DEBUG = True


class TestConfig(Config):
    ENV = 'Test'
    TESTING = True


class ProductionConfig(Config):
    ENV = 'Production'
    DATABASE_URI = ''
