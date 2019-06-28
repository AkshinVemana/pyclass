"""
title: math_variable_lab-1.py
author: Akshin Vemana
date: 6/25/2019 3:08 PM
"""

""" SWALLOW """
swallowWeight = 60  # grams
swallowCarryWeight = swallowWeight / 3
coconutWeight = 1450  # grams

swallowsPerCoconut = coconutWeight / swallowCarryWeight  # = 1450 / (60 / 3)
print(swallowsPerCoconut)

""" MACAW """
macawCarryPercentage = 1 / 3
# coconutWeight = 1450
macawWeight = 900

macawCarryWeight = macawCarryPercentage * macawWeight
macawsPerCoconut = coconutWeight / macawCarryWeight  # = 1450 / (900/3)
print(macawsPerCoconut)
