from urllib import request
import urllib.request

# https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1638017738&period2=1669553738&interval=1d&events=history&includeAdjustedClose=true

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1638017738&period2=1669553738&interval=1d&events=history&includeAdjustedClose=true'

def download_stock_data(goog_url):
    response = request.urlopen(goog_url) # goesto url andconnect to the webpage
    csv = response.read()
    csv_str = str(csv)
    lines  = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,  "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
            
download_stock_data(goog_url)