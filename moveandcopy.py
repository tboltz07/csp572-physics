import os
import shutil
from distutils.dir_util import copy_tree
count=0
count2=0
dst = "C:\\Users\\boltz\\PycharmProjects\\untitled\\venv\\Cu\\"
src="C:\Program Files (x86)\JFEFF"
feff_cmd="./ feff"
feff_files=os.listdir(src)
for folder in os.listdir(dst):
    if count<1:
            dst_1 = dst + folder+"\\"
            print("dst1->" + dst_1)
            for molecule in os.listdir(dst_1):
                    dst_2 = dst_1 + molecule
                    if os.path.exists(dst_2) and molecule[len(molecule) - 4:len(molecule)] != ".inp":
                        print("dst2->"+dst_2)
                        copy_tree(src,dst_2)
                        os.chdir(dst_2)
                        os.system(feff_cmd)
                        for item in os.listdir(dst_2):
                            if item in feff_files and "." in item or item=="feff":
                                print("file=>"+item)
                                os.remove(item)
                            elif item in feff_files:
                                print("folder=>"+item)
                                shutil.rmtree(item)



    count+=1

