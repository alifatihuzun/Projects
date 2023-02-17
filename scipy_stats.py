import scipy.stats as stats
import pandas as pd
import numpy as np

random = np.random.randint(20, 300, 20)
array = pd.DataFrame(random)

print(random)
print(stats.describe(array))