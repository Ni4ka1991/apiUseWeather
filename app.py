#!/usr/bin/env python3

# app.py 
from os import system
from data import *
from paginator import *


system( "clear" )
city, data = importData()
print()

data_as_list = dataConversion( data )
dataList( 1 )
pagesNavigator()
