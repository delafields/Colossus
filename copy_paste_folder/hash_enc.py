import pandas as pd
import numpy as np

np.random.seed(314)
x = np.random.randint(low=100, high=1000, size=4)
x = np.array([hex(i) for i in x])
print(f'x: {x}')
 
df = pd.DataFrame(data=x, columns=['feature'])

def hash_enc(df, cols):
    for col in cols:
        df[f'{col}_hash_enc'] = df[col].apply(lambda x: hash(str(x)) % 5000)
    return df
 
df = freq_enc(df, ['feature'])
print(df)