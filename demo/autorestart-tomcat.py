#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import datetime

res = subprocess.Popen("ps -ef | grep tomcat", stdout=subprocess.PIPE, shell=True)
tomcats = res.stdout.readlines()
counts = len(tomcats)

if counts < 4:
    dt = datetime.datetime.now()
    fp = open('/root/tomcat6.txt', 'a')
    fp.write('tomcat6 stop at %s\n' % dt.strftime('%Y-%m-%d %H:%M:%S'))
    fp.close()
    subprocess.Popen("/usr/local/tomcat6/bin/startup.sh", shell=True)
