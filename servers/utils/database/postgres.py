from __future__ import with_statement
from fabric.api import *
from utils.database import DatabaseDump

class PostgresDump(DatabaseDump):
    ''' A subclass of DatabaseDump. '''
    
    name = "Postgres Dump"
    
    def run(self, *args, **kwargs):
        ''' dumps, gzips and downloads a postgres database.'''

        with cd('/tmp/'):
            cmd = 'pg_dump'

            if self.user is not None:
                cmd += ' -U %s' % self.user
            if self.hostname is not None:
                cmd += ' -h %s' % self.hostname

            self.finish_dump(cmd)
