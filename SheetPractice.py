#!/usr/bin/env python
# coding: utf-8

# In[5]:


def Musicsheetlearning():

    def Check(num=2,var='Clef'):
        global variable
        variable=var

        while True:
            from IPython.display import clear_output

            try:
                global numchoice
                numchoice=int(input("Please enter your choice here : "))
                if numchoice > 0 and numchoice <= int(num):
                    clear_output()
                    break
                else:
                    print(f"Please enter your choice as integer and in between 0 and {num}")
            except:
                print(f"Please enter your choice as integer")



    print("\nPress 1 for Treble Clef Training\nPress 2 for Bass Clef Traning")
    Check(2,'Clef')
    print("Your Choice for {} is {}\n".format(variable,str(numchoice)))

    clef_choice=numchoice

    print("\nPress 1 for Beginer mode\nPress 2 for Intermediate mode\nPress 3 for Advanced mode")
    Check(3,'difficulty')
    print("Your Choice for {} is {}\n".format(variable,str(numchoice)))

    difficulty=numchoice

    if clef_choice == 1:

        if difficulty==1:

            Play_in_loop(Treblenotes_basic,TrebleClef_basic,4)

        elif difficulty==2:

            Play_in_loop(Treblenotes_basic,TrebleClef_basic,6,2)
        else:

            Play_in_loop(Treblenotes_adv,TrebleClef_adv,11,4)

    else:

        if difficulty==1:

            Play_in_loop(Bassnotes_basic,BassClef_basic,4)

        elif difficulty==2:

            Play_in_loop(Bassnotes_basic,BassClef_basic,6,2)
        else:

            Play_in_loop(Bassnotes_adv,BassClef_adv,11,4)


if __name__=='__main__':

    from Play_in_loop import *

    Musicsheetlearning()

