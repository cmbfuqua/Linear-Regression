#%%
import pandas as pd 
import altair as alt 
import statsmodels as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression as lr

# %%
data = pd.read_csv('../data/weather.csv')

# %%
wind_dummies = pd.get_dummies(data.wind_direction,drop_first=True)
#%%
data['sw'] = wind_dummies.sw 
data['w'] = wind_dummies.w
#%%
data = data.drop(columns='wind_direction')

# %%
coef = []
cols = []
for col in ['hightemp', 'precipitation', 'windspeed', 'cloudy','lowtemp', 'air_pressure', 'humidity', 'thisWeek', 'sw', 'w']:
    model = ols('temp_in2days ~ {}'.format(col),data = data).fit()
    cols.append(col)
    coef.append(model.params[1])
    print('col: {}  coef: {}'.format(col,model.params[1]))

data_coef = pd.DataFrame({'col':cols,'coef':coef})
# %%
new_vals = pd.DataFrame()

for value in data_coef.col:
    print(value)
    scaler = data_coef.loc[data_coef.col == value].reset_index().coef[0].round(3)
    new_vals[value] = data[value] * scaler
# %%
new_vals['today'] = data.today
new_vals['temp2days'] = data.temp_in2days
new_vals['day_score'] = (new_vals.hightemp + 
                        new_vals.precipitation + 
                        new_vals.windspeed +
                        new_vals.cloudy + 
                        new_vals.lowtemp +
                        new_vals.air_pressure + 
                        new_vals.humidity +
                        new_vals.thisWeek + 
                        new_vals.sw +
                        new_vals.w)
                        
#%%
chart3 = alt.Chart(new_vals,title = ['Daily Max Temp In Rexburg April 2022','Prediction In Blue']).mark_point().encode(
    alt.X('day_score', title = 'Scaled Day Score',scale = alt.Scale(zero=False)),
    alt.Y('temp2days',title = 'High Temp In 2 Days (F)',scale = alt.Scale(zero=False)),
).transform_regression('day_score','temp2days').mark_line()
chart3 = chart3 + chart3.transform_regression('day_score','temp2days').mark_line()
#%%
chart3.save('regress_line.png')
# %%
train = new_vals.loc[new_vals.today != 1]
test = new_vals.loc[new_vals.today == 1]
modelf = ols('temp2days ~ day_score',data = train).fit()

# %%
modelf.predict(test.drop(columns = 'temp2days'))
# %%
import numpy as np
print('MSE: {}'.format(modelf.scale))
print('RMSE: {}'.format(np.sqrt(modelf.scale)))
modelf.summary()
# %%
final = new_vals.copy()
final['temp2days'][0] = 57

chart = alt.Chart(final,title = ['Daily Max Temp In Rexburg April 2022','Prediction In Blue']).mark_point().encode(
    alt.X('day_score', title = 'Scaled Day Score',scale = alt.Scale(zero=False)),
    alt.Y('temp2days',title = 'High Temp In 2 Days (F)',scale = alt.Scale(zero=False)),
    alt.Color('today:N',scale = alt.Scale(range = ['blue','red']),legend = None)
)

finalc = chart + chart.transform_regression('day_score','temp2days').mark_line()
finalc
#%%
finalc.save('prediction.png')
# %%
chart2 = alt.Chart(final,title = ['Daily Max Temp In Rexburg April 2022','Prediction In Blue']).mark_point().encode(
    alt.X('day_score', title = 'Scaled Day Score',scale = alt.Scale(zero=False)),
    alt.Y('temp2days',title = 'High Temp In 2 Days (F)',scale = alt.Scale(zero=False)),
)
chart2.save('initial.png')
# %%
from diagnosticPlots import diagnostic_plots

diagnostic_plots(train.day_score,'day_score',train.temp2days,modelf)
# %%
