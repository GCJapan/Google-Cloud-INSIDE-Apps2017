#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys

def send_message(mes):
    url = "http://35.194.191.240/"
    values = {'mes' : mes}
    headers = {'content-type': 'application/json'}
    f = requests.post(url, data=json.dumps(values), headers=headers)
    print(f.json)
    res = json.loads(json.loads(f.text))
    return res

def main():
    print("")
    print('＝＝＝Google Cloud INSIGHT Games & Apps 2017＝＝＝')
    print("")
    print(u'グーグル雲太郎: まだ未熟者ですが、よろしくお願いします ! ("exit"で終了します)。')

    while(True):
        input_test_word = input('You: ')
        if input_test_word == "exit":
            sys.exit()
        res = send_message(input_test_word)
        print(res)
        print(u"グーグル雲太郎: "+res["result"]["fulfillment"]["speech"])

if __name__ == '__main__':
    main()

