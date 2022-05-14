#%%
from matplotlib.pyplot import axis
from matplotlib.transforms import Transform
import pandas as pd 
import altair as alt 
import numpy as np 

from statsmodels.formula.api import ols
from diagnosticPlots import diagnostic_plots as diagplots 
from summary_stats import summary_stats as sumstats
# %%
datame = pd.read_excel('../data/cars.xlsx')
data = datame.loc[datame.i_bought != 1]
# %%
chart_basic = alt.Chart(data,title = '2001 Chevy Blazer +- 3 years').mark_point().encode(
    alt.X('scale_mileage:Q',title = 'Mileage (1K)',scale = alt.Scale(zero = False),axis = alt.Axis(grid = False)),
    alt.Y('scale_price:Q',title = 'Price USD (1K)',scale = alt.Scale(zero = False),axis = alt.Axis(format = '$'))
).transform_calculate(
    scale_mileage = 'datum.mileage/1000',
    scale_price = 'datum.price/1000'
).properties(
    width = 500
)
chart_basic
#%%
#chart_basic.save('intro.png')
# %%
data['sqrt_price'] = data.price**.5
data['log_price'] = np.log(data.price)

# %%
chart_basic = alt.Chart(data,title = '2001 Chevy Blazer +- 3 years').mark_point().encode(
    alt.X('scale_mileage:Q',title = 'Mileage (1K)',scale = alt.Scale(zero = False),axis = alt.Axis(grid = False)),
    alt.Y('log_price:Q',title = 'Price LOG USD',scale = alt.Scale(zero = False),axis = alt.Axis(format = '$'))
).transform_calculate(
    scale_mileage = 'datum.mileage/1000',
).properties(
    width = 500
)

reg = chart_basic.transform_regression('scale_mileage','log_price').mark_line()
chartb = chart_basic + reg
chartb
#%%
#chartb.save('log_chart.png')

# %%
reg_type= 'exp'
chart_basic = alt.Chart(data,title = 'Chevy Blazer').mark_point().encode(
    alt.X('scale_mileage:Q',title = 'Mileage (10K)',
        scale = alt.Scale(zero = False),
        axis = alt.Axis(grid = False)),
    alt.Y('scale_price:Q',title = 'Price USD (10K)',
        scale = alt.Scale(zero = False,domain = [0,6]),
        axis = alt.Axis(format = '$'))
).transform_calculate(
    scale_mileage = 'datum.mileage/10000',
    scale_price = 'datum.price/10000'
).properties(
    width = 500
)

reg = chart_basic.transform_regression('scale_mileage', 'scale_price',method = reg_type).mark_line(clip = True)

chartf = chart_basic + reg 
chartf
#%%
#chartf.save(f'line_{reg_type}.png')

#%%
reg_type= 'pow'
chart_basic = alt.Chart(data,title = 'Chevy Blazer').mark_point().encode(
    alt.X('scale_mileage:Q',title = 'Mileage (10K)',
        scale = alt.Scale(zero = False),
        axis = alt.Axis(grid = False)),
    alt.Y('scale_price:Q',title = 'Price USD (10K)',
        scale = alt.Scale(zero = False,domain = [0,6]),
        axis = alt.Axis(format = '$'))
).transform_calculate(
    scale_mileage = 'datum.mileage/10000',
    scale_price = 'datum.price/10000'
).properties(
    width = 500
)

reg = chart_basic.transform_regression('scale_mileage', 'scale_price',method = reg_type).mark_line(clip = True)

chartf = chart_basic + reg 

#chartf.save(f'line_{reg_type}.png')
chartf
# %%
model = ols('log_price ~ mileage',data = data).fit()
model.summary()
#%%
sumstats(model,'log_price',data)
# %%
diagplots(data.mileage,'mileage',data.log_price,model)
# %%
predict = pd.DataFrame({'mileage':[150000]})
np.exp(model.predict(predict.mileage)[0])
# %%
print(pd.DataFrame({
    'Metric':['MSE','RMSE','SSE','SSR','SSTO','R^2','RSE'],
    'Value':[.21,.46,6.36,47.15,53.51,.88,.46]
}).to_markdown())

#%%
fake = []
value = []
for i in range(0,260000,1000):
    fake.append(i)
    output = np.exp(11.01-(.00001575 * i))
    value.append(output)
faked = pd.DataFrame({'x':fake,'y':value})
# %%
line = alt.Chart(faked).mark_line(color = 'black').encode(
    alt.X('x', title = None),
    alt.Y('y',title = None)
)
my = alt.Chart(datame,title = 'Blue: Data  Green: My Purchase  Red: Possible Sell Price').mark_circle(clip = True).encode(
    alt.X('mileage', title = 'Mileage'),
    alt.Y('price', title = 'Sale Price',scale = alt.Scale(zero = False,domain = [1000,60000])),
    alt.Color('i_bought:N',title = None,legend = None,scale = alt.Scale(range = ['blue','green','red']))
)
f = line + my
f.save('mychart.png')

# %%
