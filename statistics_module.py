from blockchain import statistics
#get()
stats= statistics.get()
stats_d=vars(stats)
print("Keys in Stats:")
for i in stats_d:
	print(i)
print("Enter key to view:",end=" ")
key=input()
print("Value of {}:{}".format(key,stats_d[key]))
