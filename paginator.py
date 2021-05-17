#!/usr/bin/env python3

# paginator.py



from select_one import *

import math
from os import system
from random import randint

print()
print("Hi, I'm < paginator > module" )
input( "hit enter to continue" )


USERS_PG = 4
#pages = math.ceil( len( data )/USERS_PG )

def listParam( data ):
    pages = math.ceil( len( data )/USERS_PG )
    return pages


def dataList( data, init_pg = 1):
 
 pages = listParam( data )
 
 system( "clear" )
 print()
 print( f"The list of data have {pages} pages.\n" )
 

 for i in range( USERS_PG * ( init_pg - 1 ), min( USERS_PG * init_pg, len( data ))):
     print( f"{i + 1:3} {data[i][0]:12} >> {data[i][1]}" )


 print( "-" * 54 )

 for k in range( 1, pages + 1 ):
  if( k == init_pg ):
   print( "[ %d ]"%k , end = "" )
  else:
   print( " %d "%k , end = "" )
  
 print()

 ####### PRINT USER LIST #########

def navigator( data ):

    pages = listParam( data )
    anchor = 1 # initial page 
    dataList( data, 1 ) 

    while True:
        navigator = input(\
           "\n1. Enter p to change page number.\
            \n2. Enter < / >  to go to the prev / next pages.\
            \n3. Enter x to exit.\
            \n4. Enter s to get info separately.\
            \n >>>  "\
        )
        print()
        if( navigator == "p" ):
           invite = int( input( f"Select a page from the range 1 to {pages}  >>>  " ))
           
           if( anchor <= invite and invite <= pages ):
               dataList( data, 1 )
               anchor = invite

           else:
               print( "Such page is not in the list" )
               input( "hit ENTER to continue" )

        elif( navigator == "<"):
          
          if( anchor > 1):
              anchor -= 1
              dataList( anchor )
          else:
              print( "You are already  on the first page." )
              input( "hit ENTER to continue" )

        elif( navigator == ">"):
          if( anchor < pages ):
              anchor += 1
              dataList( data, 1 )
          else:
              print( f"You are already  on the last < {pages} > page." )
              input( "hit ENTER to continue" )
      
        elif( navigator == "x"):
          print( "By, by!" )
          break
      
        elif( navigator == "s" ):
          chooseOne( data )
      
        else:
          print( "Be careful!" )
 

