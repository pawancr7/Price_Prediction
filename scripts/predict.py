def pred():
    import time
    import json
    from unittest import result
    import numpy as np
    import pandas as pd
    import pickle
    import warnings
    warnings.filterwarnings("ignore")

    df12 = pd.read_csv('scripts/Datasets/bhp.csv')

    X = df12.drop(['price'], axis='columns')

    with open('scripts/Datasets/model.pickle', 'rb') as f:
        lr_clf = pickle.load(f)

    def predict_price(location, sqft, bath, bhk):
        loc_index = np.where(X.columns == location)[0][0]

        x = np.zeros(len(X.columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        return lr_clf.predict([x])[0]

    # args (location, sqft, bath, bhk)
    # eg: predict_price('Indira Nagar',1000, 3, 3)

    j = open('logs/data.json', 'r')
    js = json.load(j)

    loc = js['loc']
    sqft = int(js['sqft'])
    bath = int(js['bath'])
    bhk = int(js['bhk'])

    r = (predict_price(loc, sqft, bath, bhk))
    print('Predicted price ${}k'.format(round(r, ndigits=3)))
    result = {'result': round(r, ndigits=3)}

    j = open('logs/result.json', 'w')
    js = json.dump(result, j)

    log_time = '{} '.format(time.ctime())
    log_args = '{},{},{},{} '.format(loc, sqft, bath, bhk)
    price_val = '{} \n'.format(str(round(r, ndigits=3)))
    labels = '[time, location, sqft, bath, bhk, price]\n'

    with open('logs/logs.txt', 'a') as f:
        f.write(labels)
        f.write(log_time)
        f.write(str(log_args))
        f.write(price_val)
