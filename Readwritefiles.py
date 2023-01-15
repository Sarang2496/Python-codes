fw = open('sample.txt', 'w')
fw.write('Some random stuff \n ')
fw.write('I like cheese! \n ')
fw.close()


### to read a file

fr = open('sample.txt','r')
text =fr.read()
print(text)
fr.close()