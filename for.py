exp = [2344,6778,343590,687,9987,9090, 56560, 465469]

total = 0

for i in range(len(exp)):
    print('Month', str(i) +' Expense is: ', str(exp[i]))
    total = total+exp[i]

print('--------------------------')

print('The total is:',total)

print('--------------------------')
for i in range (1,11):
    print(i)