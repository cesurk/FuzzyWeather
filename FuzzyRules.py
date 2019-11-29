# Import statements
# import numpy as np
# import skfuzzy as fuzz
# from skfuzzy import control as ctrl

def windRule(weather):
   # Use value: weather["wind"]["speed"]
   return

def temperatureRule(weather):
   # Use value: weather["main"]["temp"]
   return

def humidityRule(weather):
   # Use value: weather["main"]["humidity"]
   return

def descriptionRule(weather):
   # Use value: weather[0]["main"]
   return


# ----- SAMPLE API RESULT AS REFERENCE -----
# {
#    "coord":{
#       "lon":-75.69,
#       "lat":45.42
#    },
#    "weather":[
#       {
#          "id":500,
#          "main":"Rain",
#          "description":"light rain",
#          "icon":"10d"
#       }
#    ],
#    "base":"stations",
#    "main":{
#       "temp":-0.18,
#       "pressure":1016,
#       "humidity":80,
#       "temp_min":-1.67,
#       "temp_max":1.67
#    },
#    "visibility":4828,
#    "wind":{
#       "speed":8.7,
#       "deg":260,
#       "gust":13.4
#    },
#    "snow":{
#       "1h":0.25
#    },
#    "clouds":{
#       "all":90
#    },
#    "dt":1573843428,
#    "sys":{
#       "type":1,
#       "id":872,
#       "country":"CA",
#       "sunrise":1573819282,
#       "sunset":1573853610
#    },
#    "timezone":-18000,
#    "id":6094817,
#    "name":"Ottawa",
#    "cod":200
# }
