countries = ["USA", "India", "Germany", "France"]
cities = ['Washington', 'NewDelhi', 'Berlin', 'Pairs']

# Make A Dictionary 

z = zip(countries, cities)
d = dict(z)

# Display Key - Values Pairs From Dictionary d

print('{:15s} -- {:15s} '.format('COUNTRY', 'CAPITAL'))
for k in d:
    print('{:15s} -- {:15s} '.format(k, d[k]))