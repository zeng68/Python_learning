dir_path = 'E:\\txt\\zqg.txt'
dir_path2 = 'E:\\txt\\zqg2.txt'
# a = 3
# with open(dir_path, 'a') as f:
#     a = a + 1
#     f.write(str(a)+'\n')1


with open(dir_path, 'r') as f1:
    with open(dir_path2,'w')as f2:
        for file in f1:
            file = file.strip().replace('，','').replace('。','')
            f2.write(file+'\n')
