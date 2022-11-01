'''Найти все файлы оканчивающиеся на .py в папке и всех подпапках, записать в файл'''
import os
import shutil
#print(os.path.abspath(os.curdir))
os.chdir("./main")
#print(os.path.abspath(os.curdir))

dir_list = []

for cur_dir, dir, files in os.walk("."):
    for f in files:
        if f.endswith(".py"):
            dir_list.append(cur_dir.replace(".", "main"))
            break

os.chdir("..")
dir_list.sort()
with open("out.txt", "w") as wr:
    for i in dir_list:
        wr.write(i+"\n")