#%%
import pandas as pd 
import numpy as np 
import altair as alt
from statsmodels.formula.api import ols 
# %%
data = pd.read_csv('../data/orange.csv')
# %%
chart = alt.Chart(data).mark_point().encode(
    alt.X('age'),
    alt.Y('circumference')
)
chart
# %%
chart +chart.transform_regression('age','circumference',method = 'pow').mark_line()
# %%
