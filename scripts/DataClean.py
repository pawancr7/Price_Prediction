import os
import pandas as pd
import numpy as np

print("Cleaning Data")
l = os.listdir('scripts/Datasets/')
if 'bhp.csv' not in l:

    df1 = pd.read_csv("scripts/Datasets/bengaluru_house_prices.csv")

    df2 = df1.drop(['area_type', 'society', 'balcony',
                    'availability'], axis='columns')

    df3 = df2.dropna()

    df3['bhk'] = df3.loc[:, ('size')].apply(lambda x: int(x.split(' ')[0]))

    def is_float(x):
        try:
            float(x)
        except:
            return False
        return True

    df3[~df3['total_sqft'].apply(is_float)].head(10)

    def convert_sqft_to_num(x):
        tokens = x.split('-')
        if len(tokens) == 2:
            return (float(tokens[0])+float(tokens[1]))/2
        try:
            return float(x)
        except:
            return None

    df4 = df3.copy()
    df4.total_sqft = df4.total_sqft.apply(convert_sqft_to_num)
    df4 = df4[df4.total_sqft.notnull()]
    df4.head(2)

    df5 = df4.copy()
    df5['price_per_sqft'] = df5['price']*100000/df5['total_sqft']

    df5_stats = df5['price_per_sqft'].describe()

    df5.location = df5.location.apply(lambda x: x.strip())
    location_stats = df5['location'].value_counts(ascending=False)
    location_stats

    location_stats.values.sum()

    len(location_stats[location_stats > 10])

    len(location_stats)

    len(location_stats[location_stats <= 10])

    location_stats_less_than_10 = location_stats[location_stats <= 10]
    location_stats_less_than_10

    len(df5.location.unique())

    df5.location = df5.location.apply(
        lambda x: 'other' if x in location_stats_less_than_10 else x)
    len(df5.location.unique())

    df5.head(10)

    df5[df5.total_sqft/df5.bhk < 300].head()

    df5.shape

    df6 = df5[~(df5.total_sqft/df5.bhk < 300)]
    df6.shape

    df6.price_per_sqft.describe()

    def remove_pps_outliers(df):
        df_out = pd.DataFrame()
        for key, subdf in df.groupby('location'):
            m = np.mean(subdf.price_per_sqft)
            st = np.std(subdf.price_per_sqft)
            reduced_df = subdf[(subdf.price_per_sqft > (m-st))
                               & (subdf.price_per_sqft <= (m+st))]
            df_out = pd.concat([df_out, reduced_df], ignore_index=True)
        return df_out

    df7 = remove_pps_outliers(df6)

    def remove_bhk_outliers(df):
        exclude_indices = np.array([])
        for location, location_df in df.groupby('location'):
            bhk_stats = {}
            for bhk, bhk_df in location_df.groupby('bhk'):
                bhk_stats[bhk] = {
                    'mean': np.mean(bhk_df.price_per_sqft),
                    'std': np.std(bhk_df.price_per_sqft),
                    'count': bhk_df.shape[0]
                }
            for bhk, bhk_df in location_df.groupby('bhk'):
                stats = bhk_stats.get(bhk-1)
                if stats and stats['count'] > 5:
                    exclude_indices = np.append(
                        exclude_indices, bhk_df[bhk_df.price_per_sqft < (stats['mean'])].index.values)
        return df.drop(exclude_indices, axis='index')

    df8 = remove_bhk_outliers(df7)
    df8.shape

    df8[df8.bath > 10]

    df8[df8.bath > df8.bhk+2]

    df9 = df8[df8.bath < df8.bhk+2]

    df10 = df9.drop(['size', 'price_per_sqft'], axis='columns')

    dummies = pd.get_dummies(df10.location)
    dummies.head(3)

    df11 = pd.concat(
        [df10, dummies.drop('other', axis='columns')], axis='columns')
    df12 = df11.drop('location', axis='columns')

    df12.to_csv("bhp.csv", index=False)
