from blockchain import exchangerates
#get_ticker()
ticker=exchangerates.get_ticker()
print("Exchange Rates:",list(ticker))
print("Enter Currency:",end=" ")
cur=input()
print("Keys in {}".format(cur))
ticker_c=vars(ticker[cur])
for i in ticker_c:
	print(i)
print("Enter key to view:",end=" ")
key=input()
print("Value of {}:{}".format(key,ticker_c[key]))

#to_btc()
btc_amount=exchangerates.to_btc('INR',400000)
print("Bitcoin amount:",btc_amount)
