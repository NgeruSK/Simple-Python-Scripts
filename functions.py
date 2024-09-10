exp = [2344,6778,343590,687,9987,9090, 56560, 465469]

exp2 = [564,677,9090,690,850,6768, 7878, 12200]



def calculateAddition(mylist):
    total = 0
    for i in range(len(mylist)):
        print('Month', str(i) +' Expense is: ', str(mylist[i]))
        total = total + mylist[i]
    return total

print('--------------------------')
print('The total for exp 1 is:',calculateAddition(exp))
print('--------------------------')
print('The total for exp 2 is:',calculateAddition(exp2))
print('--------------------------')


#default b equals 0 so might be ommited
def sum (a, b=0):
    return a + b

#defined a and b
print('With 2 params total',sum(4,5))

#defined b only
print('With 1 param total',sum(3))