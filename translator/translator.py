#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mtranslate import translate


def main():
    #sentence = raw_input("Please provide sentence to be translated : ")
    sentence = 'Bonjour comment allez vous?'
    print(translate(sentence))
 
if __name__ == '__main__':
    main()
