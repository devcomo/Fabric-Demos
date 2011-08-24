
from fabric.api import settings, roles, env, run, sudo, cd
from fabric.decorators import task
from fabric import tasks
from fabric.contrib.project import rsync_project

import secrets


env.roledefs = {
  'dev': [
    'vagrant@127.0.0.1:2222'
  ],
  'prod': [
    'fabric.justinvoss.com'
  ],
}


class DemoDeployment(tasks.Task):

  name = 'deploy'

  def run(self):
    self.refresh_code()    
    run('coffee -c /srv/fabric-demo/src/js/')
    sudo('service nginx reload')    

  def refresh_code(self):
    rsync_project(
      remote_dir = '/srv/fabric-demo',
      local_dir = './',
      delete = True,
      exclude = ['*.pyc', 'fabfile.py', '.vagrant', 'Vagrantfile'],
    )


class ProductionDeployment(DemoDeployment):

  name = 'production_deploy'
  
  def refresh_code(self):
    with cd('/tmp'):
      run('git clone git://github.com/CoMoRichWebGroup/Fabric-Demos.git')
      run('rm -rf /srv/fabric-demo/*')
      run('cp -R Fabric-Demos/deploy/* /srv/fabric-demo/')
      run('rm -rf Fabric-Demos')


@task
@roles('dev')
def deploy():
  env.key_filename = '/Library/Ruby/Gems/1.8/gems/vagrant-0.8.2/keys/vagrant'
  t = DemoDeployment()
  t.run()


@task
@roles('prod')
def production_deploy():

  env.user     = secrets.username
  env.password = secrets.password

  t = ProductionDeployment()
  t.run()
