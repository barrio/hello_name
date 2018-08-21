import os


class Config:
    SECRET_KEY = (os.environ.get('SECRET_KEY') or
                  'you-will-never-guess')
    DEBUG_TB_INTERCEPT_REDIRECTS = False

