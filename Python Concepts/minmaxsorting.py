# dictionary 
stocks = {
    'Goog': 509,
    'Yahoo': 39,
    'Amazon': 123,
    'Apple': 345
}
# keys and values
# zips in to list of tuples

print(max(zip(stocks.values(), stocks.keys())))  # need to give two list as an input

print(min(zip(stocks.keys(), stocks.values()))) 

print(sorted(zip(stocks.values(), stocks.keys()))) 

print(sorted(zip(stocks.keys(), stocks.values()))) # sorted accrdoing to alphabest 