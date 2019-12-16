# Import statements
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

# Rule to decide shorts or pants
def bottoms(wind, temperature, humidity, w, t, h):
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
    bottom_system.input['wind'] = w
    bottom_system.input['temperature'] = t
    bottom_system.input['humidity'] = h
    # Crunch the numbers
    bottom_system.compute()
    bottom_value = bottom_system.output['bottom']
    # Return the type of bottoms to wear
    if bottom_value <= 6.5:
        return "pants"
    else:
        return "shorts"

# Rule to decide shorts or pants
def tops(wind, temperature, humidity, w, t, h):
    # Build rules for types of bottoms
    top = ctrl.Consequent(np.arange(0, 10, 1), 'top')
    top['parka'] = fuzz.trimf(top.universe, [0, 0, 3])
    top['light_jacket'] = fuzz.trimf(top.universe, [2, 4, 6])
    top['sweater'] = fuzz.trimf(top.universe, [3, 6, 8])
    top['shirt'] = fuzz.trimf(top.universe, [7, 10, 10])

    # Rules dictating shirt, sweater, light jacket, or parka
    rule1 = ctrl.Rule(
        (temperature['hot'] | temperature['very_hot'])
    , top['shirt'])

    rule2 = ctrl.Rule(
        (temperature['cold'] | temperature['very_cold'])
    , top['parka'])

    rule3 = ctrl.Rule(
        (temperature['moderate'] |
        (temperature['warm'] & wind['high']))
    , top['sweater'])

    rule4 = ctrl.Rule(
        (temperature['little_cold'] |
        (temperature['moderate'] & humidity['wet']))
    , top['light_jacket'])

    rule5 = ctrl.Rule(
        (wind['low'] & temperature['warm'])
    , top['shirt'])

    # Pass rules to controller
    top_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])

    # Control System to compute values
    # TO DO: Change to api inputs
    top_system = ctrl.ControlSystemSimulation(top_ctrl)
    top_system.input['wind'] = w
    top_system.input['temperature'] = t
    top_system.input['humidity'] = h
    # Crunch the numbers
    top_system.compute()
    top_value = top_system.output['top']
    # Return the type of top to wear
    if top_value <= 2.5:
        return "parka"
    elif top_value <= 5:
        return "light jacket"
    elif top_value <= 7.5:
        return "sweater"
    else:
        return "shirt"


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
