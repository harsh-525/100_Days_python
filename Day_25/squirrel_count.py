import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data.columns)

# temp = data[data['Primary Fur Color'] == 'Black'].count()['Unique Squirrel ID']
#
# print(temp, "\n", type(temp))

final_data = {
    'fur_color': list(set(data['Primary Fur Color'])),
    'count': [
        # data[data['Primary Fur Color'] == 'Cinnamon'].count()['Unique Squirrel ID'],
        # data[data['Primary Fur Color'] == 'Gray'].count()['Unique Squirrel ID'],
        # data[data['Primary Fur Color'] == 'Black'].count()['Unique Squirrel ID'],
        # data[data['Primary Fur Color'] == 'nan'].count()['Unique Squirrel ID']
        len(data[data['Primary Fur Color'] == 'Cinnamon']),
        len(data[data['Primary Fur Color'] == 'Gray']),
        len(data[data['Primary Fur Color'] == 'Black']),
        len(data[data['Primary Fur Color'] == 'nan']),
    ]
}
squirrel_fur_count = pd.DataFrame(final_data)
print(squirrel_fur_count.sort_values(by='count', ascending=False))
