#%%
import pandas as pd 
import altair as alt
import numpy as np 

from statsmodels.formula.api import ols
from diagnosticPlots import diagnostic_plots as diagplots
from summary_stats import summary_stats
# %%
data = pd.read_csv('../data/')