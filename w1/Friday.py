#%%
import pandas as pd 
import altair as alt
import statsmodels 

data = pd.read_csv('../data/airquality.csv')

# %%
may = data.loc[data.Month == 5]
# %%
chart = alt.Chart(may).mark_point().encode(
    alt.X('Day'),
    alt.Y('Temp',scale = alt.Scale(zero = False))
)
chart + chart.transform_regression('Day','Temp').mark_line()

#%%
from statsmodels.formula.api import ols
#%%
model = ols('Temp ~ Day',data = may).fit()
model.summary()

# %%
