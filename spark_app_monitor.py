# coding=utf-8

import json
import urllib2
import traceback
import socket
import time
import subprocess
from send_alert import send_alert, send_warning

rms = ['http://10.13.56.81:8088/ws/v1/cluster',
       'http://10.13.56.72:8088/ws/v1/cluster']

# 任务执行时间：5小时kill，2小时报警
ALERT_DELAY = 60 * 60 * 2
ALERT_DELAY_KILL = 60 * 60 * 5

ALERT_SERVICE = "SPARK_SERVICE"
ALERT_GROUP = "DIP_SPARK_APP"


def get_timeout_apps():
    timeout_apps = []
    for rm in rms:

        print rm

        try:

            json_str = urlread(
                rm + '/apps?states=RUNNING,ACCEPTED&applicationTypes=SPARK')

            if json_str is None:
                continue

            apps = json.loads(json_str)

            print apps
            if isinstance(apps, dict):
                if apps['apps']:
                    for app in apps['apps']['app']:
                        now = time.time()
                        delay = app['startedTime'] / 1000
                        if now - delay > ALERT_DELAY:
                            timeout_apps.append((delay, app['id']))
        except ValueError, e:
            print 'error:', e
    return timeout_apps


def urlread(url, timeout=1):
    print url
    for i in range(3):
        try:
            req = urllib2.Request(url)
            sockfile = urllib2.urlopen(req, timeout=timeout)

            if sockfile.getcode() != 200:
                raise urllib2.URLError((url, sockfile.getcode()))

            return sockfile.read()

        except (urllib2.URLError, socket.error) as e:
            # logger.debug( repr( e ) )
            traceback.print_exc()
            continue
    return None


def stop(app_id):
    if app_id:
        cmd = "yarn application -kill %s" % app_id
        print cmd
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        cmd = "hadoop fs -rm -r -f /user/hdfs/.sparkStaging/%s" % app_id
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
    else:
        print "%s not RUNNING" % (app_id)


timeout_apps = get_timeout_apps()

print timeout_apps

for timeout_app in timeout_apps:
    delay = timeout_app[0]
    app_id = timeout_app[1]

    if delay > ALERT_DELAY_KILL:
        stop(app_id)
        send_warning(ALERT_SERVICE, ALERT_GROUP,
                     'spark app %s execute too long,kill it' % timeout_app[1])
    else:
        send_warning(ALERT_SERVICE, ALERT_GROUP,
                     'spark app %s execute too long' % timeout_app[1])
