import pandas as pd

df = pd.DataFrame({"a": [10, 20, 30], 
                   "b": [20, 30, 40]})
print(df)

#%%
print('='*30)
def print_me(col):
    print('[print_me]',col)
    return col

print(df.apply(print_me, axis=0))

#%%
print('='*30)
def print_me2(col):
    print('[print_me2]',col)
    print(col)
    print(col.iloc[0],col.iloc[1],col.iloc[2])
    return col

print(df.apply(print_me2, axis=0))
