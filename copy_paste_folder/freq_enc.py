import pandas as pd
import numpy as np

df = pd.DataFrame(np.array(['cat', 'cat', 'dog', 'lion', 'lion', 'lion']),
                      columns=['animal'])

def freq_enc(df, cols):
    for col in cols:
        # get variable frequencies
        frequencies = (df.groupby(col).size()) / len(df) 
        # encode frequencies
        df[f'{col}_freq_enc'] = df[col].apply(lambda x : frequencies[x]) 
    return df
 
df = freq_enc(df, ['animal'])
print(df)