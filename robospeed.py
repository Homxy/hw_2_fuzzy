import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

speed_error = ctrl.Antecedent(np.arange(-20, 21, 1), 'speed_error')
change_error = ctrl.Antecedent(np.arange(-20, 21, 1), 'change_error')
control_output = ctrl.Consequent(np.arange(-20, 21, 1), 'control_output')

speed_error['negative'] = fuzz.trimf(speed_error.universe, [-20, -20, 0])
speed_error['zero'] = fuzz.trimf(speed_error.universe, [-5, 0, 5])
speed_error['positive'] = fuzz.trimf(speed_error.universe, [0, 20, 20])

change_error['negative'] = fuzz.trimf(speed_error.universe, [-20, -20, 0])
change_error['zero'] = fuzz.trimf(speed_error.universe, [-5, 0, 5])
change_error['positive'] = fuzz.trimf(speed_error.universe, [0, 20, 20])

control_output['decrease'] = fuzz.trimf(control_output.universe, [-20, -20, -5])
control_output['zero'] = fuzz.trimf(control_output.universe, [-5, 0, 5])
control_output['increase'] = fuzz.trimf(control_output.universe, [5, 20, 20])

rule1 = ctrl.Rule(speed_error['negative'] & change_error['negative'], control_output['decrease'])
rule2 = ctrl.Rule(speed_error['negative'] & change_error['zero'], control_output['decrease'])
rule3 = ctrl.Rule(speed_error['negative'] & change_error['positive'], control_output['zero'])
rule4 = ctrl.Rule(speed_error['zero'] & change_error['negative'], control_output['decrease'])
rule5 = ctrl.Rule(speed_error['zero'] & change_error['zero'], control_output['zero'])
rule6 = ctrl.Rule(speed_error['zero'] & change_error['positive'], control_output['increase'])
rule7 = ctrl.Rule(speed_error['positive'] & change_error['negative'], control_output['zero'])
rule8 = ctrl.Rule(speed_error['positive'] & change_error['zero'], control_output['increase'])
rule9 = ctrl.Rule(speed_error['positive'] & change_error['positive'], control_output['increase'])

control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])


simulation = ctrl.ControlSystemSimulation(control_system)

speed_error_value = -1  
change_error_value = 0
simulation.input['speed_error'] = speed_error_value
simulation.input['change_error'] = change_error_value
simulation.compute()
control_output_value = simulation.output['control_output']
print("Control Output:", control_output_value)

speed_error.view(sim=simulation)
change_error.view(sim=simulation)
control_output.view(sim=simulation)
plt.show()



