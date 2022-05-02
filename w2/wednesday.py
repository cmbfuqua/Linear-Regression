#%%
import pandas as pd 
import altair as alt 
from statsmodels.formula.api import ols

# %%
data = pd.read_csv('../data/mtcars.csv')
# %%
sum([x for x in range(1,7)])
# %%
sum([5, 15, 2, 29, 35, 24, 25, 39])
# %%
sum([x**2 for x in range(1,7)])

# %%
total = 0
for i in [5, 15, 2, 29, 35, 24, 25, 39]:
    total += i**2
print(total)
# %%
alt.Chart(data).mark_point().encode(
    alt.X('wt'),
    alt.Y('qsec')
)
# %%
