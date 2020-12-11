import math
from math import pi
import numpy
import scipy.constants
import solar
from h358data import DataContainer

### TO BE COMPLETED

corridor_resistance = 0.03397409605136547

out_resistance = 0.030222194636565048

down_resistance = 0.028620336576640495

# variables
h358 = DataContainer('h358data_2015-2016.csv')
datetime = h358.get_variable('datetime')
office_CO2_concentration = h358.get_variable('office_CO2_concentration')
corridorCCO2 = h358.get_variable('corridor_CO2_concentration')
Toffice_reference = h358.get_variable('Toffice_reference')
Tcorridor = h358.get_variable('Tcorridor')
humidity_outdoor = h358.get_variable('humidity_outdoor')
nebulosity = h358.get_variable('nebulosity')
Tout = h358.get_variable('Tout')
power_stephane = h358.get_variable('power_stephane')
power_khadija = h358.get_variable('power_khadija')
power_audrey = h358.get_variable('power_audrey')
power_stagiaire = h358.get_variable('power_stagiaire')
power_block_east = h358.get_variable('power_block_east')
power_block_west = h358.get_variable('power_block_west')
window_opening = h358.get_variable('window_opening')
door_opening = h358.get_variable('door_opening')
dT_heat = h358.get_variable('dT_heat')

solar_gain = solar.SolarGain()
phi_sun=[solar_gain.get_solar_gain(pi, pi/2, dt)[1] for dt in datetime]
phi_sun = numpy.array(phi_sun, dtype=float)*0.3

## TO BE COMPLETED

occupancy = []

for i in range (len(datetime)) :
    c = 0
    if power_stephane[i]>17 :
        c+=1
    if power_khadija[i]>17 :
        c+=1
    if power_audrey[i]>17 :
        c+=1
    if power_stagiaire[i]>17 :
        c+=1
    occupancy.append(c)
    

## TO BE COMPLETED

total_electric_power = []
## TO BE COMPLETED



#office_power_gains = ...
## To BE COMPLETEDD

#static thermal model


'''def simulate(door_opening_forced: bool=None, window_opening_forced: bool=None, Tout_bias: float=0, Tcorridor_bias: float=0, office_power_gains_bias: float=0):
    office_simulated_temperature = []
    office_simulated_CO2 = []
    for k in range(len(datetime)):
        ### TO BE COMPLETED
        
    return office_simulated_temperature, office_simulated_CO2


office_simulated_temperature_ref, office_simulated_CO2_ref = simulate()
h358.add_external_variable('office_simulated_temperature', office_simulated_temperature_ref)
h358.add_external_variable('office_simulated_CO2', office_simulated_CO2_ref)

office_simulated_temperature, office_simulated_CO2 = simulate(door_opening_forced=True)
h358.add_external_variable('office_simulated_temperature_door_opening_forced', office_simulated_temperature)
h358.add_external_variable('office_simulated_CO2_door_opening_forced', office_simulated_CO2)
print('_____ door opening forced ____')
print('temperature error:', sum([abs(office_simulated_temperature_ref[k]-office_simulated_temperature[k]) for k in range(len(datetime))])/len(datetime))
print('CO2 error:', sum([abs(office_simulated_CO2_ref[k]-office_simulated_CO2[k]) for k in range(len(datetime))])/len(datetime))

office_simulated_temperature, office_simulated_CO2 = simulate(window_opening_forced=True)
h358.add_external_variable('office_simulated_temperature_window_opening_forced', office_simulated_temperature)
h358.add_external_variable('office_simulated_CO2_window_opening_forced', office_simulated_CO2)
print('_____  window opening forced ____')
print('Temperature error error:', sum([abs(office_simulated_temperature_ref[k]-office_simulated_temperature[k]) for k in range(len(datetime))])/len(datetime))
print('CO2 error:', sum([abs(office_simulated_CO2_ref[k]-office_simulated_CO2[k]) for k in range(len(datetime))])/len(datetime))

office_simulated_temperature, office_simulated_CO2 = simulate(Tout_bias=5)
h358.add_external_variable('office_simulated_temperature_Tout_bias5', office_simulated_temperature)
h358.add_external_variable('office_simulated_CO2_Tout_bias5', office_simulated_CO2)
print('_____  Tout bias ____')
print('Temperature error:', sum([abs(office_simulated_temperature_ref[k]-office_simulated_temperature[k]) for k in range(len(datetime))])/len(datetime))
print('CO2 error:', sum([abs(office_simulated_CO2_ref[k]-office_simulated_CO2[k]) for k in range(len(datetime))])/len(datetime))

office_simulated_temperature, office_simulated_CO2 = simulate(Tcorridor_bias=5)
h358.add_external_variable('office_simulated_temperature_Tcorridor_bias5', office_simulated_temperature)
h358.add_external_variable('office_simulated_CO2_Tcorridor_bias5', office_simulated_CO2)
print('_____  Tcorridor bias ____')
print('Temperature error:', sum([abs(office_simulated_temperature_ref[k]-office_simulated_temperature[k]) for k in range(len(datetime))])/len(datetime))
print('CO2 error:', sum([abs(office_simulated_CO2_ref[k]-office_simulated_CO2[k]) for k in range(len(datetime))])/len(datetime))

office_simulated_temperature, office_simulated_CO2 = simulate(office_power_gains_bias=100)
h358.add_external_variable('office_simulated_temperature_office_power_gains_bias100', office_simulated_temperature)
h358.add_external_variable('office_simulated_CO2_office_power_gains_bias100', office_simulated_CO2)
print('_____  gains bias ____')
print('Temperature error power:', sum([abs(office_simulated_temperature_ref[k]-office_simulated_temperature[k]) for k in range(len(datetime))])/len(datetime))
print('CO2 error power:', sum([abs(office_simulated_CO2_ref[k]-office_simulated_CO2[k]) for k in range(len(datetime))])/len(datetime))
h358.plot()'''
