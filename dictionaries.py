phonebook = {"tom":789999, "mike":7899666, "Tina":782652552}

#all show
print(phonebook)

#for mike
print(phonebook["mike"])

#adding element
phonebook["ngeru"] = 78999998

#deleting element
del phonebook["tom"]

#re-add tom
phonebook["tom"] = 76834345

#iterate through them
for key in phonebook:
    print("key:", key, "value:", phonebook[key])

#using tuples
print('----tuple view----')
for k, v in phonebook.items():
    print('key:',key,'value:',v)

#search
print("tom" in phonebook)