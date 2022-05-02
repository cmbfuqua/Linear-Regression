#%%
import pandas as pd 
from statsmodels.formula.api import ols

data = pd.read_csv('../dataset-14820.csv')
# %%
males = data.loc[data.sex == 'M']
# %%
model = ols('weight ~ height',data = males).fit()
model.summary()
# %%
data = pd.read_csv('../dataset-90380.csv')

# %%
model = ols('Murder ~ Assault',data = data).fit()
model.summary()
# %%
