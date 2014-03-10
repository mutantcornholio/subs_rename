#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import os

VIDEO_EXTS = ('.avi', '.mkv')

def ask_dialog(left_list, right_list):
    format_lenth = len(max(left_list, key=len)) + 1
    for i in range(len(right_list)):  # assuming right list is shorter
        print '{:<{}}-> {}'.format(left_list[i], format_lenth, right_list[i])
    answer = raw_input('Does this look nice? [y/n] ')
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print 'Assuming %s as "n" ' % answer


files = os.listdir('.')
files.sort()
videos = []
subs = []
new_subs = []

for i in files:
    if i.endswith(VIDEO_EXTS):
        videos.append(i)
    elif i.endswith('.srt'):
        subs.append(i)

for i in range(len(subs)):
    if len(videos) >= i+1:
        new_subs.append(os.path.splitext(videos[i])[0]+'.srt')
    else:
        break

if ask_dialog(subs, new_subs):
    for i in range(len(new_subs)):
        os.rename(subs[i], new_subs[i])
    print 'Done'
else:
    print 'Aborting'