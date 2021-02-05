import os
import time
from datetime import datetime
import re
import pyaudio
import wave
def play_wav(filepath):
    # 播放wav文件
    chunk = 1024
    # 从目录中读取语音
    wf = wave.open(filepath, 'rb')
    #print("wf: ",wf)
    data = wf.readframes(chunk)
    #print("data: ",data)
    # 创建播放器
    p = pyaudio.PyAudio()

    # 获得语音文件的各个参数
    FORMAT = p.get_format_from_width(wf.getsampwidth())
    CHANELS = wf.getnchannels()
    RATE = wf.getframerate()
    # print('FORMAF:{} \nCHANELS: {}\nRATE: {}'.format(FORMAT,CHANELS,RATE))
    str_tmp = 'FORMAF:{} \nCHANELS:{}\nRATE:{}'.format(FORMAT, CHANELS, RATE)
    print("播放的系统参数\n" + str_tmp)
    # 打开音频流，output=True表示音频输出
    stream = p.open(format=FORMAT,
                    channels=CHANELS,
                    rate=RATE,
                    frames_per_buffer=chunk,
                    output=True)
    # while data !='':
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()
    # print("播放结束")
    print("播放结束")

if __name__=="__main__":
    pathfile='C:\\Users\\weiwei\\Desktop\\语音\\小优小优无法播放的\\小优小优\\迟洪鑫.wav'
    # pathfile2='C:\\Users\\weiwei\\Desktop\\语音\\xiaoyou\\chihongxin-cvt.wav'
    # play_wav(pathfile)

    pathfile3='C:\\Users\\weiwei\\Desktop\\语音\\小优小优无法播放的\\小优小优\\2.wav'
    play_wav(pathfile3)
    # adbshell =  "ffmpeg -i " + pathfile + " -ac 2 " + pathfile3
    #
    # res = os.system(adbshell)
    # if res == 0:
    #     print("转换成功")
    # else:
    #     print("转换失败")