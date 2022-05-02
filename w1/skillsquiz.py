#%%
import altair as alt 
import pandas as pd 
import numpy as np 
import statsmodels.formula.api as sm

#%%
data = pd.read_csv('../data/airquality.csv')

# %%
modela = sm.ols('Wind ~ Temp',data = data)
resultsa = modela.fit()
print(resultsa.summary())
print('MSE: {}'.format(resultsa.scale))
print('RMSE: {}'.format(np.sqrt(resultsa.scale)))
#%%
pred = pd.DataFrame({'Temp':[72,72,72,72]})
print(resultsa.predict(pred.Temp))
#%%
cars = pd.read_csv('../data/mtcars.csv')

# %%
resultsc = sm.ols('mpg ~ wt',data = cars).fit()
print(resultsc.summary())
# %%
pred = pd.DataFrame({'wt':[3]})
print(resultsc.predict(pred.wt))
# %%
chart = alt.Chart(cars).mark_point().encode(
    alt.X('wt'),
    alt.Y('mpg')
)

chart + chart.transform_regression('wt','mpg').mark_line()
# %% air quality part
from diagnosticPlots import diagnostic_plots
from statsmodels import api 
diagnostic_plots(data.Temp,'Temp',data.Wind,resultsa)

# %% cars part
diagnostic_plots(cars.wt,'wt',cars.mpg,resultsc)
# %%
