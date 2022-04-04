class Config(object):

    SECRET_KEY = 'prakhar_test'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
