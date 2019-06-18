from blockchain import blockexplorer
from base58 import b58encode
#vars() takes an object as a parameter which may be can a module, a class, an instance, or any object having __dict__ attribute.

#get_block()
block=blockexplorer.get_block('00000000000000000018a65ff0bbbc2a93493c693d05dd65c6a8dcbb881f55fb')
block_d=vars(block) #creating dictionary of object block
print("Keys in Block:")
for x in block_d:
	print(x)
print("\nEnter key to display its value:",end=" ")
key=input()
print("\nValue of {}:{}".format(key,block_d[key]))

#get_tx()
transaction=blockexplorer.get_tx('459489331')  #one of the transaction ids of latest block
trans_d=vars(transaction)
print("Keys in Transaction:")
for x in trans_d:
	print(x)
print("\nEnter key to display its value:",end=" ")
key=input()
print("\nValue of {}:{}".format(key,trans_d[key]))

#get_address()
addr=blockexplorer.get_address('1FfmbHfnpaZjKFvyi1okTjJJusN455paPH')
addr_d=vars(addr)
print("Keys available:")
for i in addr_d:
        print(i)
print("Enter key to view:",end=" ")
key=input()
if(key!='transactions'):
	print("Value of {}:{}".format(key,addr_d[key]))
else:
	print(dir(addr_d[key]))
	
#get_block_height()
i=lblock_d['height']
print("Height of latest block is:",i)
height=blockexplorer.get_block_height(str(i))
i=0
for x in height:
	i=i+1
	print("Block ",i)
	a=vars(x)
	print("\nKeys of block",i)
	for y in a:
		print(y)
	print("Enter key to view:",end=" ")
	k=input()
	print("\nValue of {}:{}".format(k,a[k]))
print("Total no of blocks matching this height:",i)

#get_xpub() #KEY_ERROR gap__limit
xpubs=blockexplorer.get_xpub('xpub6CUGRUonZSQ4TWtTMmzXdrXDtypWKiKrhko4egpiMZbpiaQL2jkwSB1icqYh2cfDfVxdx4df189oLKnC5fSwqPfgyP3hooxujYzAu3fDVmz')
print(xpubs)

#get_multi_addrress
add=blockexplorer.get_multi_address('1FfmbHfnpaZjKFvyi1okTjJJusN455paPH')
add_d=vars(add)
print("Keys available:")
for i in add_d:
	print(i)
print("Enter key to view:",end=" ")
key=input()
if((key!='addresses')and (key!='transactions')):
	print("Value of {}:{}".format(key,add_d[key]))
else:
	adr=add_d[key]
	print(dir(adr))

#get_unspent_outputs
unspent=blockexplorer.get_unspent_outputs('1FfmbHfnpaZjKFvyi1okTjJJusN455paPH')
print(dir(unspent))
	
#get_latest_block()
lblock=blockexplorer.get_latest_block()
lblock_d=vars(lblock) #creating dictionary of object latest block
print("Keys in Block:")
for x in lblock_d:
	print(x)
print("\nEnter key to display its value:",end=" ")
key=input()
print("\nValue of {}:{}".format(key,lblock_d[key]))

#get_unconfirmed_tx()
utx=blockexplorer.get_unconfirmed_tx()
print("No. of unconfirmed transactions:",len(utx))
c=1
for i in utx:
	tx_d=vars(i)
	print("{}. Hash:{}, Time:{}".format(c,tx_d['hash'],tx_d['time']))
	c=c+1

#get_blocks()
simblocks=blockexplorer.get_blocks()
c=1
print("No. of Simple Blocks:",len(simblocks))
for i in simblocks:
	simb_d=vars(i)
	print("{}. Hash:{}, Height:{}, Time:{}, Main Chain:{}".format(c,simb_d['hash'],simb_d['height'],simb_d['time'],simb_d['main_chain']))
	c=c+1







