from environs import Env

env = Env()
env.read_env()

DJANGO_SECRET_KEY = env.str('DJANGO_SECRET_KEY')
