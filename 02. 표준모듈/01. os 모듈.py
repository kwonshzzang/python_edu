# 표준 라이브러리: os, sys, math, datetime, random

import os
import shutil

print(os.getcwd())
print(__file__)
print(os.listdir('/'))
# print(os.list(os.getcwd()))

# os.mkdir('mydir')
# os.rmdir('mydir')

# shutil.rmtree('test')
# os.remove('test.txt')

print(os.path.isdir('test'))
print(os.path.isfile('text.txt'))

print(os.path.getsize('01. os 모듈.py'))
