import apibitmex.bitmex
client = apibitmex.bitmex.bitmex()

data = client.Quote.Quote_get(symbol='XBTUSD').result()

print(data)