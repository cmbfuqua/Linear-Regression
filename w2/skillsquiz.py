#%%
import pandas as pd 
import altair as alt 
import numpy as np 
from statsmodels.formula.api import ols
# %%
data = pd.read_csv('../data/orange.csv')
#%%
chart = alt.Chart(data).mark_point().encode(
    alt.X('age'),
    alt.Y('circumference')
)
chart + chart.transform_regression('age','circumference').mark_line()
# %%
model = ols('circumference ~ age',data).fit()
model.summary()
# %%
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
corcoef = np.corrcoef(data.circumference,data.age)[0][1]
print(f'Correlation: {corcoef}')
# %%
pred = pd.DataFrame({'age':[3*365]})
model.predict(pred.age)
# %%
data = pd.read_csv('../data/mtcars.csv')
# %%
modelwt = ols('mpg ~ wt',data).fit()
modelcyl = ols('mpg ~ cyl',data).fit()
modelhp = ols('mpg ~ hp',data).fit()
# %%
for model in [modelwt,modelcyl,modelhp]:
    sse = np.sum((model.fittedvalues - data.mpg)**2)
    print(f'SSE: {sse.round(2)}')
    #calculate ssr
    ssr = np.sum((model.fittedvalues - data.mpg.mean())**2)
    print(f'SSR: {ssr.round(2)}')
    #calculate sst
    ssto = ssr + sse
    print(f'SSTO: {ssto.round(2)}')
    r2 = 1- sse/ssto
    print(f'R^2: {r2.round(2)}')

corcoef = np.corrcoef(data.mpg,data.wt)[0][1]
print(f'Correlation: {corcoef}')
corcoef = np.corrcoef(data.mpg,data.cyl)[0][1]
print(f'Correlation: {corcoef}')
corcoef = np.corrcoef(data.mpg,data.hp)[0][1]
print(f'Correlation: {corcoef}')
# %%
from diagnosticPlots import diagnostic_plots

diagnostic_plots(d)