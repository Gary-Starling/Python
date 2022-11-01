import os

info = open('sometext.txt', 'r') #open
str1 = info.readline()
str2 = info.readline()
info.close

print(str1)
print(str2)

#with open('sometext.txt') as inf:
#	s1 = inf.readline().strip()
#	s2 = inf.readline().strip()
#	s3 = inf.readline().strip()
#	print(s3)


#os.path.join('.','/','sometext.txt')
with open('sometext.txt') as inf:
	for line in inf:
		line = line.strip()
		print(line)

outf = open('sometext.txt','w')
outf.write('new text\n')
outf.write(str(100))
outf.close()
