# create a multiplication table of 1 to 3

table = [[i*j for j in range(1,11)] for i in range(1,21)]
print(table)