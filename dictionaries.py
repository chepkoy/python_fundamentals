from pprint import pprint as pp

urls = {
    'Google': 'http://google.com',
    'pluralsight': 'http://pluralsight.com',
    'Microsoft ': 'http://microsoft.com'
}

# dict constructor accepting iterable series of key-value 2-tuples
names_and_ages = [('allan', 24),('naomi', 19), ('brian', 13)]
d = dict(names_and_ages)

# keyword arguments - requires keys are valid python identifiers

phonetic = dict(a='alfa', b = 'bravo', c = 'charlie')

# Copying
d = dict(goldenrod=0xdaa529, indigo = '0xsffs2', seashell= 0x3433)

e = d.copy()

# using the dict constructor

f = dict(e)

# Extending a dictionary
g = dict(wheat = 0x23434, khaki = 0x87344)

f.update(g)

# Update replaces values corresponding to duplicate keys

stocks = {'GOOG': 891, 'AAPL': 416}
stocks.update({'GOOG': 894, 'YAHOO': 34})

# Iteration is over keys
colors = dict(aquamarine ="#86888", blue = "#DEGD888")
for key in colors:
    print("{key} => {value}".format(key=key, value=colors[key]))


# use values for an iterable view onto the series of values

for value in colors.values():
    print(value)

# keys method gives iterable view onto keys-not often needed

for key in colors.keys():
    print(key)

# Use items for an iterable view onto the series of key-value tuples

for key, value in colors.items():
    print("{key} => {value}".format(key=key, value=value))

# Membership in and not in operators work on the keys

symbols = dict(usd = '\u0024', gbp = '\u00a3')
'usd' in symbols

# use del keyword to remove by key

del d[key]

# python standard library pprint module
pp(colors)