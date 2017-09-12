#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys

def send_message(mes):
    url = "http://35.194.191.240/"
    headers = {"Content-Type" : "application/json"}
    values = {'mes' : mes}
    json_data = json.dumps(values).encode("utf-8")
    req = urllib2.Request(url, data=json_data, headers=headers)
    f = urllib2.urlopen(req)
    res = json.loads(json.loads(f.read().decode("utf-8")))
    return res

def main():
    print("")
    print('＝＝＝Google Cloud INSIGHT Games & Apps 2017＝＝＝')
    print("")
    print(u'グーグル雲太郎: まだ未熟者ですが、よろしくお願いします ! ("exit"で終了します)。')

    while(True):
        input_test_word = raw_input('You: ')
        if input_test_word == "exit":
            sys.exit()
        res = send_message(input_test_word)
        print(u"グーグル雲太郎: "+res["result"]["fulfillment"]["speech"])

if __name__ == '__main__':
    main()

