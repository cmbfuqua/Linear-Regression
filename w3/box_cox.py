def boxcox(x_val):
    from scipy.stats import boxcox as bc

    rlambda = bc(x_val).__getitem__(1)

    array = bc(x_val).__getitem__(0)

    print(f'Lambda: {rlambda}')
    return array