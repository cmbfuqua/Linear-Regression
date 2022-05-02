#%%
import pandas as pd 
import altair as alt 
import numpy as np 

from statsmodels.formula.api import ols
# %%
data = pd.read_csv('../data/mtcars.csv')
# %%
model = ols('wt ~ disp',data = data).fit()
model.summary()
# %%
model = ols('mpg~wt',data = data).fit()
model.summary()
# %%
pred = pd.DataFrame({'wt':[2.7]})
# %%
model.predict(pred.wt)
# %%
