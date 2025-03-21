import numpy as np

pull = lambda exponent, percentile = .75: lambda x: x[x >= np.percentile(x, percentile)] ** exponent
round_t2 = lambda x: round(x, 2)
shift = lambda magnitude: lambda x: x + magnitude
stretch = lambda magnitude: lambda x: x * magnitude
