#!/usr/bin/env python
# coding: utf-8

# In[217]:

from Notes import *
#from Notes import Treblenotes_basic
#from Notes import Bassnotes_basic
#from Notes import Treblenotes_adv
#from Notes import Bassnotes_adv

def TrebleClef_basic(x,y):
    notes=Treblenotes_basic
    print("\n")
    print("------------------------------------------------------------"+notes[x+7][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+6][y])
    print("------------------------------------------------"+notes[x+5][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+4][y]+"\t\t")
    print("------------------------------------"+notes[x+3][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+2][y]+"\t\t\t")
    print("------------------------"+notes[x+1][y]+"--------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("------------"+notes[x-1][y]+"--------------------------------------------------------")
    print("\n")


def BassClef_basic(x,y):
    notes=Bassnotes_basic
    print("\n")
    print("------------------------------------------------------------"+notes[x+7][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+6][y])
    print("------------------------------------------------"+notes[x+5][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+4][y]+"\t\t")
    print("------------------------------------"+notes[x+3][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+2][y]+"\t\t\t")
    print("------------------------"+notes[x+1][y]+"--------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("------------"+notes[x-1][y]+"--------------------------------------------------------")
    print("\n")

    

     
def TrebleClef_adv(x,y):
    notes=Treblenotes_adv
    print("\n")
    print("                                                              -----"+notes[x+11][y]+"----")
    print("\t\t\t\t\t\t\t \t"+notes[x+10][y])
    print("------------------------------------------------------------"+notes[x+9][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+8][y])
    print("------------------------------------------------"+notes[x+7][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+6][y]+"\t\t")
    print("------------------------------------"+notes[x+5][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+4][y]+"\t\t\t")
    print("------------------------"+notes[x+3][y]+"--------------------------------------------")
    print("\t\t  "+notes[x+2][y]+"\t\t\t")
    print("------------"+notes[x+1][y]+"--------------------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("                  ------"+notes[x-1][y]+"-------                  ")
    print("\n")
    

    
def BassClef_adv(x,y):
    notes=Bassnotes_adv
    print("\n")
    print("                                                              -----"+notes[x+11][y]+"----")
    print("\t\t\t\t\t\t\t \t"+notes[x+10][y])
    print("------------------------------------------------------------"+notes[x+9][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+8][y])
    print("------------------------------------------------"+notes[x+7][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+6][y]+"\t\t")
    print("------------------------------------"+notes[x+5][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+4][y]+"\t\t\t")
    print("------------------------"+notes[x+3][y]+"--------------------------------------------")
    print("\t\t  "+notes[x+2][y]+"\t\t\t")
    print("------------"+notes[x+1][y]+"--------------------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("                  ------"+notes[x-1][y]+"-------                  ")
    print("\n")