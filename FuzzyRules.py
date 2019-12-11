# Import statements
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

# def ControlSystem(data):
def ControlSystem():
    # New Antecedent/Consequent objects hold universe variables
    # and membership functions
    wind = ctrl.Antecedent(np.arange(0, 25, 1), 'wind')
    temperature = ctrl.Antecedent(np.arange(-40, 40, 1), 'temperature')
    humidity = ctrl.Consequent(np.arange(0, 100, 1), 'humidity')

    # Wind membership functions, Units: Meters per second
    wind['low'] = fuzz.trimf(wind.universe, [0, 0, 7])
    wind['medium'] = fuzz.trimf(wind.universe, [0, 5, 10])
    wind['high'] = fuzz.trimf(wind.universe, [7, 15, 10000])
    # View wind membership functions
    # wind['medium'].view()

    # Temperature membership functions
    temperature['very_cold'] = fuzz.trimf(temperature.universe, [-10000, -25, -20])
    temperature['cold'] = fuzz.trimf(temperature.universe, [-25, -17.5, -10])
    temperature['little_cold']  = fuzz.trimf(temperature.universe, [-10, -5, 5])
    temperature['moderate']  = fuzz.trimf(temperature.universe, [-5, 5, 15])
    temperature['warm']  = fuzz.trimf(temperature.universe, [10, 15, 20])
    temperature['hot']  = fuzz.trimf(temperature.universe, [17, 23, 30])
    temperature['very_hot'] = fuzz.trimf(temperature.universe, [27, 35, 10000])
    # View temperature membership functions
    # temperature['moderate'].view()

    # Humidity membership functions
    humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 30])
    humidity['comfortable'] = fuzz.trimf(humidity.universe, [20, 50, 80])
    humidity['wet'] = fuzz.trimf(humidity.universe, [50, 80, 10000])
    # View temperature membership functions
    # humidity['comfortable'].view()

    bottom(wind, temperature, humidity, 3, 23, 50)

def bottom(wind, temperature, humidity, w, t, h):
    # Build rules for types of bottoms
    bottom = ctrl.Consequent(np.arange(0, 26, 1), 'bottom')
    bottom['cold'] = fuzz.trimf(bottom.universe, [0, 30, 60])
    bottom['hot'] = fuzz.trimf(bottom.universe, [40, 70, 100])

    # Rules dictating shorts
    rule1 = ctrl.Rule(
        (temperature['warm'] | temperature['hot'] | temperature['very_hot'])
    , bottom['hot'])

    rule2 = ctrl.Rule(
        humidity['comfortable'] | humidity['wet'], bottom['hot']
    )

    # Rules dictating pants
    rule3 = ctrl.Rule(
        (wind['medium'] | wind['high']), bottom['cold']
    )

    # Pass rules to controller
    bottom_ctrl = ctrl.ControlSystem([rule1, rule2])


    # bottom_system = ctrl.ControlSystemSimulation(bottom_ctrl)
    # # Pass in input
    # bottom_system.input['wind'] = w
    # bottom_system.input['temperature'] = t
    # bottom_system.input['humidity'] = h
    # # Crunch the numbers
    # bottom_system.compute()
    # print(bottom_system.output['bottom'])
    # bottom.view(sim=bottom_system)


ControlSystem()

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
