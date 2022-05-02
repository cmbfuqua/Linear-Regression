#%%
import pandas as pd 
import altair as alt 
import numpy as np
# %%
data = pd.read_csv('airquality.csv')
#%%
alt.Chart(data, title = 'Maximum daily temperature').mark_bar().encode(
    alt.X('Temp', title = 'Temperature', bin = alt.Bin(maxbins=9)),
    alt.Y('count()')
)
# %%
data.Temp.mean()
# %%
data.Temp.std()
# %%
alt.Chart(data).mark_boxplot().encode(
    alt.X('Month',scale = alt.Scale(zero = False)),
    alt.Y('Temp',scale = alt.Scale(zero = False))
)
# %%
data.loc[data.Month == 5].Temp.mean()
# %%
data.loc[data.Month == 7].Temp.mean()

# %%
data.loc[data.Month == 5].Temp.std()
# %%
data.loc[data.Month == 7].Temp.std()
# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
x = pd.DataFrame(data.Wind)
y = pd.DataFrame(data.Temp)
model.fit(x,y)

print('intercept: {}'.format(model.intercept_))
print('coef: {}'.format(model.coef_))
# %%
import statsmodels.formula.api as smf

results = smf.ols('Temp ~ Wind', data).fit()

print(results.summary())

print('MSE: {}'.format(results.scale))
print('RMSE: {}'.format(np.sqrt(results.scale)))
# %%
