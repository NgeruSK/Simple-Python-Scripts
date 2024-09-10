import json

books = {}

books['tom'] = {
'publisher':'Mark Otis',
'year':'2008',
'isbn-no':'FKI-09-56',
'copies':34
}

books['saish'] = {
'publisher':'Meko Ngeru',
'year':'2018',
'isbn-no':'FKI-09-90',
'copies':46
}


books_obj = json.dumps(books)
#print(books)

#Writing the file
# with open("c:/Users/intuser/Simon/Projects/Python/HelloWorlds/books.txt","w") as f:
#     f.write(books_obj)
#     f.close()


#Reading the file
f =  open("c:/Users/intuser/Simon/Projects/Python/HelloWorlds/books.txt","r")
read_obj = json.loads(f.read()) 
print(type(read_obj))
#accessing isbn - no
#print(read_obj['tom']['isbn-no'])

#preview
for book in books:
    print(book)
    print(books[book])