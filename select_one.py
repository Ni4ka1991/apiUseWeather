
#!/usr/bin/env python3

# select_one.py

from os import system

from data import *


def chooseOne( viewList ):
    print()
    choice = input( f"Enter a ordinal number of param you want to know about {query} >>> " )
    if choice in createList( viewList ):
        choice = int(choice)
        for i in range( len( viewList ) + 1 ):
            if( choice == i ):
                print("-" * 20 )
                print( f"You choosed for {query} parameter < {viewList[i - 1][0]} >. {viewList[i - 1][0]} = {viewList[i - 1][1]}" )
    else:
        print( "ERROR!" )

def createList(some_list):
    a = []
    for i in range( 1, len(some_list) + 1 ):
        a.append( str(i) )
    return a


