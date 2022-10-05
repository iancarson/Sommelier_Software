import pandas as pd
import numpy as np
#use seed value of 1492 as a base to generate a random number
#These numbers a not truly random,
#but pseudo-random, i.e. deterministic
np.random.seed(1492)
#generate one dimensional array filled with 5000 values
#array is filled with random floating point samples from
#the normal standard distribution
test_df = pd.DataFrame({ 'var1': np.random.randn(5000) })
#show the random values
print(test_df)
#draw a histogram
test_df.hist()