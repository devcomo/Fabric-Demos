from fabric.api import *
from utils import server, db
# from utils.database import PostgresDump

# env.hosts = []
# env.postgres_dbs = []

env.hosts = ['gregaker.net', ]
env.postgres_dbs = [
    {
        'database': 'gregaker',
        'user': 'gregaker',
    }
]
