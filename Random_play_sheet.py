#!/usr/bin/env python
# coding: utf-8

# In[1]:

from Notes import *
from Sheetdetails import *

def Random_play_sheet(inp_note,inp_clef,maxi,mini=1):

    from random import shuffle
    
    note=inp_note
    clef=inp_clef
    
    if maxi >= 9:
        x=13
    else:
        x=9
    
    rand=list(range(x))

    for i in range(x):
        note[i][1]=''

    shuffle(rand)

    while True :
        if rand[0] == 0 or rand[0] >= maxi or rand[0] < mini :
            shuffle(rand)
        else:
            break

    cnt = rand[0]

    while cnt>=0:
        note[rand[cnt]][1]='O'
        cnt=cnt-1

    inp_clef(1,1)