from __future__ import division, print_function
from .ompacore import OMPAProblem 
from .thermocline_array import ThermoclineArrayOMPAProblem 
from .watermasspenaltyfunc import get_wm_penalty_func
from .plotting import (plot_water_mass_fractions, plot_residuals,
                       plot_thermocline_water_mass_fractions,
                       plot_thermocline_residuals,
                       build_altair_viz, build_thermocline_altair_viz)
