"""
title: math_variables-2
author: Akshin Vemana
date: 6/25/2019 3:22 PM
"""

import math
""" MACAW """
macawCarryPercentage = 1/3
coconutWeight = 1450
macawWeight = 900

macawCarryWeight = macawCarryPercentage * macawWeight
macawsPerCoconut = coconutWeight / macawCarryWeight # = 1450 / (900/3)
print(math.ceil(macawsPerCoconut))

"""
import math
carrying_weight_percentage = 1/3
coconut_weight = 1450
macaw_weight = 900
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconut_weight/macaw_limit
print(math.ceil(number_macaws))
"""
