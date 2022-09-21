from pymongo import MongoClient
import time
from predict import pred
from getpass import getpass

key = getpass('Enter MongoDB password ')
timeout = int(input('Enter Timeout Time '))
req = 'mongodb+srv://Akash:{}@cluster0.6pagbip.mongodb.net/?retryWrites=true&w=majority'.format(
    key)

client = MongoClient(req)
db = client.get_database('PricePrediction')
recordPrice = db.PredictionPrice


def get():
    # Mongo DB
    print('Server Running')

    records = db.PredictionData
    fetched = list(records.find())
    l = fetched[1]
    return l


location = ' '
sqft = ' '
bath = ' '
bhk = ' '

for i in range(timeout):
    l = get()
    x = (location, sqft, bath, bhk)
    y = (str(l['location']), l['sqft'], l['bath'], l['bhk'])

    if x != y:
        location = str(l['location'])
        sqft = l['sqft']
        bath = l['bath']
        bhk = l['bhk']
        print('not same')

        # predict fun
        price_predicted = pred(location, sqft, bath, bhk)

        price = {
            'price': price_predicted
        }

        recordPrice.insert_one(price)

        log_time = '{} '.format(time.ctime())
        log_args = '{},{},{},{} '.format(location, sqft, bath, bhk)
        price_val = '{} \n'.format(str(round(price_predicted, ndigits=2)))
        labels = '[time, location, sqft, bath, bhk, price]\n'

        with open('logs/logs.txt', 'a') as f:
            f.write(labels)
            f.write(log_time)
            f.write(str(log_args))
            f.write(price_val)

    else:
        print('same')
        get()
