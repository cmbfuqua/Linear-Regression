def summary_stats(results,data):
    import numpy as np
    print(results.summary())
    print('MSE: {}'.format(results.scale))
    print('RMSE: {}'.format(np.sqrt(results.scale)))
    model = results
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