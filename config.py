import logging
import os
import sys

FORMAT = '%(asctime)s - (%(name)s) - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)

logger.handlers = [handler]


def env():
    return os.environ.get('ENV', 'dev')


def is_staging():
    return env() == 'staging'


def is_dev():
    return env() == 'dev'


def is_production():
    return env() == 'production'


for key, var in os.environ.items():
    locals()[key] = var
