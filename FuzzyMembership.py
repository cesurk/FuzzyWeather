# Import statements
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

def membership():
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

    return wind, temperature, humidity
