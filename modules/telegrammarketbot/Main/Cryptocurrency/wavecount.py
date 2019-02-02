# Wave Count
from cryptocompare_wrapper import daily_price_historical

# Get Price
df = daily_price_historical('BTC')

df.close
