

#data.py

import requests
 
print( "Hi, I'm module data.py" )
input( "hit enter ..." )

API_KEY = "602e7b589d4da1ef52adda6224f21b23" 

def importData():
    city = input( "Enter a city weather in do you whant to know >>>  " )
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    print( "waiting for server response ..." )
    
    res = requests.get( url )
    data = res.json()

    return [ city, data ]

def dataConversion( data ):
    data_as_list = data.items()
    data_as_list = list( data.items() )
    
    return data_as_list

def dataLines(data):
    for i in data:
        print( f"{i:15} :  {data[i]}" )

city, data = importData()
