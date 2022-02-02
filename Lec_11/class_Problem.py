import numpy as np
from scipy import interpolate

rt=interpolate.CubicSpline([0,1,2],[1,2,4])
print(rt(1.5))
