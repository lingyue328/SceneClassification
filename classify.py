import os
import shutil

root='./places365/result.txt'
result='./Classify'
def dir_Create(path):
    if not os.path.exists(result+'\\'+path):
        os.makedirs(result+'\\'+path)

dir_Create('Others')

file=open(root)
count=0
for line in file.readlines():
    line=line.strip('\n')
    if count%6==0:
        pic_name=line[3:]
    if (count-1)%6==0:
        L=line.split('(')
        name=L[0].strip(' ')
        dir_Create(name)
        shutil.move(pic_name,result+'\\'+name)
 
    count+=1

file.close()