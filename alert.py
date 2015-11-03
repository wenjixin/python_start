#!/usr/bin/env python26
# encoding: utf-8
import sys
import getopt
import re
from send_alert import Client

kid = "2012090416"
passwd = "VrcUe70eTvnGIm3wd4g6cLtMlvg7s7"
url_path = '/v1/alert/send'


def usage(return_code=2):
    help = """
 Usage %s --service "service" --object "object" --subject "subject" --content "test" --gmsgto "litaotest" --gmailto "litaotest"  --auto_merge "0" [options]
 options:
  --service         service
  --object          object
  --subject         subject
  --content         content

  --gmailto         contact groups (split by comma)
  --gmsgto          contact groups (split by comma)
  --auto_merge      1/0
  --help            help usage

""" % sys.argv[0]
    print help
    sys.exit(return_code)


def send_alert(service, object, subject, content, gmsgto='', gmailto='', auto_merge="1"):
    if not service or not object or not subject or not content:
        print "4 para must given:service,object,subject,content"
        sys.exit()
    elif not gmsgto and not gmailto:
        print "2 prar must at least give 1:gmsgto and gmailto"
        sys.exit()
    else:
        data = dict(
            kid=kid,
            passwd=passwd,
            url='iconnect.monitor.sina.com.cn',
            sv='DIP',
            service=service,
            object=object,
            subject=subject,
            content=content,
            html='1',
            mailto='',
            msgto='',
            ivrto='',
            gmailto=gmailto,
            gmsgto=gmsgto,
            givrto='',
            auto_merge=auto_merge,
        )
        client = Client(data['url'], 80)
        client.bind_auth(data.pop('kid'), data.pop('passwd'))
        response = client.post(url_path, data)
        if response.split(',')[1].split(':')[1] == ' 0':
            return "1"
        else:
            return response

if __name__ == "__main__":
    send_alert('www', 'test', 'subject', 'content', 'yuanbotest', 'yuanbotest')
