
import os
import shutil

#file = open("data.txt", "a")
#symbols = file.read()
#print(symbols)
#print(repr(symbols))


#symbols.splitlines()
#print(symbols)



#file.write("line4\n")
#file.close()
#
#file = open("data.txt", "r")
#for stroka in file:
#    #stroka = stroka.rstrip()
#    print(stroka.rstrip())
#file.close()

'''
with open("data.txt") as file, open("data_copy", "w") as wr:
    for line in file:
        wr.write(line)
        print(line.rstrip())
'''

'''
rev_lines = open("data.txt").readlines()
with open("data_reverse.txt", "w") as wr:
    wr.writelines(reversed(rev_lines))
'''

shutil.copy("./data.txt","./copy")
print(os.getcwd())
print(os.listdir())

os.chdir("..")

for current_dir, dir, files in os.walk("."):
    print(current_dir)
    print(dir)
    print(files)

#print(os.path.abspath("main.py"))
#os.chdir("..")
#print(os.getcwd())
#print(os.listdir())