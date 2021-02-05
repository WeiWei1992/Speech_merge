from operate_excel import handle_excel,write_excel
from aibaidu import baidu_mp3
import time
import os
from tkinter import *
from creat_txt import handle_txt
import logging
import logging.config
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
def baidu_speech_merge(tk_text,filepath=None,mp3fold=None):
    if not filepath:
        filepath='语料.xlsx'
    location=handle_excel(filepath)
    for i in range(len(location)):
        text=location[i][2]
        tmp="百度合成语料..."+str(text)+"\n"
        tk_text.insert(END,tmp)
        logging.info(tmp)
        result=baidu_mp3(text,mp3fold)
        write_excel(location[i],result,filepath)
        time.sleep(1)
    if not mp3fold:
        path=os.getcwd()
        mp3fold=os.path.join(path,'Result')
    tk_text.insert(END,"语料合成结束，为语料生成txt文件...\n")
    logging.info("语料合成结束，为语料生成txt文件...")
    #handle_txt(mp3fold)
    tk_text.insert(END,"txt文件生成完成\n")
    tk_text.insert(END,"语料合成完成")
    logging.info("txt文件生成完成,语料合成完成")


if __name__=="__main__":
    mp3fold="C:\\Users\\weiwei\\Desktop\\电热水器语音通用模块R328 V1.2.0版本提测质量部"
    #baidu_speech_merge()