from blockchain import createwallet
#create_wallet()
wallet=createwallet.create_wallet('675passwd','367404166','http://localhost:3000/',label='demo')
wallet_d=vars(wallet)
print("Keys of wallet:")
for i in wallet_d:
	print(i)
print("Enter key to view:",end=" ")
key=input()
print("Value of {}:{}".format(key,wallet_d[key]))

