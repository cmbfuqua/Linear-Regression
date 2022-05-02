#%%
import pandas as pd
import numpy as np 
import altair as alt
from statsmodels.formula.api import ols
# %%
data = pd.read_csv('../data/weatherclean.csv')
data = data.loc[data.today != 1]
# %%
model = ols('temp2days ~ day_score', data).fit()
preds = model.predict()
# %%
data['resids'] = data.temp2days - preds
# %%
# make residuals
for i in range(len(data)):
    i += 1
    x = data.day_score[i]
    y_top = data.temp2days[i]
    y_bottom = data.temp2days[i] - data.resids[i]
    temp = pd.DataFrame({'x':x,'y':[y_top,y_bottom]})
    charti = alt.Chart(temp).mark_line().encode(
        alt.X('x'),
        alt.Y('y')
    )
    if i == 1:
        chart = charti
    else:
        chart = chart + charti
chart

# %%
chart2 = alt.Chart(data, title = 'Residuals').mark_point().encode(
    alt.X('day_score',scale = alt.Scale(zero = False)),
    alt.Y('temp2days',scale = alt.Scale(zero = False))
)
chartr = chart2.transform_regression('day_score','temp2days').mark_line()
chartf = chart2 + chart + chartr
# %%
chartf.save('residuals_basic.png')
#%%
# make sse
for i in range(len(data)):
    i2 = i + 1
    for s in range(4):
        if s == 0:
            # to get left |
            x = data.day_score[i2]
            y_top = data.temp2days[i2]
            y_bottom = data.temp2days[i2] - data.resids[i2]
            temp = pd.DataFrame({'x':x,'y':[y_top,y_bottom]})
            chart = alt.Chart(temp).mark_line(color = 'red').encode(
                alt.X('x'),
                alt.Y('y')
            )
        elif s == 1:
            # to get right |
            x = data.day_score[i2] + data.resids[i2]
            y_top = data.temp2days[i2]
            y_bottom = data.temp2days[i2] - data.resids[i2]
            temp = pd.DataFrame({'x':x,'y':[y_top,y_bottom]})
            chart1 = alt.Chart(temp).mark_line(color = 'red').encode(
                alt.X('x'),
                alt.Y('y')
            )
            chart = chart + chart1
        elif s == 2:
            # to get top 
            x_left = data.day_score[i2]
            x_right = data.day_score[i2] + data.resids[i2]
            y_left = data.temp2days[i2]
            y_right = data.temp2days[i2]
            temp = pd.DataFrame({'x':[x_left,x_right],'y':[y_left,y_right]})
            chart1 = alt.Chart(temp).mark_line(color = 'red').encode(
                alt.X('x'),
                alt.Y('y')
            )
            chart = chart + chart1
        elif s == 3:
            # to get bottom 
            x_left = data.day_score[i2]
            x_right = data.day_score[i2] + data.resids[i2]
            y_left = data.temp2days[i2] - data.resids[i2]
            y_right = data.temp2days[i2] - data.resids[i2]
            temp = pd.DataFrame({'x':[x_left,x_right],'y':[y_left,y_right]})
            chart1 = alt.Chart(temp).mark_line(color = 'red').encode(
                alt.X('x'),
                alt.Y('y')
            )
            chart = chart + chart1
    if i == 0:
        charts = chart
    else:
        charts = charts + chart
charts

#%%
chart1 = alt.Chart(data,).encode(
    alt.X('day_score',title = 'Day Score',scale = alt.Scale(zero = False)),
    alt.Y('temp2days',title = 'Temp2days',scale = alt.Scale(zero = False))
).transform_regression('day_score','temp2days').mark_line()
chartf = chart1 + charts
chartf
#%%
chartf.save('sse.png')
# %%
# make SSR
for i in range(len(data)):
    i += 1
    x = data.day_score[i]
    y_top = preds[i-1]
    y_bottom = preds[i-1] - (preds[i-1] - data.temp2days.mean())
    temp = pd.DataFrame({'x':x,'y':[y_top,y_bottom]})
    charti = alt.Chart(temp).mark_line().encode(
        alt.X('x'),
        alt.Y('y')
    )
    if i == 1:
        chart = charti
    else:
        chart = chart + charti
chart
#%%
regres = pd.DataFrame({'x':[390,425],'y':[data.temp2days.mean(),data.temp2days.mean()]})

chart1 = alt.Chart(data).encode(
    alt.X('day_score',title = 'Day Score',scale = alt.Scale(zero = False)),
    alt.Y('temp2days',title = 'Temp2days',scale = alt.Scale(zero = False))
).transform_regression('day_score','temp2days').mark_line()
chart2 = alt.Chart(regres).mark_line(color = 'red').encode(
    alt.X('x'),
    alt.Y('y')
)
chartf = chart1 + chart2 + chart
chartf
#%%
chartf.save('regress_line.png')
# %%
# Make SSTO
for i in range(len(data)):
    i += 1
    x = data.day_score[i]
    y_top = data.temp2days[i]
    y_bottom = data.temp2days[i] - (data.temp2days[i] - data.temp2days.mean())
    temp = pd.DataFrame({'x':x,'y':[y_top,y_bottom]})
    charti = alt.Chart(temp).mark_line().encode(
        alt.X('x'),
        alt.Y('y')
    )
    if i == 1:
        chart = charti
    else:
        chart = chart + charti
chart
# %%

regres = pd.DataFrame({'x':[390,425],'y':[data.temp2days.mean(),data.temp2days.mean()]})
chartr = alt.Chart(regres).mark_line(color = 'red').encode(
    alt.X('x'),
    alt.Y('y')
)
chart1 = alt.Chart(data).mark_point().encode(
    alt.X('day_score'),
    alt.Y('temp2days',scale = alt.Scale(zero = False))
)
chartf = chartr + chart + chart1
chartf
# %%
chartf.save('initial.png')
# %%
