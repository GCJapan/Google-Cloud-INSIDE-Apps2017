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
    res = f.text
    return res

def main():
    print("")
    print('＝＝＝Google Cloud INSIGHT Games & Apps 2017＝＝＝')
    print("")
    print(send_message(""))

    while(True):
        try:
            input_test_word = raw_input('You: ')
        except:
            input_test_word = input('You: ')
        if input_test_word == "exit":
            sys.exit()
        print(send_message(input_test_word))

if __name__ == '__main__':
    main()

