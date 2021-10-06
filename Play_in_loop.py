#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from Notes             import *
from Sheetdetails      import *
from IPython.display   import clear_output
from Validation        import Key_comparision
from Random_play_sheet import Random_play_sheet

def Play_in_loop(inp_note,inp_clef,maxi,mini=1):
    
    note=inp_note
    clef=inp_clef
    
    def Read_input():
        global readinput
        readinput=input("Enter the matching keys in order here sepereated by space : ")
        for x in readinput.split(' '):
            for y in inp_note:
                if y[1]=='O' and x!='' :
                    if y[0]==x.upper():
                        y[1]=x.upper()
                        break
    Random_play_sheet(inp_note,inp_clef,maxi,mini=1)
    
    while True:
        Read_input()
        
        try:
            Key_comparision(inp_note)
            check=0
        except:
            check=1
        
        try:
            if (readinput[0].lower()=='q' or readinput.lower()=='quit' or
                readinput[0].lower()=='x' or readinput.lower()=='exit'):
                    clear_output()
                    print("\nExiting\n")
                    break
            elif check==0:
                clear_output()
                print("New Board")
                Play_in_loop(inp_note,inp_clef,maxi,mini=1)
                break
            elif check==1:
                clear_output()
                inp_clef(1,1)
                
        except:
            continue

