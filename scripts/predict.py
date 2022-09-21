def pred(location, sqft, bath, bhk):
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
    price = predict_price(location, sqft, bath, bhk)
    return price
