from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

df12 = pd.read_csv('scripts/Datasets/bhp.csv')

X = df12.drop(['price'], axis='columns')

y = df12.price

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10)


cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

print(cross_val_score(LinearRegression(), X, y, cv=cv))
print(cross_val_score(Lasso(), X, y, cv=cv))
print(cross_val_score(DecisionTreeRegressor(), X, y, cv=cv))
