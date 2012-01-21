import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOCAL = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = os.path.join(PROJECT_ROOT_PATH,'syria_wings')
