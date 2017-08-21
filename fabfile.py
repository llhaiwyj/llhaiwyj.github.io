# -*- coding:utf-8 -*-

from fabric.api import *


TAR_FILE_NAME = 'ppadminweb.tar.gz'

env.user = 'root'
env.hosts = ['yuetamen.com']
env.password = 'Zc48798Zh'

# 打包文件
def pack():


    tar_files = ['dist/*']
    exclude_files = ['fabfile.py', '*.tar.gz', '.DS_Store', '.git']
    exclude_files = ['--exclude=\'%s\'' % t for t in exclude_files]

    local('rm -f %s' % TAR_FILE_NAME)
    local('tar -czvf %s %s %s' % (TAR_FILE_NAME, ' '.join(exclude_files), ' '.join(tar_files)))
    print u"在当前目录创建一个打包文件: %s" % (TAR_FILE_NAME)

def clean():
    local('rm -f %s' % TAR_FILE_NAME)

def deploy():

    pack()

    remote_temp_tar = "/tmp/%s" % TAR_FILE_NAME
    # run("rm -f %s" % remote_temp_tar)

    print u'上传 源文件 %s' % TAR_FILE_NAME
    put(TAR_FILE_NAME, remote_temp_tar)

    remote_dist_base_dir = '/opt/www/PPAdminWeb'

    run('mkdir -p %s' % remote_dist_base_dir)

    with cd(remote_dist_base_dir):
        print '解压文件到到目录: %s' % remote_dist_base_dir
        run('tar -xzvf %s' % remote_temp_tar)

    # nginx 相关配置
    nginx_file = 'deploy/ppadminweb.conf'
    remote_nginx_file = '/etc/nginx/conf.d/ppadminweb.conf'

    print u'上传 nginx 配置文件 %s' % nginx_file
    put(nginx_file, remote_nginx_file)

    run('nginx -t')
    run('nginx -s reload')

    clean()
