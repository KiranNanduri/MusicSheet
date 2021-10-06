#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from Notes import *

def Key_comparision(i):

    while True:
        for x,y in i:
            if y != '':
                if x!=y:
                    raise Exception('Validation Error') 
        break