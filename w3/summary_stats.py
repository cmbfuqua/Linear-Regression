def summary_stats(results,Ycolumn,data):
    import numpy as np
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