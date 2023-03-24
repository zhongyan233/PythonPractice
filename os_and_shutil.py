import os
import shutil

def search_dir(dir,result):
    child_files = os.listdir(dir)# 
    for child_file in child_files:
        child_file = os.path.join(dir,child_file)
        if os.path.isdir(child_file):
            search_dir(child_file,result)
        else:
            result.append(child_file)

result = []
search_dir("E:\My Origninal Character",result)
# print(result)
output = "E:\My Origninal Character\picture"
os.makedirs(output)
for file in result:
    if os.path.isfile(file) and (file.endswith("jpg") or file.endswith("png")):
        shutil.move(file,output)