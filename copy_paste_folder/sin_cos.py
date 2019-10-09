import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rand_times(n):
    """Generate n rows of random 24-hour times (seconds past midnight)"""
    rand_seconds = np.random.randint(0, 24*60*60, n)
    return pd.DataFrame(data=dict(seconds=rand_seconds))

n_rows = 1000

df = rand_times(n_rows)

def sin_cos(df, cols):
    for col in cols:
        col_max_val = max(df[col])
        df[f'{col}_sin_enc'] = np.sin(2*np.pi * df[col]/ col_max_val) # sin transform
        df[f'{col}_cos_enc'] = np.cos(2*np.pi * df[col]/ col_max_val) # cos transform
    return df

df = sin_cos(df, ['seconds'])
print(df.head(2))

df.drop('seconds', axis=1, inplace=True)

df.sample(50).plot.scatter('seconds_sin_enc','seconds_cos_enc').set_aspect('equal')