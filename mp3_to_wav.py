import os
#
# adbshell="ffmpeg -i C:\\Users\\weiwei\\Desktop\\语料合成\\语料\\新建文件夹\\把冰吧的灯关上.mp3 C:\\Users\\weiwei\\Desktop\\语料合成\\语料\\新建文件夹\\把冰吧的灯关上1.wav"
# res=os.system(adbshell)
# print("res: ",res)
# print("type(res):",type(res))

def check_mp3_wav(path):
    files=[]
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        files=files
    mp3_num=0
    wav_num=0
    for file in files:
        if "mp3" in file:
            mp3_num=mp3_num+1
        elif "wav" in file:
            wav_num=wav_num+1
        else:
            print("有其他格式的文件，忽略")

    if mp3_num==wav_num:
        print("mp3数量和wav格式数量相等 ")
    else:
        print("有转换失败的，请检查")


def delete_mp3(path):
    files = []
    for root, dirs, files in os.walk(path):
        print("root: ", root)
        print("dirs: ", dirs)
        print("files: ", files)
        files = files
    for file in files:
        if 'mp3' in file:
            pathtmp=os.path.join(path,file)
            res=os.remove(pathtmp)
            print(res)

def wav_to_wav_tmp(path):
    files=[]
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        files=files
    for file in files:
        file_name=os.path.basename(file)
        #print(file_name)
        file_name_1=file_name.split('.')[0]
        #print(file_name_1)
        wav_name=file_name_1+"towav"+ ".wav"
        #print(wav_name)

        filepath_mp3=os.path.join(path,file)
        filepath_wav=os.path.join(path,wav_name)

        adbshell="ffmpeg -i "+str(filepath_mp3) +" "+str(filepath_wav)
        res=os.system(adbshell)
        if res==0:
            print("转换成功")
        else:
            print("转换失败")

def wav_to_wav(path):
    #单通道wav类型转化位双通道的wav
    files = []
    for root, dirs, files in os.walk(path):
        print("root: ", root)
        print("dirs: ", dirs)
        print("files: ", files)
        files = files
    for file in files:
        filesrc=os.path.join(path,file)
        res="new_wav_"+file
        fileres=os.path.join(path,res)

        adbshell = "ffmpeg -i " + filesrc + " -ac 2 " + fileres
        res = os.system(adbshell)
        if res == 0:
            print("转换成功")
        else:
            print("转换失败")



def mp3_to_wav(path):
    files=[]
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        files=files
    for file in files:
        file_name=os.path.basename(file)
        #print(file_name)
        file_name_1=file_name.split('.')[0]
        #print(file_name_1)
        wav_name=file_name_1+ ".wav"
        #print(wav_name)

        filepath_mp3=os.path.join(path,file)
        filepath_wav=os.path.join(path,wav_name)

        adbshell="ffmpeg -i "+str(filepath_mp3) +" "+str(filepath_wav)
        res=os.system(adbshell)
        if res==0:
            print("转换成功")
        else:
            print("转换失败")
    check_mp3_wav(path)

def pcm_to_wav(path):
    files=[]
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        files=files
    for file in files:
        file_name=os.path.basename(file)
        #print(file_name)
        file_name_1=file_name.split('.')[0]
        #print(file_name_1)
        wav_name=file_name_1+ ".wav"
        #print(wav_name)

        filepath_pcm=os.path.join(path,file)
        print("filepath_pcm: ",filepath_pcm)
        filepath_wav=os.path.join(path,wav_name)

        #adbshell="ffmpeg -y -f u8 -ar 11025 -ss 00:00:10 -t 00:01:22 -i "+str(filepath_pcm) +" -c:a libmp3lame -q:a 8 "+str(filepath_wav)

        adbshell="ffmpeg.exe -f s16le -ar 16000 -ac 1 -i" +" "+ filepath_pcm+" " +filepath_wav

        res=os.system(adbshell)
        if res==0:
            print("转换成功")
        else:
            print("转换失败")

    # check_mp3_wav(path)

def delete_pcm(path):
    files = []
    for root, dirs, files in os.walk(path):
        print("root: ", root)
        print("dirs: ", dirs)
        print("files: ", files)
        files = files
    for file in files:
        if 'pcm' in file:
            pathtmp=os.path.join(path,file)
            res=os.remove(pathtmp)
            print(res)




if __name__=="__main__":
    path="C:\\Users\\weiwei\\Desktop\\_197f545b02ba44738d5bfa51d573489c\\"
    # pcm_to_wav(path)
    delete_pcm(path)


    # path="C:\\Users\\weiwei\\Desktop\\格式不正确小优小优\\小优小优"
    # wav_to_wav(path)
    # #mp3_to_wav(path)
    # delete_mp3(path)


    # pathfile = 'C:\\Users\\weiwei\\Desktop\\语音\\小优小优无法播放的\\小优小优'
    # wav_to_wav(pathfile)
