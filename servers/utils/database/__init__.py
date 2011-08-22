from fabric.api import *
from fabric.tasks import Task
import time

class DatabaseDump(Task):
    ''' A subclass of fabric.tasks.Task, this class '''

    def __init__(self, dbname, user=None, hostname=None):
        self.dbname = dbname
        self.user = user
        self.hostname = hostname
        self.dump_time = time.strftime('%Y%m%d%H%M%S')
        self.out_name = '%s_%s.sql' % (self.dbname, self.dump_time)

    def finish_dump(self, command):
        run('%s > %s' % (command, self.out_name))
        self.gzip()
        self.download()

    def gzip(self):
        run('gzip %s' % self.out_name)
    
    def download(self):
        get('/tmp/%s.gz' % self.out_name)

# At the bottom to prevent import errors
from utils.database.postgres import PostgresDump
