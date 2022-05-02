#%%
import pandas as pd 
import altair as alt 

# %%

gssex = [x for x in range(10)]
gssey = [y for y in range(10)]

gssrx = [x for x in range(10)]
gssry = [-1 if y % 2 == 0 else 1 for y in range(10)]

sse = pd.DataFrame({'x':gssex,'y':gssey})
ssr = pd.DataFrame({'x':gssrx,'y':gssry})
# %%
ssechart = alt.Chart(sse).mark_point().encode(
    alt.X('x'),
    alt.Y('y')
)
ssechartf = ssechart + ssechart.transform_regression('x','y').mark_line()
# %%
ssrchart = alt.Chart(ssr[1:]).mark_point().encode(
    alt.X('x',),
    alt.Y('y',scale = alt.Scale(domain = [-5,5]))
)
ssrchartf = ssrchart + ssrchart.transform_regression('x','y').mark_line()
# %%
ssechartf.save('ssechart.png')
ssrchartf.save('ssrchart.png')
# %%
