#%%
import pandas as pd 
import altair as alt 
import numpy as np 

from statsmodels.formula.api import ols
from diagnosticPlots import diagnostic_plots
from summary_stats import summary_stats
# %%
data = pd.read_csv('../data/Caschool.csv')
# %%
alt.Chart(data).mark_point().encode(
    alt.X('mealpct'),
    alt.Y('testscr',scale = alt.Scale(zero = False))
)
# %%
model = ols('testscr ~ mealpct',data).fit()
model.summary()
# %%
diagnostic_plots(data.mealpct,'mealpct',data.testscr,model)
# %%
data = pd.read_csv('../data/clothing.csv')
#%%
alt.Chart(data2).mark_point().encode(
    alt.X('nhourspw:Q',scale = alt.Scale(zero = False)),
    alt.Y('ntsales:Q')
).transform_calculate(
    nhourspw = 'log(datum.hourspw)'
)
# %%
data2 = data.loc[data.index != 396]
model = ols('tsales ~ hourspw',data2).fit()
model.summary()
# %%
summary_stats(model,'tsales',data)
# %%
diagnostic_plots(data.hourspw,'hourspw',data.tsales,model)
# %%
from box_cox import boxcox
data['ntsales'] = boxcox(data.tsales)[0]

# %%
