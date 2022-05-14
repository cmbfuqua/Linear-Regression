#%%
import pandas as pd 
import altair as alt
import numpy as np 

from statsmodels.formula.api import ols
# %%
data = pd.read_csv('../data/davis.csv')
# %%
model = ols('height ~ weight',data = data).fit()
model.summary()
# %%
chart = alt.Chart(data).mark_point().encode(
    alt.X('weight',scale = alt.Scale(zero = False)),
    alt.Y('height',scale = alt.Scale(zero = False))
)
chartf = chart + chart.transform_regression('weight','height').mark_line()
chartf
# %%
from diagnosticPlots import diagnostic_plots

diagnostic_plots(data.weight,'weight',data.height,model)
# %%
model2 = ols('height ~ weight',data = data.loc[data.index != 11]).fit()
model2.summary()
# %%
from diagnosticPlots import diagnostic_plots
datano = data.loc[data.index != 11]
diagnostic_plots(datano.weight,'weight',datano.height,model2)
# %%
data = pd.read_csv('../data/prestige.csv')
# %%
modelp = ols('income ~ prestige',data = data).fit()
modelp.summary()
#%%
chart = alt.Chart(data).mark_point().encode(
    alt.X('prestige',scale = alt.Scale(zero = False)),
    alt.Y('income',scale = alt.Scale(zero = False))
)
chartf = chart + chart.transform_regression('prestige','income').mark_line()
chartf

# %%
from summary_stats import summary_stats
summary_stats(modelp,'prestige',data)
# %%
data = pd.read_csv('../data/burt.csv')
# %%
modelb = ols('IQbio ~ IQfoster',data).fit()
modelb.summary()
# %%
data = pd.read_csv('../data/mtcars.csv')
data.head()
# %%
modelc = ols('mpg ~ disp',data).fit()
modelc.summary()
# %%
from summary_stats import summary_stats
summary_stats(modelc,'disp',data,1)
# %%
import numpy as np
Ycolumn = 'mpg'
results = modelc
print('MSE: {}'.format(results.scale.round(2)))
print('RMSE or Variance: {}'.format(np.sqrt(results.scale).round(2)))
model = results
sse = np.sum((model.fittedvalues- data[Ycolumn])**2)
print(f'SSE: {sse.round(2)}')
#calculate ssr
ssr = np.sum((model.fittedvalues - data[Ycolumn].mean())**2)
print(f'SSR: {ssr.round(2)}')
#calculate sst
ssto = ssr + sse
print(f'SSTO: {ssto.round(2)}')
r2 = 1- sse/ssto
print(f'R^2: {r2.round(2)}')
rse = np.sqrt(results.scale)
print(f'RSE: {rse.round(2)}')
# %%
data = pd.read_csv("../data/orange.csv")
modelo = ols('circumference ~ age',data).fit()
modelo.summary()
# %%
from summary_stats import summary_stats
summary_stats(modelo,'circumference',data)
# %%
from box_cox import boxcox
boxcox(data.circumference)
# %%
data['box_circumference'] = new_array[0]
# %%
modelo = ols('box_circumference ~ age',data).fit()
modelo.summary()
# %%
chart = alt.Chart(data).mark_point().encode(
    alt.X('age'),
    alt.Y('circumference')
)
chartf = chart + chart.transform_regression('age','circumference').mark_line()
chartf + chart.transform_regression('age','circumference',method = 'pow').mark_line()
# %%
from diagnosticPlots import diagnostic_plots
diagnostic_plots(data.age,'age',data.box_circumference,modelo)
# %%
from scipy.stats import boxcox
boxcox(data.circumference, alpha = .05)
# %%
