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
    humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')

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

    bottoms(wind, temperature, humidity)

def bottoms(wind, temperature, humidity):
    # Build rules for types of bottoms
    bottom = ctrl.Consequent(np.arange(0, 10, 1), 'bottom')
    bottom['pants'] = fuzz.trimf(bottom.universe, [0, 0, 7])
    bottom['shorts'] = fuzz.trimf(bottom.universe, [3, 10, 10])

    # Rules dictating shorts or pants
    rule1 = ctrl.Rule(
        (temperature['warm'] | temperature['hot'] | temperature['very_hot'])
    , bottom['shorts'])

    rule2 = ctrl.Rule(
        (temperature['moderate'] | temperature['little_cold'] |
        temperature['cold'] | temperature['very_cold'])
    , bottom['pants'])

    rule3 = ctrl.Rule(
        (temperature['moderate'] | humidity['wet'])
    , bottom['shorts'])

    rule4 = ctrl.Rule(
        (temperature['warm'] | wind['high'])
    , bottom['pants'])

    # Pass rules to controller
    bottom_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

    # Control System to compute values
    # TO DO: Change to api inputs
    bottom_system = ctrl.ControlSystemSimulation(bottom_ctrl)
    bottom_system.input['wind'] = 3
    bottom_system.input['temperature'] = -23
    bottom_system.input['humidity'] = 20
    # Crunch the numbers
    bottom_system.compute()
    botom_value = bottom_system.output['bottom']
    print(botom_value)


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
