import numpy as np
import pandas as pd
import statsmodels.stats.api as sms

prices = np.random.randint(10, 100, 1000) #Asked 100 people to guess our product prices

print(sms.DescrStatsW(prices).tconfint_mean()) #Confidence Interval