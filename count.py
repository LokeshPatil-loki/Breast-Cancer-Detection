import os

# folder path
dir_path = r'/home/loki/Downloads/archive'
# print(os.listdir(dir_path))
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    path1 = dir_path + "/"+path+"/0"
    path2 = dir_path + "/"+path+"/1"
    print(path)
    print("\t0: ", len(os.listdir(path1)), "\n\t1: ", len(os.listdir(path2)))
# print('File count:', count)
