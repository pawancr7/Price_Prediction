import os

print('Training Model using Linear Regression')


def train():
    import pickle
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import warnings
    warnings.filterwarnings("ignore")

    print('model training running')

    df12 = pd.read_csv('scripts/Datasets/bhp.csv')

    X = df12.drop(['price'], axis='columns')

    y = df12.price

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=10)

    lr_clf = LinearRegression()
    lr_clf.fit(X_train, y_train)

    with open('scripts/Datasets/model.pickle', 'wb') as f:
        pickle.dump(lr_clf, f)


l = os.listdir('scripts/Datasets/')
if 'model.pickle' not in l:
    train()
