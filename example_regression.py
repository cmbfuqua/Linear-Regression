#%%
import pandas as pd 
import altair as alt 
import numpy as np
# %%
data = pd.read_csv('data/airquality.csv')
# %%
# Create the regression
import statsmodels.formula.api as smf

results = smf.ols('Temp ~ Wind + Month', data).fit()

# output regression summary statistics
print(results.summary())
print('MSE: {}'.format(results.scale))
print('RMSE: {}'.format(np.sqrt(results.scale)))
model = results
sse = np.sum((model.fittedvalues - data.circumference)**2)
print(f'SSE: {sse.round(2)}')
#calculate ssr
ssr = np.sum((model.fittedvalues - data.circumference.mean())**2)
print(f'SSR: {ssr.round(2)}')
#calculate sst
ssto = ssr + sse
print(f'SSTO: {ssto.round(2)}')
r2 = 1- sse/ssto
print(f'R^2: {r2.round(2)}')
# %%
'''
To make a prediction, you need to first create a Data Frame
of your predictions you want to make, then you need to make sure
it has the same column name as the original explanatory column.
Then and ONLY then will the prediction work. 

This is horrible programming. 
'''
pred = pd.DataFrame({'Temp':[72,72,72,72]})
print(results.predict(pred.Temp))