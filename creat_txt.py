import os
def write_txt(path,file):
    #filepath=os.path.join(path,file)
    #print("filepath: ",filepath)
    text=file.split('.')[0]
    file_txt=text+'.txt'
    filepath=os.path.join(path,file_txt)
    print("filepath: ", filepath)
    # text=str(text)
    # print(text)
    print(text)
    with open(filepath,'w',encoding='utf-8') as f:
        f.write(text)
    #pass
def handle_txt(path):
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        for file in files:
            write_txt(root,file)

    # root,dirs,files=os.walk(path)
    # print("root: ",root)
    # print("dirs: ",dirs)
    # print("files: ",files)

def test_(file1=None,file2=None):
    print("file1: ",file1)
    print("file2: ",file2)


if __name__=="__main__":
    #text='nihao'
    # test_(file1=text)
    path=os.getcwd()
    path=os.path.join(path,'Result')
    print("path: ",path)
    handle_txt(path)


