f =  open("c:/Users/intuser/Simon/Projects/Python/HelloWorlds/funny.txt","r")
f_out =  open("c:/Users/intuser/Simon/Projects/Python/HelloWorlds/funny_wc.txt","w")

#f.write("\n I love python")
#print(f.read())

for line in f:
    #print num characters in each
    print("Number of characters:",len(line))
    #print num of words
    num_words = line.split(' ')
   # print(len("\n Number of words: " + str(len(num_words))))
    f_out.write("Wordcount: "+ str(len(num_words)) + " Sentence: "+line)

f.close()
f_out.close()