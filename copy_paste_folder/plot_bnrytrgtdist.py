import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({'bin_1': ['T','T','T','T','T','T','T','F','F','F'],
                   'bin_2': ['Y','N','Y','N','Y','N','Y','N','Y','N'],
                   'target': [1,1,0,0,0,0,0,0,1,0]})

fig, ax = plt.subplots(1, 2, figsize=(10,5))
fig.suptitle('Binary Distribution vs. Distribution of Target Variable')

for ax, name in zip(ax.flatten(), list(df.columns)):
    sns.countplot(x=df[name], ax=ax, hue=df['target'], saturation=1)