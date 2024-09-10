my_list = ['Simon', 'Bonny']

#add item to last index plus 1
my_list.append('Marto')

#insert function to specific index
my_list.insert(1, 'Ngeru')

#subsets
print(my_list[0:0])

print('Length of list is: '+ str(len(my_list)))

#searcgh function
print('Simon' in my_list)

for item in my_list:
    print(item)