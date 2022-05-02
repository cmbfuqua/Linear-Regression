#%%
import altair as alt 
import pandas as pd 
import numpy as np 
import statsmodels.formula.api as sm

#%%
data = pd.read_csv('../data/airquality.csv')
# %%
chart = alt.Chart(data).mark_point().encode(
    alt.X('Wind', title = 'Average wind speed in miles per hour between 7am and 10am'),
    alt.Y('Temp',title = 'Temp in degrees F',scale = alt.Scale(zero = False))
)

chart = chart + chart.transform_regression('Wind', 'Temp').mark_line()

chart.properties(
    title = {
        'text': 'Max daily temp',
        'subtitle':'May to September 1973'
    }
)
# %%
model = sm.ols('Wind ~ Temp',data = data)
results = model.fit()
print(results.summary())
print('MSE: {}'.format(results.scale))
print('RMSE: {}'.format(np.sqrt(results.scale)))
#%%
pred = pd.DataFrame({'Temp':[72,72,72,72]})
print(results.predict(pred.Temp))
#%%

