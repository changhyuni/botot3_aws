import os
count = 0

if __name__ == "__main__":
    root_dir = "/mnt/c/Users/DELL/Desktop/grow-ansible/test"
    for (root, dirs, files) in os.walk(root_dir):
        print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                print("Dir Name : " + dir_name)

        if len(files) > 0:
            for file_name in files:
                count += 1
                print("File Name : " + file_name)
                
    print('총 파일 갯수는 {}개 입니다.'.format(count))
