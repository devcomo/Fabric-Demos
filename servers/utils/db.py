from fabric.api import *
from utils.database import *

@task
def backup_postgres():
    dbs = env.get('postgres_dbs', None)
    if dbs is not None:
        for db in dbs:
            pg = PostgresDump(db.get('database'), db.get('user', None),
                         db.get('hostname'))
            pg.run()
