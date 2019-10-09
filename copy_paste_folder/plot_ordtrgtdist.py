

df = pd.DataFrame({'Eastwood': ['Good','Bad','Ugly','Good','Bad','Ugly','Good','Bad','Ugly','Good'],
                   'Lil_Jon': ['WHAT','WHAT','WHAT','WHAT','YEAH','YEAH','YEAH','OK','OK','OK'],
                   'target': [1,1,0,0,0,0,0,0,1,0]})
print(df)

fig, ax = plt.subplots(1, 2, figsize=(10,5))
fig.suptitle('Distribution of Target Variable Ratio = 1 \n (lowest → highest ratio)')

ordinal_ordering = {}

for ax, name in zip(ax.flatten(), list(df.columns)):
    # calculate the ratio of target counts
    ct = pd.crosstab(df[name], df['target']).apply(lambda r: r/r.sum(), axis = 1)
    # unstack the cross-tabulated df
    stacked = ct.stack().reset_index().rename(columns = {0: 'ratio'}) 
    # sort by target ratio
    stacked = stacked.sort_values(['target', 'ratio'], ascending = [False, True]) 
    sns.barplot(x = stacked[name], y = stacked['ratio'], ax = ax, hue = stacked['target'])
    
    # create mapping for encoding
    ordinal_ordering[name] = stacked[name].unique()

print(ordinal_ordering)