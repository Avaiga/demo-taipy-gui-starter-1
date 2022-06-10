from taipy.gui import Gui
from math import cos, exp 
import os

page = """
#This is *Taipy* GUI 

A value: <|{decay}|>.

A slider: <br/>
<|{decay}|slider|>

My chart: 
<|{data}|chart|>
"""

def compute_data(decay):
    return [cos(i/16) * exp(-i*decay/6000) for i in range(720)]

def on_change(state, var_name, var_value):
    if var_name == 'decay':
        state.data = compute_data(var_value)

decay = 10
data = compute_data(decay) 

Gui(page=page).run(title='Taipy GUI Video 1',
    		       dark_mode=False)
