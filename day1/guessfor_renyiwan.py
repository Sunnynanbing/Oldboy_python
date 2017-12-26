#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auther:tangnanbing

old_boy_age = 54
count = 0
while count <3:
    guess_age = int(input('age:'))
    if old_boy_age == guess_age:
        print ('ok,')
        break
    elif old_boy_age > guess_age:
        print ('think older')
    else:
        print('think smaller')
    count +=1
    if count == 3:
        countine_confirm = input('do you want to keep guessing?')
        if countine_confirm != 'n':
            count = 0
