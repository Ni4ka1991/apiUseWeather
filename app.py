#!/usr/bin/env python3

# app.py 
from os import system
from data import data
from paginator import *


system( "clear" )
print()

data_as_list = dataConversion( data )
dataList( data_as_list, 1 )
navigator( data_as_list )
